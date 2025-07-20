from document_analysis import extract_text_from_image, analyze_document
from image_analysis import analyze_image
from risk_assessment import assess_risk
from compliance import check_compliance
from routing import route_claim  # ✅ Import claim routing logic

def main():
    # Sample input files (make sure these exist)
    document_path = "data/sample_docs/sample_doc1.png"
    image_path = "data/sample_images/sample_image1.png"
    
    # Step 1: Extract and analyze document
    print("📄 Extracting text from document...")
    text = extract_text_from_image(document_path)
    
    # (Optional but useful) Debugging line to see OCR output
    print("🔎 Extracted Text:\n", text)

    doc_info = analyze_document(text)

    # Step 2: Analyze image
    print("🖼️  Analyzing property image...")
    image_info = analyze_image(image_path)

    # Step 3: Assess risk
    print("📊 Assessing property risk...")
    risk_score = assess_risk(doc_info, image_info)

    # Step 4: Check compliance
    print("✅ Checking underwriting compliance...")
    compliance_status = check_compliance(doc_info)

    # Step 5: Route the claim (NEW)
    claim_type = doc_info.get("claim_type", "Unknown")
    priority = doc_info.get("priority", "Low")
    routing_decision = route_claim(claim_type, priority)

    # Step 6: Final Report - Print and Save
    report_output = (
        "\n================== Final Underwriting Report ==================\n"
        f"🏠 Property Type       : {doc_info.get('property_type', 'N/A')}\n"
        f"🔥 Fire Safety Present : {doc_info.get('fire_safety', 'N/A')}\n"
        f"📄 Claim Type           : {claim_type}\n"
        f"⚡ Priority Level       : {priority}\n"
        f"🖼️  Image Analysis      : {image_info}\n"
        f"⚠️  Risk Score          : {risk_score}\n"
        f"🧾 Compliance Status   : {compliance_status}\n"
        f"🚚 Routing Decision     : {routing_decision}\n"
        "===============================================================\n"
    )

    print(report_output)

    # Save to file
    with open("final_report.txt", "w") as f:
        f.write(report_output)

if __name__ == "__main__":
    main()
