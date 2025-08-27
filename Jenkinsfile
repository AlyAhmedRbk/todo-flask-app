pipeline {
    agent any

    stages {
        stage('Code') {
            steps {
                echo 'This will fetch the code from github'
                git url : "https://github.com/AlyAhmedRbk/todo-flask-app.git", branch : "main"
            }
        }
        
        stage('Build') {
            steps {
                echo 'This will Build the code '
                sh "docker build -t flask-app:latest ."
            }
        }
        
        stage('Push To Dockerhub') {
            steps {
                echo 'This will push the flask image to docker hub repo'
                
                withCredentials([usernamePassword(
                    'credentialsId' : 'dockerHubCred',
                    passwordVariable : 'dockerHubPass',
                    usernameVariable : 'dockerHubUser')]){
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                        sh "docker image tag flask-app:latest alyahmed071/flask-todo-app:latest"
                        sh "docker push ${env.dockerHubUser}/flask-todo-app:latest"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'This will deploy the code '
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
