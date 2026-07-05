"""Test configuration for Feature Engineering Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "feature-engineering-agent", "category": "Data Engineering"}
