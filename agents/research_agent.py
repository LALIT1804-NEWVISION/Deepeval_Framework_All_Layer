def research_agent(query: str,retrieval_context: list) -> str:

    context = "\n".join(retrieval_context)

    if not context:
        return "No relevant information found."

    return context