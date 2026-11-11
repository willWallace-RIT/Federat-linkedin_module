import queue
import threading
import time
from src.analyzer import CandidateAnalyzer

class FederatedDispatchEngine:
    def __init__(self, effectiveness_threshold=0.65):
        self.queue = queue.Queue()
        self.threshold = effectiveness_threshold
        self.lock = threading.Lock()

    def receive_job_event(self, job_posting, registered_users):
        print(f"[EVENT] New Job Detected: {job_posting['title']} at {job_posting['company_id']}")
        for user in registered_users:
            analyzer = CandidateAnalyzer(user)
            score = analyzer.calculate_effectiveness(job_posting)
            if score >= self.threshold:
                item = {
                    'timestamp': time.time(),
                    'user_id': user['id'],
                    'job_id': job_posting['id'],
                    'score': score
                }
                self.queue.put(item)

    def process_queue(self):
        while not self.queue.empty():
            app = self.queue.get()
            with self.lock:
                self.submit_application(app)
            self.queue.task_done()

    def submit_application(self, application):
        print(f"[FCFS DISPATCH] Applied User '{application['user_id']}' -> Job '{application['job_id']}' | Score: {application['score']:.2f} | Time: {application['timestamp']}")
