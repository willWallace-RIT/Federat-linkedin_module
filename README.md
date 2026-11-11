# Federated FCFS LinkedIn Job Application Engine

An algorithmic framework for quantifying LinkedIn candidate job fit and dispatching applications via a federated First-Come, First-Served (FCFS) queue engine.

## Project Structure
- `src/analyzer.py`: Candidate effectiveness score computation model ($E(u, j)$).
- `src/engine.py`: Distributed event-driven FCFS dispatch queue.
- `src/main.py`: Simulation runner demonstrating job detection and auto-dispatching.
- `tests/test_analyzer.py`: Unit tests for scoring logic.
- `requirements.txt`: Dependencies.

## Quick Start
```bash
pip install -r requirements.txt
python src/main.py
```
