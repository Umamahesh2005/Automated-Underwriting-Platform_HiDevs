# src/compliance.py
def check_compliance(document_info):
    if document_info["fire_safety"] == "Yes":
        return "Compliant"
    else:
        return "Non-Compliant"
