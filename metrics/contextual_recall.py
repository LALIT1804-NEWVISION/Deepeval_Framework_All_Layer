from deepeval.metrics import ContextualRecallMetric

def create_contextual_recall_metric(evaluation_model):

    return ContextualRecallMetric(
        threshold=0.7,
        model=evaluation_model,
        include_reason=True
    )