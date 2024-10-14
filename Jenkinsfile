# jenkins file for python
pipeline {
    agent { label 'ubuntu' }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm  // Проверка кода
            }
        }

        stage('Set Up Environment') {
            steps {
                bat '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                python3 --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip3 install -r requirements.txt'  // Установка зависимостей
            }
        }
    }
}

