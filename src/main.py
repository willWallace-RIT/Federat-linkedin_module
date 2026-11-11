import time
import numpy as np
from src.engine import FederatedDispatchEngine

if __name__ == "__main__":
    print("Initializing Federated FCFS Job Dispatch Simulation...")
    mock_user = {
        'id': 'usr_90210',
        'embedding': np.array([0.12, 0.85, 0.43, 0.91]),
        'network_map': {'comp_a': 4, 'comp_b': 0},
        'historical_inbound_rate': 0.35
    }
    mock_job = {
        'id': 'job_8811',
        'company_id': 'comp_a',
        'title': 'Systems Software Architect',
        'embedding': np.array([0.10, 0.88, 0.40, 0.95]),
        'timestamp': time.time() - 300
    }
    engine = FederatedDispatchEngine(effectiveness_threshold=0.60)
    engine.receive_job_event(mock_job, [mock_user])
    engine.process_queue()
