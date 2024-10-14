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
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                python3 --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'  // Установка зависимостей
            }
        }
    }
}

