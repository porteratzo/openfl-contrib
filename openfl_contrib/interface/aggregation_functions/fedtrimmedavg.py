# Copyright (C) 2020-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Federated averaging module."""

import numpy as np
from typing import List
from .interface import AggregationFunction


def _trim_mean(array: np.ndarray, proportiontocut: float) -> np.ndarray:
    assert (proportiontocut < 0.5) & (
        proportiontocut > 0.0
    ), "proportiontocut should be between 0 and 0.5, expects axis 0 to be collaborators"
    axis = 0
    array_shape0 = array.shape[axis]
    lowercut = int(proportiontocut * array_shape0)
    uppercut = array_shape0 - lowercut

    partitioned_array = np.partition(array, (lowercut, uppercut - 1), axis)
    slice_list = [slice(None)] * partitioned_array.ndim
    slice_list[axis] = slice(lowercut, uppercut)
    result: np.ndarray = np.mean(partitioned_array[tuple(slice_list)], axis=axis)
    return result


def aggregate_trimmed_avg(
    weights: List[np.ndarray], proportiontocut: float
) -> List[np.ndarray]:
    """Compute trimmed average."""

    trimmed_w = [
        _trim_mean(np.stack(layer), proportiontocut=proportiontocut)
        for layer in zip(*weights)
    ]

    return trimmed_w


class TrimmedAverage(AggregationFunction):
    """Federated trimmed average aggregation.

    Paper: arxiv.org/abs/1803.01498
    """

    def __init__(self, beta: float = 0.2, **kwargs) -> None:
        super().__init__(**kwargs)
        self.beta = beta

    def __repr__(self) -> str:
        """Compute a string representation of the function."""
        rep = "Trimmed average Aggregation Function"
        return rep

    def aggregate_models(self, model_weights: List[np.ndarray]) -> List[np.ndarray]:
        """Compute fed avg across models. Expects list of weights of each collaborator"""
        return aggregate_trimmed_avg(model_weights, self.beta)

    def aggregate_metrics(self, metrics: List[np.ndarray]) -> np.ndarray:
        """Aggregate metrics like loss and accuracy"""
        return sum(metrics) / len(metrics)
