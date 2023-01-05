pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerHub')
	}
    stages {
        /*
        stage('Build') {
            agent any
            steps {
                sh '''
                docker stop python-docker
                docker rm python-docker
                '''
            }
        }
        */

        stage('Test') {
           
            steps {
                sh 'py.test --junit-xml test-reports/results.xml src/tests/test_main.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Deliver') {
            steps {
                sh 'docker build --tag schetkiglobe7/python-docker:latest .'
            }
        }

        stage('Run') {
            steps {
                /*sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push schetkiglobe7/python-docker:latest
                '''*/
                sh 'docker run -p 8088:8085 --name Pirates -d schetkiglobe7/python-docker:latest'
            }
        }
    }
}