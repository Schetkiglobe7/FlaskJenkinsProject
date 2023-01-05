pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerHub')
	}
    stages {
        stage('Build') {
            agent any
            steps {
                sh '''
                docker stop python-docker
                docker rm python-docker
                '''
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
                sh 'docker build --tag schetkiglobe7/python-docker:latest .'
            }
        }

        stage('Run') {
            agent any
            steps {
                //sh 'docker run -p 8085:5000 --name python-docker -d python-docker:latest'
                sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push schetkiglobe7/python-docker:latest
                '''
            }
        }
    }
}