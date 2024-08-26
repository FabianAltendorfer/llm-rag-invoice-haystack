from haystack.components.generators import HuggingFaceAPIGenerator
import os

def setup_llm(model_name):
    return HuggingFaceAPIGenerator(api_type="serverless_inference_api",
                                    api_params={"model": model_name},
                                    token=os.getenv("HUGGINGFACE_API_TOKEN"))