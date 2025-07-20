# 🏡 Automated Underwriting Platform

## 📌 Overview
This project automates the underwriting process for property insurance by:
- 📄 Extracting key information from property documents using OCR (Tesseract)
- 🖼️ Analyzing property images using a pre-trained deep learning model
- ⚠️ Assessing risk score based on fire safety and image clues
- ✅ Checking underwriting compliance

---

## ⚙️ How It Works

### 1. 🧾 Document Analysis  
Uses OCR (`pytesseract`) to extract structured data from scanned documents:
- Claim type (e.g., Fire, Theft)
- Priority (e.g., High, Low)
- Property type (e.g., Residential, Villa, Apartment)
- Fire safety indicators (fire extinguisher, alarm, etc.)

### 2. 🖼️ Image Analysis  
Utilizes a pre-trained **ResNet50** model from PyTorch to classify property images:
- Custom class override: class index `449` labeled as "house"
- Helps detect risky assets like boathouses or unknown structures

### 3. ⚠️ Risk Assessment & Compliance Check  
Combines insights from document and image analysis to:
- Compute a risk level: High / Medium / Low
- Flag missing fire safety equipment
- Mark the claim as **Compliant** or **Non-Compliant**

### 4. 📊 Final Underwriting Report  
Displays a summary in the terminal and saves it to `final_report.txt`:

🏠 Property Type : Residential
🔥 Fire Safety Present : Yes
📄 Claim Type : Fire
⚡ Priority Level : High
🖼️ Image Analysis : Predicted class index: 449 - house
⚠️ Risk Score : Low
🧾 Compliance Status : Compliant
🚚 Routing Decision : Route to Emergency Fire Claims Team


---

## 🚀 How to Run

### 1. 📥 Install dependencies

Make sure Python 3 is installed. Then run:

```bash
python3 -m venv .venv
source .venv/bin/activate        # For macOS/Linux
.venv\Scripts\activate           # For Windows
pip install -r requirements.txt
