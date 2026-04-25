from pipeline_builder import build_pipeline
from typing import Any


def extract_intent(prompt: str) -> dict[str, str]:
    normalized_prompt = prompt.lower()

    if any(word in normalized_prompt for word in ("simple", "baseline", "naive", "basic")):
        complexity = "simple"
    else:
        complexity = "advanced"

    if "trend" in normalized_prompt:
        pattern = "trend"
    elif "seasonal" in normalized_prompt:
        pattern = "seasonal"
    else:
        pattern = "none"

    return {"complexity": complexity, "pattern": pattern}


def _select_estimator(intent: dict[str, str]) -> str:
    if intent["complexity"] == "simple":
        return "NaiveForecaster"

    if intent["pattern"] in {"trend", "seasonal"}:
        return "ExponentialSmoothing"

    return "NaiveForecaster"


def _confidence_score(intent: dict[str, str]) -> float:
    if intent["complexity"] == "simple":
        return 0.9

    if intent["pattern"] in {"trend", "seasonal"}:
        return 0.85

    return 0.7


def _alternative_models(selected_estimator: str) -> list[str]:
    alternatives = ["NaiveForecaster", "ExponentialSmoothing"]
    return [model for model in alternatives if model != selected_estimator]


def generate_explanation(intent: dict[str, str], model: str) -> str:
    if intent["complexity"] == "simple":
        return f"Selected {model} because the prompt looks simple and a baseline forecaster is appropriate."

    if intent["pattern"] == "trend":
        return f"Selected {model} because the prompt suggests a trend pattern that benefits from smoothing."

    if intent["pattern"] == "seasonal":
        return f"Selected {model} because the prompt suggests seasonal structure that benefits from smoothing."

    return f"Selected {model} as a safe default because the prompt did not strongly indicate a trend or seasonal pattern."


def _select_estimator_details(prompt: str) -> tuple[dict[str, str], str, float, list[str], str]:
    intent = extract_intent(prompt)
    selected_estimator = _select_estimator(intent)
    reasoning = generate_explanation(intent, selected_estimator)
    confidence = _confidence_score(intent)
    alternatives = _alternative_models(selected_estimator)
    return intent, selected_estimator, confidence, alternatives, reasoning


def _simulate_list_estimators() -> dict[str, list[dict[str, str]]]:
    return {
        "estimators": [
            {"name": "NaiveForecaster"},
            {"name": "ExponentialSmoothing"},
        ]
    }


def _simulate_describe_estimator(estimator_name: str) -> dict[str, str]:
    return {
        "name": estimator_name,
        "task": "forecasting",
        "description": f"Mock description for {estimator_name}.",
    }


def _simulate_validation(pipeline: list[str]) -> dict[str, Any]:
    return {"valid": True, "pipeline": pipeline}


def _simulate_prediction() -> list[int]:
    return [100, 110, 120]


def run_agent(query: str) -> dict[str, Any]:
    print(f"User query: {query}")

    print("\n1. MCP tool call: list_estimators(query=\"forecasting\")")
    list_estimators_response = _simulate_list_estimators()
    print(list_estimators_response)

    intent, selected_estimator, confidence, alternatives, selection_reasoning = _select_estimator_details(query)
    print("\n2. Intent extraction")
    print(intent)

    print("\n3. Estimator selection")
    print(f"Selected estimator: {selected_estimator}")
    print(f"Reasoning: {selection_reasoning}")
    print(f"Confidence: {confidence}")
    print(f"Alternatives: {alternatives}")

    print("\n4. MCP tool call: describe_estimator")
    estimator_description = _simulate_describe_estimator(selected_estimator)
    print(estimator_description)

    print("\n5. Building pipeline")
    pipeline = build_pipeline(selected_estimator)
    print(f"Pipeline: {pipeline}")

    print("\n6. MCP tool call: validate_pipeline")
    validation = _simulate_validation(pipeline)
    print(validation)

    print("\n7. MCP tool call: instantiate_pipeline")
    instantiation = {"success": True, "handle": "mock_pipeline_handle", "pipeline": pipeline}
    print(instantiation)

    print("\n8. MCP tool call: load_data_source")
    loaded_data = {
        "success": True,
        "data_handle": "mock_data_handle",
        "dataset": "airline",
    }
    print(loaded_data)

    print("\n9. MCP tool call: fit_predict")
    prediction_output = _simulate_prediction()
    print(prediction_output)

    return {
        "intent": intent,
        "selected_estimator": selected_estimator,
        "confidence": confidence,
        "alternatives": alternatives,
        "pipeline": pipeline,
        "validation": validation,
        "instantiation": instantiation,
        "loaded_data": loaded_data,
        "prediction_output": prediction_output,
        "reasoning": selection_reasoning,
        "estimator_description": estimator_description,
        "list_estimators_response": list_estimators_response,
    }
