from agents.research_agent import research_agent
from agents.answer_agent import answer_agent

def supervisor_agent(query: str,retrieval_context: list,evaluation_model) -> str:

    # Step 1: Research Agent
    research_result = research_agent(query,retrieval_context)

    # Step 2: Answer Agent
    final_answer = answer_agent(query,research_result,evaluation_model)

    # Step 3: Final response
    return final_answer