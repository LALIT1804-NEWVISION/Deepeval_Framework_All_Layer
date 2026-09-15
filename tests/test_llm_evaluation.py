import allure
import pytest

from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel

from config.settings import (
    TEST_DATA_FILE,
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    TEMPERATURE
)

from utils.data_loader import load_test_data

from metrics import (
    create_answer_relevancy_metric,
    create_faithfulness_metric,
    create_contextual_precision_metric
)

# NEW
from agents.supervisor_agent import supervisor_agent

# Load Test Data from Json File

test_data = load_test_data(TEST_DATA_FILE)

# Ollama Model

evaluation_model = OllamaModel(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=TEMPERATURE
)

# Create Metrics

answer_relevancy_metric = create_answer_relevancy_metric(evaluation_model)
faithfulness_metric = create_faithfulness_metric(evaluation_model)
contextual_precision_metric = create_contextual_precision_metric(evaluation_model)

# Metrics List

metrics = [answer_relevancy_metric,faithfulness_metric,contextual_precision_metric]

# Generate Actual Output

# def generate_actual_output(input_question, retrieval_context):
#     context = "\n".join(retrieval_context)
#     prompt = f"""
# You are a helpful assistant.
# Answer the user's question using only the provided context.
# Context:{context}Question:{input_question}
# Provide a clear and concise answer.
# """ 
#     response = evaluation_model.generate(prompt)
#     return response[0]

# Generate Actual Output using Multi-Agent

def generate_actual_output(input_question, retrieval_context):

    actual_output = supervisor_agent(
        input_question,
        retrieval_context,
        evaluation_model
    )

    return actual_output


# LLM Evaluation Test

@pytest.mark.parametrize(
    "test_case_data",
    test_data,
    ids=[item["id"] for item in test_data]
)
def test_llm_evaluation(test_case_data):

    # Generate Actual Output Dynamically
    # Generate Actual Output using Multi-Agent
    actual_output = generate_actual_output(
        test_case_data["input"],
        test_case_data["retrieval_context"]
    )
    print("\nQuestion:", test_case_data["input"])
    print("Actual Output:", actual_output)

    allure.attach(
        test_case_data["input"],
        name="Question",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        str(actual_output),
        name="Actual Output",
        attachment_type=allure.attachment_type.TEXT
    )
    
    # Create DeepEval Test Case
    test_case = LLMTestCase(
    input=test_case_data["input"],
    actual_output=actual_output,
    expected_output=test_case_data["expected_output"],
    retrieval_context=test_case_data["retrieval_context"]
)
    # Run DeepEval Evaluation

    assert_test(
        test_case=test_case,
        metrics=metrics
    )

