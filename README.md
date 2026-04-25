# sktime-agentic-forecaster

## Overview
sktime-agentic-forecaster is a minimal agentic forecasting prototype. It converts a natural-language query into a structured forecasting pipeline, executes a deterministic prediction, and explains the reasoning behind its decisions.

This demonstrates how agentic systems can perform transparent, auditable decision-making rather than relying on opaque or trial-and-error workflows.

This prototype focuses on the agent reasoning layer rather than model execution.
The design mirrors MCP workflows and can be extended to real sktime pipelines.

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

This project was built alongside contributions to sktime-mcp:
- [PR #212](https://github.com/sktime/sktime-mcp/pull/212) – Align documentation with `list_estimators(query=...)` MCP interface
- [PR #216](https://github.com/sktime/sktime-mcp/pull/216) – Fix pipeline validation to disallow forecaster→forecaster chains
- [PR #225](https://github.com/sktime/sktime-mcp/pull/225) – Replace hardcoded `/tmp` paths with cross-platform temp directory
- [PR #298](https://github.com/sktime/sktime-mcp/pull/298) – Update docs and examples to use `list_estimators` instead of deprecated `search_estimators`

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
