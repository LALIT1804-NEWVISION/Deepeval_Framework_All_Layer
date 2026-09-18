from deepeval.metrics import ContextualRelevancyMetric

def create_contextual_relevancy_metric(evaluation_model):

    return ContextualRelevancyMetric(
        threshold=0.7,
        model=evaluation_model,
        include_reason=True
    )