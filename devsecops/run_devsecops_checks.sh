#!/bin/bash

echo "Running Bandit (Python static analysis)..."
bandit ../subnet_analyzer.py ../visualize.py -r

echo ""
echo "Running pip-audit (dependency CVEs)..."
pip-audit

echo ""
echo "Running Safety (library CVEs)..."
safety check --full-report

echo ""
echo "Running Trivy (Docker image scan)..."
docker build -t subnet-analyzer ..
trivy image subnet-analyzer

echo ""
echo "Running Gitleaks (secrets scan)..."
gitleaks detect --source .. --no-banner

echo ""
echo "DevSecOps checks completed."
