# sktime-agentic-forecaster

## Overview
sktime-agentic-forecaster is a minimal agentic forecasting prototype. It converts a natural-language query into a structured forecasting pipeline, executes a deterministic prediction, and explains the reasoning behind its decisions.

This demonstrates how agentic systems can perform transparent, auditable decision-making rather than relying on opaque or trial-and-error workflows.

---

## How it works
Prompt → Intent → Model Selection → Pipeline Construction → Prediction → Explanation

---

## Agent Design
- **Intent extraction**: The agent maps prompt text into structured signals (`complexity`, `pattern`).
- **Decision logic**:  
  - Simple queries → `NaiveForecaster`  
  - Trend/seasonal signals → `ExponentialSmoothing`
- **Reasoning system**: Each decision is accompanied by an explanation and alternative candidates.
- **Confidence scoring**: Deterministic confidence values reflect decision certainty.

---

## Example

**Input:**  
Forecast airline passengers using simple method  

**Output:**
- intent: `{"complexity": "simple", "pattern": "none"}`
- selected model: `NaiveForecaster`
- reasoning: Selected a baseline forecaster because the request does not indicate trend, seasonality, or advanced modeling requirements.
- confidence: `0.9`
- prediction: `[100, 110, 120]`

---

## Why this matters
Agentic systems must make decisions that are:
- explainable
- reproducible
- structurally valid

This prototype demonstrates how such systems can move from prompt-driven ambiguity to structured pipeline construction with explicit reasoning.

---

## Connection to sktime + MCP
This project mirrors MCP tool concepts such as:
- estimator discovery
- estimator description
- pipeline validation
- pipeline execution

The implementation intentionally simulates these interactions to demonstrate MCP-style agent behavior without external dependencies.

---

## How to run
```bash
python run_demo.py
```
- Or open demo.ipynb for a step-by-step walkthrough.
---

## Limitations
- Simulation only (no real MCP backend)
- Limited model space (small predefined set)

---

## Future Work
- Integrate real MCP tool calls
- Add LLM-based reasoning layer
- Expand estimator selection and validation logic
