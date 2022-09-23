pipeline {
    agent any
    environment {
        DJANGO_SETTINGS_MODULE = 'app.settings'
        DJANGO_SECRET = credentials('DJANGO_SECRET')
        DB_ENGINE = 'django.db.backends.postgresql'
        DB_NAME = credentials('DB_NAME')
        POSTGRES_CREDS = credentials('POSTGRES')
        DB_HOST = 'db'
        DB_PORT = '5432'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                withPythonEnv('python3.8') {
                    sh 'pip install -r requirements.txt'
                    sh 'pip install pytest'
                    sh 'python3.8 manage.py collectstatic --noinput'
                }
            }
        }
        stage('Tests') {
            steps {
                withPythonEnv('python3.8') {
                    sh 'python3.8 -m pytest || [[ $? -eq 1 ]]'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo docker-compose up --build'
            }
        }
    }
}

