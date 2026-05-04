#!/usr/bin/env bash
set -e

# Change to the env directory
cd "$(dirname "$0")"

echo "[*] Building and starting the vulnerable Docker container..."
docker-compose up -d --build

echo "[*] Waiting for the container to be ready..."
sleep 3

echo "[*] Running the exploit..."
# Test command
python3 exploit.py -u http://localhost:8080/index.php -c "id; uname -a; pwd"

echo "[*] Done. You can bring down the environment with: docker-compose down"
