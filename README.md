# Feature Engineering Agent

[![CI](https://github.com/kogunlowo123/feature-engineering-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/feature-engineering-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

ML feature engineering agent that designs, computes, and serves features for machine learning models, managing feature stores, point-in-time correctness, feature drift detection, and real-time feature serving.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_features` | Design feature set for a ML use case with transformations |
| `compute_features` | Compute features from raw data with point-in-time correctness |
| `register_feature` | Register a feature in the feature store with metadata |
| `serve_features` | Serve features for real-time model inference |
| `detect_drift` | Detect feature distribution drift between training and serving |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/features/design` | Design features |
| `POST` | `/api/v1/features/compute` | Compute features |
| `POST` | `/api/v1/features/register` | Register feature |
| `POST` | `/api/v1/features/serve` | Serve features |
| `POST` | `/api/v1/features/drift` | Detect drift |

## Features

- Feature Design
- Feature Computation
- Feature Serving
- Drift Detection
- Point In Time Joins

## Integrations

- Feast
- Tecton
- Hopsworks
- Sagemaker Feature Store
- Vertex Feature Store

## Architecture

```
feature-engineering-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── feature_engineering_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Feast + Tecton + Hopsworks + Feature Store**

---

Built as part of the Enterprise AI Agent Platform.
