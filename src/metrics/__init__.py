# ruff: noqa: F401

# NOTE: Importing these metrics automatically adds them to the METRIC_REGISTRY
from .base import BaseMetric, BaseComparativeMetric

# Implemented Metrics
from .cka import CKA
from .norm import NormMetric
from .per import PERMetric

# Registry
from ._registry import METRIC_REGISTRY

# Typing
from src.config.learning_dynamics import BaseMetricConfig
from typing import Dict, Any


def get_metric(
    metric_config: BaseMetricConfig, training_config: Dict[str, Any]
) -> BaseMetric:
    """
    Loads a metric from the metrics directory.
    """
    return METRIC_REGISTRY[metric_config.metric_name](metric_config, training_config)
