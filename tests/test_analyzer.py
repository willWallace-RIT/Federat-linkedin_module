import unittest
import numpy as np
from src.analyzer import CandidateAnalyzer, cosine_similarity

class TestCandidateAnalyzer(unittest.TestCase):
    def test_cosine_similarity(self):
        v1 = np.array([1.0, 0.0])
        v2 = np.array([1.0, 0.0])
        self.assertAlmostEqual(cosine_similarity(v1, v2), 1.0)

    def test_effectiveness_bounds(self):
        user = {
            'id': 'test_user',
            'embedding': np.array([0.5, 0.5]),
            'network_map': {'comp_x': 2},
            'historical_inbound_rate': 0.2
        }
        job = {
            'id': 'test_job',
            'company_id': 'comp_x',
            'title': 'Engineer',
            'embedding': np.array([0.5, 0.5]),
            'timestamp': 0
        }
        analyzer = CandidateAnalyzer(user)
        score = analyzer.calculate_effectiveness(job)
        self.assertTrue(0.0 <= score <= 1.0)

if __name__ == '__main__':
    unittest.main()
