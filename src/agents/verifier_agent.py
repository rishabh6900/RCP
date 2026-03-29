def verifier_agent(query, answer):
    if "Citations:" not in answer:
        return "Missing citations"
    return "Verified"