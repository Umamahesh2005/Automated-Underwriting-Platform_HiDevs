# src/routing.py

def route_claim(claim_type, priority):
    if claim_type == "Fire" and priority == "High":
        return "Route to Emergency Fire Claims Team"
    elif priority == "Low":
        return "Queue for Routine Review"
    else:
        return "Send to General Claims Team"
