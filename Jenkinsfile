pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        withPythonEnv('python3') {
            sh 'pip install pytest'
            sh 'pytest mytest.py'
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

