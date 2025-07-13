pipeline {
  agent any

  environment {
    GITLEAKS_VERSION = '8.27.2'
    DOCKER_IMAGE = 'subnet-analyzer'
    VENV_PATH = '/myenv'
  }

  stages {
    stage('Clone Project') {
      steps {
        git(
          url: 'https://github.com/marwanmuhammad/devops-subnet-task.git',
          branch: 'master',
          credentialsId: 'github-cred'
        )
      }
    }

    /* ===== BUILD STAGE MUST COME FIRST ===== */
    stage('Build Docker Image') {
      steps {
        sh '''
          echo "=== BUILDING DOCKER IMAGE ==="
          docker build -t ${DOCKER_IMAGE} .
        '''
      }
    }

    /* ===== SECURITY STAGES ===== */
    stage('1. Secrets Detection') {
      steps {
        sh '''#!/bin/bash
          echo "=== RUNNING GITLEAKS SECRETS SCAN ==="
          gitleaks detect \
            --source . \
            --no-banner \
            --report-format json \
            --report-path gitleaks_report.json
        '''
        archiveArtifacts artifacts: 'gitleaks_report.json'
      }
    }

    stage('2. Python SAST (Bandit)') {
      steps {
        sh '''#!/bin/bash
          echo "=== RUNNING BANDIT STATIC ANALYSIS ==="
          . "${VENV_PATH}/bin/activate"
          bandit -r . -f html -o bandit_report.html
        '''
        archiveArtifacts artifacts: 'bandit_report.html'
      }
    }

    stage('3. Dependency Checks') {
      steps {
        sh '''#!/bin/bash
          echo "=== RUNNING DEPENDENCY CHECKS ==="
          . "${VENV_PATH}/bin/activate"
          pip-audit --format json -o pip_audit_report.json || true
          safety check --full-report > safety_report.txt || true
        '''
        archiveArtifacts artifacts: 'pip_audit_report.json,safety_report.txt'
      }
    }

    stage('4. Container Scan (Trivy)') {
      steps {
        sh '''#!/bin/bash
          echo "=== RUNNING TRIVY CONTAINER SCAN ==="
          trivy image --format json --output trivy_report.json ${DOCKER_IMAGE}
        '''
        archiveArtifacts artifacts: 'trivy_report.json'
      }
    }

    /* ===== ANALYSIS STAGES ===== */
    stage('Run Subnet Analyzer') {
      steps {
        sh '''#!/bin/bash
          echo "=== RUNNING SUBNET ANALYZER ==="
          . "${VENV_PATH}/bin/activate"
          python subnet_analyzer.py  // Runs with default paths
        '''
        archiveArtifacts artifacts: 'subnet_report.csv'
      }
    }

    stage('Run Visualizer') {
      steps {
        sh '''#!/bin/bash
          echo "=== RUNNING VISUALIZATION ==="
          . "${VENV_PATH}/bin/activate"
          python visualize.py  // Automatically finds subnet_report.csv
        '''
        archiveArtifacts artifacts: 'network_plot.png'
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: '*.csv,*.png,*.html,*.json,*.txt'
      cleanWs()
    }
  }
}
