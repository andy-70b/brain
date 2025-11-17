FROM python:3.11-slim
WORKDIR /workspace
COPY src ./src
COPY data/fixtures ./data/fixtures
COPY artifacts/registry.json ./artifacts/registry.json
ENV PYTHONPATH=/workspace/src PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
USER 65532:65532
ENTRYPOINT ["python", "-m", "andy"]
CMD ["replay", "--prompt", "Identify yourself."]
