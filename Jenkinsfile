pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            sh '''
                python -m pip install --upgrade pip
                pip install flake8 pytest
                ip install -r requirements.txt
            '''
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

