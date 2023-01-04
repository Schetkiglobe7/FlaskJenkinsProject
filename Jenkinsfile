pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Deploy') {
            agent{
                docker{
                    image 'python2-alpine'
                }
            }
            steps {
                sh 'run -p 8085:8085 --name flask-app -d flask-app'
            }
        }
    }
}