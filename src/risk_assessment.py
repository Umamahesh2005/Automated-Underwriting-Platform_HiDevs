# src/risk_assessment.py

def assess_risk(document_info, image_info):
    image_info_lower = image_info.lower()
    
    # Priority order: High > Medium > Low
    if document_info["fire_safety"] == "No" or "boathouse" in image_info_lower:
        return "High"
    
    if "crack" in image_info_lower or "broken" in image_info_lower:
        return "Medium"

    return "Low"
