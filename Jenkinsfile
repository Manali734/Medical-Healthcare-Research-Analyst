
pipeline {
    agent any

    stages {

        stage('1. Checkout Code') {
            steps {
                checkout scm
                bat 'git status'
            }
        }

        stage('2. Python Validation') {
            steps {
                bat 'python --version'
                bat 'python -m compileall app'
            }
        }

        stage('3. Build Docker Image') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('4. Deploy Application') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('5. Verify Deployment') {
            steps {
                bat 'docker compose ps'
            }
        }
    }

    post {
        success {
            echo 'Medical Healthcare application pipeline completed!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
