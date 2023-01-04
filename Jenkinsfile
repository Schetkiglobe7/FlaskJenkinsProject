node {
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "sudo docker build -t flask-app ."
   }
   stage("run docker container"){
        sh "sudo docker run -p 8085:8085 --name flask-app -d flask-app "
    }
}