def build_pipeline_from_prompt(prompt: str):
    if "simple" in prompt.lower():
        return ["NaiveForecaster"]
    return []
