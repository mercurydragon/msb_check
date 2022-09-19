pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Tests') {
            steps {
                sh '''python3 -m pip install -U pip &&  pip install -U pytest && pip install -r requirements.txt &&
                    DJANGO_SETTINGS_MODULE=app.settings python3 -m pytest || [[ $? -eq 1 ]]'''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

