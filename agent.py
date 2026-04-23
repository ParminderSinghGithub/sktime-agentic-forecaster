def _select_forecasting_model(normalized_prompt: str) -> tuple[str, str]:
    if "simple" in normalized_prompt or "baseline" in normalized_prompt:
        return "NaiveForecaster", "Selected NaiveForecaster because prompt indicated a simple or baseline approach."

    if "trend" in normalized_prompt or "seasonal" in normalized_prompt:
        return "ExponentialSmoothing", "Selected ExponentialSmoothing because prompt indicated trend or seasonal structure."

    return "NaiveForecaster", "Selected NaiveForecaster as the default forecasting model."


def build_pipeline_from_prompt(prompt: str):
    normalized_prompt = prompt.lower()
    model_name, reasoning = _select_forecasting_model(normalized_prompt)
    pipeline = ["Imputer", model_name]
    return pipeline, reasoning
