def extract_text_from_image(image_path):
    from PIL import Image
    import pytesseract
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Error extracting text: {e}"

def analyze_document(text):
    # Normalize and flatten lines
    lines = [line.strip().lower() for line in text.splitlines() if line.strip()]
    full_text = " ".join(lines)

    # Detect Property Type
    if "apartment" in full_text:
        property_type = "Apartment"
    elif "villa" in full_text:
        property_type = "Villa"
    elif "boathouse" in full_text:
        property_type = "Boathouse"
    elif "house" in full_text:
        property_type = "House"
    elif "residential" in full_text:
        property_type = "Residential"
    else:
        property_type = "Unknown"

    # Detect Fire Safety
    fire_safety_keywords = [
        "fire extinguisher", "fire alarm", "fire safety",
        "smoke detector", "fire safety: yes"
    ]
    fire_safety = "Yes" if any(word in full_text for word in fire_safety_keywords) else "No"

    # Detect Claim Type & Priority
    if "claim type: fire" in full_text or "fire damage" in full_text or "burnt" in full_text:
        claim_type = "Fire"
        priority = "High"
    elif "claim type: water" in full_text or "water leak" in full_text or "flood" in full_text:
        claim_type = "Water"
        priority = "Medium"
    elif "glass broken" in full_text or "theft" in full_text or "stolen" in full_text:
        claim_type = "Theft"
        priority = "Medium"
    elif "claim type: accident" in full_text or "accident" in full_text or "crash" in full_text:
        claim_type = "Accident"
        priority = "High"
    else:
        claim_type = "Unknown"
        priority = "Low"

    return {
        "property_type": property_type,
        "fire_safety": fire_safety,
        "claim_type": claim_type,
        "priority": priority
    }
