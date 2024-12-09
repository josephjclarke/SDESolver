from typing import List
import numpy as np


class SamplePath:
    def __init__(self, x: np.ndarray, t: np.ndarray) -> None:
        self.x = x
        self.t = t


class Solution:
    def __init__(self, samples: List[SamplePath]) -> None:
        self.samples = samples
        self.path_count = len(self.samples)

    def __iter__(self):
        for sample in self.samples:
            yield sample
