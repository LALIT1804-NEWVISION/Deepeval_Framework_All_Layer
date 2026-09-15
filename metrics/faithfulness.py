from deepeval.metrics import FaithfulnessMetric
from config.settings import THRESHOLD
def create_faithfulness_metric(model):
    return FaithfulnessMetric(
        threshold=THRESHOLD,
        model=model,
        include_reason=True,
        async_mode=False
    )