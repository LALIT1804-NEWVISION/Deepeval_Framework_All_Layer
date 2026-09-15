from deepeval.metrics import AnswerRelevancyMetric
from config.settings import THRESHOLD
def create_answer_relevancy_metric(model):
    return AnswerRelevancyMetric(
        threshold=THRESHOLD,
        model=model,
        include_reason=True,
        async_mode=False
    )