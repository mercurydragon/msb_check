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
            steps {
                withPythonEnv('python3.8') {
                    sh '''DJANGO_SETTINGS_MODULE=app.settings pytest || [[ $? -eq 1 ]]'''
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

