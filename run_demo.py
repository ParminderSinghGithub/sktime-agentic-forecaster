from agent import run_agent


def main():
    result = run_agent("Forecast airline passengers")
    print("\nFinal summary")
    print("Selected estimator:", result["selected_estimator"])
    print("Pipeline:", result["pipeline"])
    print("Prediction output:", result["prediction_output"])


if __name__ == "__main__":
    main()