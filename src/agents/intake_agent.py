def intake_agent(query):
    query = query.lower()
    questions = []

    if "completed" not in query:
        questions.append("What courses have you completed?")

    if "program" not in query:
        questions.append("Which program are you targeting?")

    return questions