      pipeline {
        agent {
            docker { image 'python:3.8' }
        }
        stages {
            stage('Install Requirements') {
                steps {
                    sh '''
                        python -m pip install --upgrade pip
                        pip install flake8 pytest
                        ip install -r requirements.txt
                    '''
                    sh 'flake8 . --exclude tests'
                    sh 'pytest'
                }
            }
            stage('Deploy') {
                steps {
                    sh 'echo not yet...'
                }
            }
        }
    }
