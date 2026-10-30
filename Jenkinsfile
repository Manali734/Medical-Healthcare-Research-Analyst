
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
                bat '"C:\\Users\\Manali\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
                bat '"C:\\Users\\Manali\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m compileall app'
            }
        }


        stage('3. Build Docker Image') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('4. Deploy Application') {
            steps {
            withCredentials([
            string(
                credentialsId: 'groq-api-key',
                variable: 'GROQ_API_KEY'
            )
        ]) {
            bat '''
                @echo off
                > .env echo GROQ_MODEL=openai/gpt-oss-120b
                >> .env echo GROQ_API_KEY=%GROQ_API_KEY%

                docker compose up -d
            '''
        }
    }
}

        stage('5. Verify Deployment') {
            steps {
            bat 'docker compose ps'
            bat 'docker ps'
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
        always {
        bat '@if exist .env del /q .env'
        }
    }
}
