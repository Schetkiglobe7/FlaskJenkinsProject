node {
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "docker build -t flask-app ."
   }
   stage("Run docker container"){
        sh "docker run -p 8085:8085 --name flask-app -d flask-app "
    }
}