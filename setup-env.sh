#!/bin/bash
# Izolowane środowisko OpenDraft na WSL - uruchom: bash setup-env.sh

set -e
cd "$(dirname "$0")"

echo "==> OpenDraft - konfiguracja środowiska"

# --- Python venv ---
if [ ! -d ".venv" ]; then
    echo "==> Tworzenie venv Python..."
    python3 -m venv .venv
fi

echo "==> Aktywowanie venv i instalacja zależności..."
source .venv/bin/activate

pip install --upgrade pip
pip install -e ./engine

# --- Node (opcjonalnie, jeśli potrzebny frontend) ---
if [ -d "npm" ] && command -v node &>/dev/null; then
    echo "==> Instalacja zależności Node..."
    (cd npm && npm install)
fi

echo ""
echo "==> Gotowe! Użycie:"
echo "    source .venv/bin/activate   # aktywuj venv"
echo "    opendraft --help            # lub draft-ai --help"
echo ""
echo "Dodaj do ~/.bashrc dla stałej aktywacji w tym katalogu:"
echo "    alias opendraft-env='source $(pwd)/.venv/bin/activate'"
echo ""
