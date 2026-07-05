# Feature Engineering Agent Architecture

ML feature engineering agent that designs, computes, and serves features for machine learning models, managing feature stores, point-in-time correctness, feature drift detection, and real-time feature serving.

## Domain Tools

- **design_features**: Design feature set for a ML use case with transformations
- **compute_features**: Compute features from raw data with point-in-time correctness
- **register_feature**: Register a feature in the feature store with metadata
- **serve_features**: Serve features for real-time model inference
- **detect_drift**: Detect feature distribution drift between training and serving