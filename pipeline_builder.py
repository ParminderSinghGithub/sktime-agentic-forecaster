def build_pipeline(estimator_name: str) -> list[str]:
    return ["Imputer", estimator_name]
