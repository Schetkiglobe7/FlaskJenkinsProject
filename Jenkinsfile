pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent any
            steps {
                sh 'echo "building the repo"'
            }
        }

        stage('Test') {
            agent any
            steps {
                sh 'echo "testing the repo"'
            }
            post {
                always {
                    sh 'echo "tracking the result of testing"'
                }
            }
        }

        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                sh 'echo "deliverying repo"'
            }
        }
    }
}