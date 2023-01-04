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
            agent {
                docker{
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml tests/test-reports/results.xml src/test_main.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
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