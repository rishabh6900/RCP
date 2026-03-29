def planner_agent(llm, prompt, query, context):
    formatted_prompt = prompt.format(query=query, context=context)
    response = llm.invoke(formatted_prompt)
    return response.content