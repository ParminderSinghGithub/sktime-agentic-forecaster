from pipeline_builder import build_pipeline
from typing import Any


def _select_estimator(prompt: str) -> tuple[str, str]:
    normalized_prompt = prompt.lower()

    if "simple" in normalized_prompt or "baseline" in normalized_prompt:
        return (
            "NaiveForecaster",
            "Prompt suggests a simple or baseline approach, so NaiveForecaster is selected.",
        )

    if "trend" in normalized_prompt or "seasonal" in normalized_prompt:
        return (
            "ExponentialSmoothing",
            "Prompt suggests trend or seasonal structure, so ExponentialSmoothing is selected.",
        )

    return (
        "NaiveForecaster",
        "No strong signal was found, so NaiveForecaster is used as the default.",
    )


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

    selected_estimator, selection_reasoning = _select_estimator(query)
    print("\n2. Estimator selection")
    print(f"Selected estimator: {selected_estimator}")
    print(f"Reasoning: {selection_reasoning}")

    print("\n3. MCP tool call: describe_estimator")
    estimator_description = _simulate_describe_estimator(selected_estimator)
    print(estimator_description)

    print("\n4. Building pipeline")
    pipeline = build_pipeline(selected_estimator)
    print(f"Pipeline: {pipeline}")

    print("\n5. MCP tool call: validate_pipeline")
    validation = _simulate_validation(pipeline)
    print(validation)

    print("\n6. MCP tool call: instantiate_pipeline")
    instantiation = {"success": True, "handle": "mock_pipeline_handle", "pipeline": pipeline}
    print(instantiation)

    print("\n7. MCP tool call: load_data_source")
    loaded_data = {
        "success": True,
        "data_handle": "mock_data_handle",
        "dataset": "airline",
    }
    print(loaded_data)

    print("\n8. MCP tool call: fit_predict")
    prediction_output = _simulate_prediction()
    print(prediction_output)

    return {
        "selected_estimator": selected_estimator,
        "pipeline": pipeline,
        "validation": validation,
        "instantiation": instantiation,
        "loaded_data": loaded_data,
        "prediction_output": prediction_output,
        "reasoning": selection_reasoning,
        "estimator_description": estimator_description,
        "list_estimators_response": list_estimators_response,
    }
