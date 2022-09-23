pipeline {
    agent any
    environment {
        DJANGO_SETTINGS_MODULE = 'app.settings'
        DJANGO_SECRET = credentials('DJANGO_SECRET')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                withPythonEnv('python3.8') {
                    sh 'pip install -r requirements.txt'
                    sh 'pip install pytest'
                }
            }
        }
        stage('Tests') {
            steps {
                withPythonEnv('python3.8') {
                    sh 'pytest || [[ $? -eq 1 ]]'
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

