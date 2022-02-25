from functools import lru_cache
from transformers import pipeline


@lru_cache()
def load_zeroshot_model(model_name="valhalla/distilbart-mnli-12-6"):
    classifier = pipeline("zero-shot-classification", model=model_name)
    return classifier
