# AgenticOps Reference Architecture
### Continuous Evaluation, Regression Detection, Distributed Tracing and Error-Budget-Based Release Governance for Production Agents

**PES University | M.Tech Capstone Project | Group 10 | 2026**

**Project Status:** Initial Prototype Completed | Continuous Evaluation Implementation in Progress

---

## 1. Project Overview

AgenticOps is a research-oriented reference architecture designed to improve the reliability, observability and release governance of production agent-based systems.

The primary objective is to establish a **continuous evaluation and regression detection framework** that monitors agent performance throughout the software development lifecycle, detects behavioral and performance degradation, and prevents unreliable agent versions from being released.

The proposed framework combines:

- Continuous evaluation and automated regression detection
- Agent workflow orchestration using LangGraph
- Execution tracing and observability using OpenTelemetry
- Baseline-versus-candidate performance comparison
- Automated release gates integrated with CI pipelines
- Error-budget-based release governance
- Longitudinal performance monitoring and analysis

The project follows an evaluation-driven development approach in which agent changes are assessed against predefined quality and reliability criteria.

## 2. Problem Statement

Agent-based applications introduce operational challenges because their workflows may involve multiple execution steps, dynamic decision-making and external dependencies.

Changes to workflow logic, models, prompts or dependencies can introduce regressions that may not be immediately visible through conventional software monitoring.

Traditional observability tools primarily capture execution behavior, latency and system errors. However, execution success does not necessarily imply that an agent has produced a correct or acceptable result.

A comprehensive reliability framework therefore needs to combine execution observability with continuous quality evaluation and automated release controls.

### Research Problem

How can continuous evaluation, distributed tracing and error-budget-based release governance be integrated into a reference architecture to detect, diagnose and contain regressions in production agent workflows?

## 3. Research Objectives

The project aims to:

1. Design a reference architecture for continuous evaluation and regression detection in agent-based systems.
2. Implement structured workflow execution using LangGraph.
3. Instrument agent workflows using OpenTelemetry to capture execution traces and latency.
4. Develop an automated evaluation framework that continuously compares candidate performance against established baselines.
5. Integrate evaluation gates into CI pipelines to prevent the release of regressed agent versions.
6. Investigate error budgets and reliability thresholds for release governance.
7. Evaluate observability tools for their ability to capture and represent agent execution traces.
8. Conduct comparative and longitudinal experiments to assess regression detection effectiveness and operational reliability.

## 4. Proposed System Architecture

The architecture is organized into six layers.

### 4.1 Agent Execution Layer

LangGraph is used to define and execute agent workflows as connected nodes with shared state.

### 4.2 Observability Layer

OpenTelemetry is used to instrument workflow execution and collect:

- Trace identifiers
- Parent-child span relationships
- Execution durations
- Workflow attributes
- Error information, where instrumented

### 4.3 Continuous Evaluation Layer

The evaluation framework is intended to execute predefined test cases automatically and assess candidate agent versions using measurable performance criteria.

Evaluation metrics may include:

- Task accuracy
- Failure rate
- Execution latency
- Regression magnitude
- Reliability across repeated executions

### 4.4 Regression Detection Layer

Candidate results are compared against baseline performance and predefined acceptance thresholds.

Regressions are identified when candidate performance violates the established evaluation criteria.

### 4.5 Release Governance Layer

A release gate determines whether a candidate version satisfies the required reliability thresholds.

- **PASS:** Candidate satisfies the configured evaluation criteria.
- **BLOCK:** Candidate violates one or more release criteria.

Future work will extend these decisions using error-budget policies and automated CI enforcement.

### 4.6 Monitoring and Analysis Layer

Planned dashboard integration will support trace inspection, regression investigation, performance comparisons and longitudinal analysis.

### Proposed Continuous Evaluation Pipeline

```text
Code Change / Pull Request
           |
           v
Continuous Integration Pipeline
           |
           v
LangGraph Agent Execution
           |
           v
OpenTelemetry Instrumentation
           |
           v
Automated Evaluation
           |
           v
Baseline vs Candidate Comparison
           |
           v
Regression Detection
           |
           v
Release Governance Gate
           |
      +----+----+
      |         |
     PASS      BLOCK
      |         |
      v         v
Release      Investigation
Eligible     and Correction
```

This represents the target architecture. Full CI automation and production monitoring have not yet been implemented.

## 5. Technology Stack

| Technology | Purpose | Status |
|---|---|---|
| Python | Prototype development and evaluation | Implemented |
| LangGraph | Workflow orchestration | Implemented |
| OpenTelemetry | Execution tracing | Basic instrumentation implemented |
| Pandas | Experimental results analysis | Used |
| Google Colab | Development and experimentation | Used |
| GitHub | Version control and collaboration | In use |
| GitHub Actions | Automated continuous evaluation | Planned |
| Arize Phoenix / Langfuse | Trace visualization and analysis | Planned |
| Error-budget policies | Reliability-based release governance | Planned |

## 6. Current Implementation

The initial proof of concept demonstrates the core components required for a continuous regression detection framework.

### Completed Components

- LangGraph workflow with classification and response nodes
- Baseline evaluation framework
- Ten predefined test cases
- Candidate-versus-baseline comparison
- Deliberately introduced regression scenario
- Threshold-based release decision
- OpenTelemetry parent-child span instrumentation
- Execution timing measurements
- Experimental result exports

### Implementation Scope

The current prototype uses a deterministic, rule-based workflow.

It demonstrates the feasibility of regression detection and tracing but does not yet implement continuous automated execution, production deployment or long-term monitoring.

## 7. Experimental Evaluation

### Experiment 1: Baseline Performance Evaluation

The initial workflow was evaluated using ten predefined test cases.

| Metric | Result |
|---|---:|
| Total test cases | 10 |
| Correct classifications | 10 |
| Accuracy | 100% |
| Failure rate | 0% |
| Mean latency | 7.57 ms |
| Release gate | PASS |

These results establish the baseline for the initial controlled test suite.

### Experiment 2: Regression Detection Validation

A deliberately faulty candidate was introduced to validate whether the evaluation mechanism could detect a performance regression.

The modified workflow incorrectly classified three refund-related requests.

| Metric | Baseline | Candidate |
|---|---:|---:|
| Test cases | 10 | 10 |
| Correct classifications | 10 | 7 |
| Accuracy | 100% | 70% |
| Accuracy degradation | — | 30 percentage points |

**Release Decision: BLOCKED**

The experiment demonstrates that the evaluation mechanism can detect the introduced regression and reject a candidate that violates its configured acceptance criteria.

This is an initial validation of the detection mechanism intended for future continuous execution.

### Experiment 3: OpenTelemetry Execution Tracing

The LangGraph workflow was instrumented using OpenTelemetry.

The verified execution captured three spans:

| Span | Relationship |
|---|---|
| `agent_execution` | Parent span |
| `classify_task` | Child span |
| `generate_response` | Child span |

The measured parent execution duration was approximately **2.41 milliseconds** in the instrumented run.

The captured spans demonstrate basic execution visibility and parent-child relationships.

A persistent observability backend, dashboard integration and comparative trace analysis remain planned extensions.

## 8. Continuous Evaluation Strategy

The proposed continuous evaluation framework will execute regression tests automatically when relevant changes are introduced.

### Planned CI Triggers

- Code pushes to designated branches
- Pull request creation or updates
- Scheduled evaluation runs, where appropriate
- Manual evaluation execution

### Planned Evaluation Workflow

1. Retrieve the current baseline and candidate implementation.
2. Execute the evaluation dataset.
3. Collect task accuracy, failure rate and latency metrics.
4. Capture workflow execution traces.
5. Compare candidate results against baseline thresholds.
6. Identify significant performance regressions.
7. Generate an evaluation report.
8. Approve or block the candidate based on configured release policies.

### Expected Benefits

- Earlier detection of workflow regressions
- Consistent evaluation across code changes
- Improved traceability of release decisions
- Reduced dependence on manual regression testing
- Reproducible performance comparisons

The continuous evaluation pipeline will be implemented and validated in subsequent development phases.

## 9. Error-Budget-Based Release Governance

The project proposes incorporating error budgets into release decisions.

An error budget represents the amount of unreliability permitted within a defined measurement window.

Future experiments will investigate policies such as:

- Maximum acceptable failure rate
- Minimum task success rate
- Permitted regression thresholds
- Latency limits
- Release restrictions when reliability budgets are exhausted

The relationship between evaluation results, observed reliability and release decisions will be examined experimentally.

Error-budget enforcement is currently a planned component rather than a completed implementation.

## 10. Research Methodology

The project follows a design-and-evaluation research approach.

### Phase 1: Reference Architecture and Prototype

- Define the research problem and system requirements.
- Develop an initial LangGraph workflow.
- Implement baseline evaluation.
- Introduce a controlled regression.
- Validate release gate behavior.
- Instrument workflow execution using OpenTelemetry.

**Status:** Initial proof of concept completed.

### Phase 2: Continuous Evaluation Implementation

- Develop reusable evaluation scripts.
- Integrate GitHub Actions.
- Automate baseline-versus-candidate comparisons.
- Generate evaluation reports.
- Establish repeatable CI release gates.

**Status:** Planned.

### Phase 3: Observability and Reliability Extension

- Integrate a trace visualization platform.
- Extend workflow complexity.
- Investigate error-budget policies.
- Implement additional reliability metrics.
- Assess trace completeness and diagnostic usefulness.

**Status:** Planned.

### Phase 4: Comparative and Longitudinal Evaluation

- Evaluate two representative agent workflows.
- Conduct repeated experiments over an extended observation period.
- Introduce controlled changes and regression scenarios.
- Compare regression detection performance.
- Assess observability tool capabilities.
- Analyze reliability trends and limitations.

**Status:** Planned.

## 11. Repository Structure

```text
capstone_group10/
├── .github/
│   └── workflows/
├── notebooks/
│   └── [Prototype notebooks]
├── results/
│   ├── agenticops_baseline_results.csv
│   └── agenticops_regression_comparison.csv
├── screenshots/
│   └── [Experimental evidence]
├── presentation/
│   └── [Progress review slides]
├── docs/
│   └── [Research documentation]
├── README.md
└── requirements.txt
```

The structure represents the intended organization of the repository. File names and contents may evolve as the project progresses.

## 12. Running the Initial Prototype

### Prerequisites

- Python 3.10 or later, subject to dependency compatibility
- Google Colab or a compatible Python environment
- Required Python libraries

### Installation

```bash
pip install langgraph pandas matplotlib opentelemetry-api opentelemetry-sdk
```

### Execution

1. Open the notebook from the `notebooks/` directory.
2. Run the notebook cells sequentially.
3. Execute the baseline evaluation.
4. Execute the candidate regression experiment.
5. Review the baseline-versus-candidate results.
6. Inspect the release gate decision.
7. Execute the OpenTelemetry instrumentation cells.
8. Review the captured spans and execution timing.

The current notebook supports manual execution. Automated continuous execution will be added through the planned CI implementation.

## 13. Evaluation Metrics

The research will investigate the following metrics.

| Metric | Purpose |
|---|---|
| Task accuracy | Measures correctness against expected outputs |
| Failure rate | Measures unsuccessful executions |
| Execution latency | Measures workflow execution time |
| Regression magnitude | Quantifies performance degradation |
| Regression detection rate | Measures the proportion of introduced regressions detected |
| False positive rate | Measures incorrect regression alerts |
| Trace completeness | Measures visibility into relevant execution steps |
| Release gate effectiveness | Evaluates release decision accuracy |
| Error-budget consumption | Tracks reliability against permitted limits |

Not all metrics are implemented in the initial prototype.

## 14. Expected Research Contributions

The proposed research aims to contribute:

1. A reference architecture for continuous evaluation and regression detection in agent workflows.
2. A reproducible approach for combining workflow tracing and quality evaluation.
3. Automated regression detection integrated with CI release governance.
4. An investigation of error-budget policies for agent reliability.
5. Comparative evidence on agent observability capabilities.
6. Longitudinal experimental findings on regression detection and reliability.

These are expected contributions that require further implementation, evaluation and comparison with existing research.

## 15. Current Limitations

The initial implementation has the following limitations:

- Evaluation is based on ten predefined test cases.
- The workflow uses deterministic classification
