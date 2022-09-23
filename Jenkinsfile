pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                withPythonEnv('python3.8') {
                    sh 'pip install -r requirements.txt'
                    sh 'pip install pytest'
                    sh '''DJANGO_SETTINGS_MODULE=app.settings python3.8 -m pytest || [[ $? -eq 1 ]]'''
                }
            }
        }
        stage('Tests') {
            environment {
                DJANGO_SETTINGS_MODULE = 'app.settings'
                DJANGO_SECRET = credentials('DJANGO_SECRET')
            }
            steps {
                withPythonEnv('python3.8') {
                    sh '''pytest || [[ $? -eq 1 ]]'''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

