import time
import numpy as np

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

class CandidateAnalyzer:
    def __init__(self, user_profile):
        self.user = user_profile

    def calculate_effectiveness(self, job_posting):
        s_prof = cosine_similarity(self.user['embedding'], job_posting['embedding'])
        company_id = job_posting['company_id']
        connections_in_company = self.user['network_map'].get(company_id, 0)
        s_net = 1.0 - np.exp(-0.5 * connections_in_company)
        s_eng = self.user.get('historical_inbound_rate', 0.1)
        hours_old = (time.time() - job_posting['timestamp']) / 3600.0
        decay = 0.05 * hours_old
        weights = [0.5, 0.3, 0.2]
        score = (weights[0] * s_prof + weights[1] * s_net + weights[2] * s_eng) - decay
        return max(0.0, min(1.0, score))
