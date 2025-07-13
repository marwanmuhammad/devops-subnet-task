# Subnet Analyzer Project 🔍

<h3> A DevOps pipeline for subnet analysis with integrated security scanning (SAST, secrets detection, container scanning).</h3>

## 🛠️ Used Tools
<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" width="100" height="100"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" title="Docker" width="100" height="100"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" title="Jenkins" width="100" height="100"/>
  <img src="https://github.com/user-attachments/assets/d2c97615-d9a4-4a23-9b17-7f3174658bef" title="Gitleaks" width="200" height="200" style="display: inline-block;"/>
  <img src="https://github.com/user-attachments/assets/0a6bb8e7-c3d9-4c4f-a4a2-9457df3bf688" title="Trivy" width="120" height="120" style="display: inline-block;"/>
  <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/9a13ab00-db45-41de-b812-3298bc7fdf73" />
  <img src="https://github.com/user-attachments/assets/f654c0fb-0a37-4a8a-bbda-678770c2c810" width="130" alt="Tool Icon"/>
  
</p>

## 📂 Project Structure
```bash
.
├── devsecops
│   ├── run_devsecops_checks.sh  # Security scan automation
│   └── Security Reports         # Generated security Scans
│       ├── bandit_report.html
│       ├── gitleaks_report.json
│       ├── pip_audit_report.json
│       ├── safety_report.txt
│       └── trivy_report.json
├── Dockerfile                   # Container configuration
├── ip_data.xlsx
├── Jenkinsfile                  # pipeline Script      
├── network_plot.png             # Viaulize Output file
├── requirments.txt              # needed requirments
├── subnet_analyzer.py           # Python script
├── subnet_report.csv            # Output File
└── visualize.py                 # Python script
```
## Project Architecture
<img width="1507" height="763" alt="Subnet Analyzer Architecture" src="https://github.com/user-attachments/assets/347d1e38-971e-4268-b094-6145a68dbffb" />

## 🚀 Quick Start
```bash
# 1. Clone repo
git clone https://github.com/marwanmuhammad/devops-subnet-task.git
cd devops-subnet-task

# 2. Install dependencies
sudo apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
sudo apt-get update && sudo apt-get install -y python3-dev python3-tk
pip install pandas matplotlib openpyxl bandit pip-audit safety

# 3. Run analysis
python subnet_analyzer.py       # Generates subnet_report.csv
python visualize.py            # Creates network_plot.png
```
## 🐳 Docker Run
```bash
# Build image
docker build -t subnet-analyzer .

# Run container (mounts current directory for reports)
docker run -v $(pwd):/app subnet-analyzer
docker run -v $(pwd):/app subnet-analyzer python visualize.py
```
## 🔒 Security Scans
```bash
# To run all checks:
chmod +x devsecops/run_devsecops_checks.sh
./devsecops/run_devsecops_checks.sh

#Reports will be saved in: devsecops/Security Reports/
```
## ⚙️ Jenkins Pipeline
The Jenkinsfile includes these stages:
    1.Clone the repo
    
    2.Build Docker Image
    
    3.Security Scans:

        Secrets Detection (Gitleaks)

        Python SAST (Bandit)

        Dependency Audit (pip-audit/safety)

        Container Scan (Trivy)

    4.Execution & Visualization:
<img width="1057" height="198" alt="image" src="https://github.com/user-attachments/assets/722f9ddb-e7d4-477d-8e0e-e512c3cfb13f" />

    5. Generating Security Reports
<img width="427" height="264" alt="image" src="https://github.com/user-attachments/assets/1a27ace1-c434-4a63-8d80-febc0d8ab00a" />









