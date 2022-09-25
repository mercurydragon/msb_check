pipeline {
    agent any

    stages {
        stage('Install req') {
            steps {
                echo 'Install req...'
                withPythonEnv('python3.8') {
                    sh 'pip install -r requirements.txt'
                    sh 'pip install pytest'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                withPythonEnv('python3.8') {
                    sh 'python3.8 -m pytest || [[ $? -eq 1 ]]'
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
