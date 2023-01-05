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

        stage('Test') {
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
        }

        stage('Deliver') {
            agent any
            steps {
                sh 'docker build --tag python-docker:latest .'
            }
        }

        stage('Run') {
            agent any
            steps {
                sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push schetkiglobe7/python-docker:latest
                '''
            }
        }
    }
}