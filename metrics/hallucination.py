from deepeval.metrics import HallucinationMetric
from config.settings import THRESHOLD
def create_hallucination_metric(model):

    return HallucinationMetric(
        threshold=THRESHOLD,
        model=model,
        include_reason=True,
        async_mode=False
    )