from typing import Callable, Tuple
import numpy as np
import solution


class Integrator:
    def __init__(
        self,
        drift: Callable,
        diffusion: Callable,
        times: np.ndarray,
        x0: np.ndarray,
        drift_jac: Callable = None,
        diffusion_jac: Callable = None,
        args: Tuple = (),
        generator: np.random.Generator = None,
    ) -> None:
        self.drift_core = drift
        self.diffusion_core = diffusion
        self.times = times
        self.x0 = x0
        self.drift_jac = drift_jac
        self.diffusion_jac = diffusion_jac

        if generator is None:
            self.generator = np.random.default_rng()
        self.generator = generator

    def drift(self, t, x):
        return self.drift_core(t, x, *self.args)

    def diffusion(self, t, x):
        return self.diffusion_core(t, x, *self.args)

    def get_path(self) -> solution.SamplePath:
        pass

    def solve(self, number_of_paths: int = 1) -> solution.Solution:
        return solution.Solution([self.get_path() for i in range(number_of_paths)])
