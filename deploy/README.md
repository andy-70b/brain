# Offline review environment

Build and run with `docker compose -f deploy/compose.yaml up --build`. The container executes transcript replay and exits. Compose disables networking, drops capabilities, and mounts a read-only root filesystem.

The image does not contain model weights, a GPU runtime, or a service endpoint. An external inference worker requires a separate environment review. Never infer deployment isolation from application configuration alone.
