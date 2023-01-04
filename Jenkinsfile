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

        /*stage('Test') {
            agent {
                docker{
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'py.test --junit-xml tests/test-reports/results.xml src/tests/test_main.py'
            }
            post {
                always {
                    junit 'tests/test-reports/results.xml'
                }
            }
        }*/

        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                sh 'docker build --tag python-docker:latest .'
            }
        }

        stage('Run') {
            agent any
            steps {
                sh 'docker run -p 8085:8085 --name python-docker -d python-docker:latest'
            }
        }
    }
}