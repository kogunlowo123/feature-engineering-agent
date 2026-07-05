"""Feature Engineering Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_features():
    """Test Design feature set for a ML use case with transformations."""
    tools = AgentTools()
    result = await tools.design_features(use_case="test", raw_data_schema="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_compute_features():
    """Test Compute features from raw data with point-in-time correctness."""
    tools = AgentTools()
    result = await tools.compute_features(feature_definitions="test", data_source="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_register_feature():
    """Test Register a feature in the feature store with metadata."""
    tools = AgentTools()
    result = await tools.register_feature(name="test", entity="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_serve_features():
    """Test Serve features for real-time model inference."""
    tools = AgentTools()
    result = await tools.serve_features(entity_ids="test", feature_names="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.feature_engineering_agent_agent import FeatureEngineeringAgentAgent
    agent = FeatureEngineeringAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
