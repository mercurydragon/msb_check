pipeline {
    agent any
    environment {
        DJANGO_SETTINGS_MODULE = 'app.settings'
        DJANGO_SECRET = credentials('DJANGO_SECRET')
        DB_ENGINE = 'django.db.backends.postgresql'
        DB_NAME = credentials('DB_NAME')
        POSTGRES_CREDS = credentials('POSTGRES')
        POSTGRES_USER = '$POSTGRES_CREDS_USR'
        POSTGRES_PASSWORD = '$POSTGRES_CREDS_PWD'
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
                sh 'rm .env'
                sh 'echo "DJANGO_SETTINGS_MODULE=app.settings" >> .env'
                sh 'echo "DB_ENGINE=django.db.backends.postgresql" >> .env'
                sh 'echo "DB_NAME=$DB_NAME" >> .env'
                sh 'echo "DJANGO_SECRET=$DJANGO_SECRET" >> .env'
                sh 'echo "POSTGRES_USER=$POSTGRES_CREDS_USR" >> .env'
                sh 'echo "POSTGRES_PASSWORD=$POSTGRES_CREDS_PSW" >> .env'
                sh 'echo "DB_HOST=db" >> .env'
                sh 'echo "DB_PORT=5432" >> .env'
                sh 'docker-compose up --build -d'
            }
        }
    }
}

