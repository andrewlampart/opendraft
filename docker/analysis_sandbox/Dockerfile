# Obraz do uruchamiania wygenerowanego skryptu analizy (pandas / numpy / scipy).
# Budowa (z katalogu repo): docker build -t opendraft-analysis-sandbox:latest -f opendraft/docker/analysis_sandbox/Dockerfile .
#
# Kontener działa jako UID/GID 1000 (non-root). Katalog joba na hoście musi pozwalać
# temu UID na zapis (np. worker Celery z uid 1000) albo ustaw OPENDRAFT_SANDBOX_CONTAINER_USER.
FROM python:3.11-slim-bookworm

RUN pip install --no-cache-dir \
    "pandas>=2.0.0,<3" \
    "numpy>=1.26.0,<3" \
    "scipy>=1.11.0,<2" \
    "matplotlib>=3.8.0,<4" \
    "openpyxl>=3.1.0,<4"

RUN groupadd --gid 1000 sandbox \
    && useradd --uid 1000 --gid sandbox --no-log-init --shell /usr/sbin/nologin --create-home sandbox \
    && mkdir -p /work \
    && chown sandbox:sandbox /work

USER sandbox
WORKDIR /work
