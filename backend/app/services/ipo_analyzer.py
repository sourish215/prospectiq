from app.services.rules_loader import load_rules

def analyze_document(text):

    rules = load_rules()

    score = 0

    for rule in rules:

        if rule["description"].lower() in text.lower():
            score += rule["weight"]

    return {"score": score}
