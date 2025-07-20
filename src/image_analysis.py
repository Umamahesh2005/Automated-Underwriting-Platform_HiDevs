import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
import json
import os

# Load ImageNet class labels
try:
    with open("imagenet_class_index.json") as f:
        class_idx = json.load(f)
except Exception as e:
    print(f"[ERROR] Failed to load class index file: {e}")
    class_idx = {}

# Load pre-trained ResNet50 model
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()

def get_label(index):
    overrides = {
        "449": "house"  # Override for ImageNet class 449 (boathouse)
    }

    str_index = str(index)
    if str_index in overrides:
        return overrides[str_index]
    
    return class_idx.get(str_index, ["", "Unknown"])[1]

def analyze_image(image_path):
    try:
        if not os.path.exists(image_path):
            return "Error analyzing image: Image file not found."

        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        image = Image.open(image_path).convert("RGB")
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = model(input_batch)
        
        _, predicted_idx = torch.max(output, 1)
        class_index = predicted_idx.item()
        label = get_label(class_index)

        return f"Predicted class index: {class_index} - {label}"
    
    except Exception as e:
        return f"Error analyzing image: {e}"
