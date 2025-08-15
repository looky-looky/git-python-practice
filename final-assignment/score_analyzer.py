import numpy as np

class ScoreAnalyzer:
    def __init__(self, score_data: np.ndarray):
        self.scores = score_data

    def calculate_student_averages(self) -> np.ndarray:
        return np.mean(self.scores, axis=1)

    def calculate_subject_averages(self) -> np.ndarray:
        return np.mean(self.scores, axis=0)

    def get_top_student_index(self) -> int:
        student_totals = np.sum(self.scores, axis=1)
        return np.argmax(student_totals)