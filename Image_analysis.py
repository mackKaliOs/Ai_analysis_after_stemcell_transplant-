# Requires: ultralytics (YOLOv8), OpenCV, CLIP, PIL, torch, torchvision
# pip install ultralytics openai-clip torch torchvision opencv-python

import torch
import clip
from PIL import Image
import os
import cv2
from ultralytics import YOLO
import pandas as pd

# Load models
device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model, preprocess = clip.load("ViT-B/32", device=device)
yolo_model = YOLO("yolov8m.pt")  # or a custom-trained home inventory model

# Define key environmental risks
TAGS = [
    "air freshener",
    "bleach",
    "dryer sheet",
    "plastic water bottle",
    "fragrance",
    "cleaning spray",
    "kitty litter",
    "candle",
    "fabric softener",
    "Teflon pan",
    "pet food",
    "pet bedding",
    "visible mold",
    "humidifier",
    "mildew",
    "vinyl shower curtain",
    "chemical detergent",
    "pesticide",
    "weed killer",
    "air purifier",
    "plants",
    "HEPA filter",
    "glass container",
    "organic cleaner",
    "BPA bottle"
]

# Prompt-friendly class groups for output clarity
XENOESTROGENS = ["dryer sheet", "fragrance", "plastic water bottle", "fabric softener", "vinyl shower curtain"]
MOLD_TRIGGERS = ["visible mold", "humidifier", "mildew", "kitty litter"]
PET_RISKS = ["kitty litter", "pet food", "pet bedding"]
CARCINOGENS = ["bleach", "cleaning spray", "pesticide", "weed killer", "Teflon pan"]
SAFE_ITEMS = ["air purifier", "plants", "HEPA filter", "glass container", "organic cleaner"]

# Directory to analyze
IMAGE_DIR = "input_photos/"
results = []

# Analysis function
def analyze_image(img_path):
    print(f"Processing {img_path}")
    image = Image.open(img_path).convert("RGB")
    processed = preprocess(image).unsqueeze(0).to(device)

    # Use CLIP to detect risk tags semantically
    text_inputs = torch.cat([clip.tokenize(f"a photo of {c}") for c in TAGS]).to(device)
    with torch.no_grad():
        image_features = clip_model.encode_image(processed)
        text_features = clip_model.encode_text(text_inputs)
        logits_per_image, _ = clip_model(processed, text_inputs)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()[0]

    top_indices = probs.argsort()[-10:][::-1]
    detections = [(TAGS[i], probs[i]) for i in top_indices if probs[i] > 0.15]

    # YOLO detection for common objects
    yolo_results = yolo_model(img_path)[0]
    yolo_labels = yolo_results.names
    yolo_detected = [yolo_labels[int(cls)] for cls in yolo_results.boxes.cls]

    return {
        "file": os.path.basename(img_path),
        "clip_detections": detections,
        "yolo_objects": yolo_detected
    }

# Run on all images
for file in os.listdir(IMAGE_DIR):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        full_path = os.path.join(IMAGE_DIR, file)
        res = analyze_image(full_path)
        results.append(res)

# Classify risks and build report
df_output = []
for r in results:
    found = [item[0] for item in r["clip_detections"]]
    xeno = [f for f in found if f in XENOESTROGENS]
    mold = [f for f in found if f in MOLD_TRIGGERS]
    pet = [f for f in found if f in PET_RISKS]
    carcinogens = [f for f in found if f in CARCINOGENS]
    safe = [f for f in found if f in SAFE_ITEMS]

    df_output.append({
        "Image": r["file"],
        "Xenoestrogens": ", ".join(xeno),
        "Mold Triggers": ", ".join(mold),
        "Pet Hazards": ", ".join(pet),
        "Carcinogens": ", ".join(carcinogens),
        "Safe Items": ", ".join(safe),
        "YOLO Objects": ", ".join(r["yolo_objects"])
    })

# Save to CSV report
df = pd.DataFrame(df_output)
df.to_csv("environmental_analysis_report.csv", index=False)
print("✅ Analysis complete. CSV saved.")
