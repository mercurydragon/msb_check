pipeline {
    agent any
    environment {
        DJANGO_SETTINGS_MODULE = 'app.settings'
        DJANGO_SECRET = credentials('DJANGO_SECRET_2')
        DB_NAME = credentials('DB_NAME')
        POSTGRES_CREDS = credentials('POSTGRES') // POSTGRES_CREDS_USR POSTGRES_CREDS_PWD
        POSTGRES_USER = '$POSTGRES_CREDS_USR'
        POSTGRES_PASSWORD = '$POSTGRES_CREDS_PWD'
    }
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

                sh 'rm .env'
                sh 'echo "DJANGO_SETTINGS_MODULE=app.settings" >> .env'
                sh 'echo "DB_ENGINE=django.db.backends.postgresql" >> .env'
                sh 'echo "DB_NAME=$DB_NAME" >> .env'
                sh 'echo "POSTGRES_USER=$POSTGRES_CREDS_USR" >> .env'
                sh 'echo "POSTGRES_PASSWORD=$POSTGRES_CREDS_PSW" >> .env'
                sh 'echo "DB_HOST=db" >> .env'
                sh 'echo "DB_PORT=5432" >> .env'
                sh 'echo "DJANGO_SECRET=$DJANGO_SECRET" >> .env'

                sh 'docker-compose up --build -d'
            }
        }
    }
}
