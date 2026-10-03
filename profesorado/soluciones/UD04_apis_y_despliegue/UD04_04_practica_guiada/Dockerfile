FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY . .
RUN uv sync
CMD ["uv", "run", "uvicorn", "main_basic:app", "--host", "0.0.0.0", "--port", "8000"]
