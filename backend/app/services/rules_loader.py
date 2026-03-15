import json

def load_rules():

    with open("rules/ipo_rules.json") as f:
        data = json.load(f)

    return data["rules"]
