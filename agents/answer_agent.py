def answer_agent(query: str, context: str, evaluation_model) -> str:

    prompt = f"Answer the question using only this context.\nContext: {context}\nQuestion: {query}"

    response = evaluation_model.generate(prompt)

    return response[0]