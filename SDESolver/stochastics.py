import numpy as np


def dW(
    dt: float, generator: np.random.Generator, size: int = 1, steps: int = 1
) -> np.ndarray:
    return generator.normal(loc=0.0, scale=np.sqrt(dt), size=(size, steps))


def I(dWs: np.ndarray) -> float:
    size, steps = dWs.shape
