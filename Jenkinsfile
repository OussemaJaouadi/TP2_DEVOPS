pipeline {
    agent any
    environment {
        DOCKER_HUB = credentials('dockerhub')
        dockerImage= ""
    }
    stages {
        stage("Pulling code") {
            steps {
                git branch: 'main', url: 'https://github.com/OussemaJaouadi/TP2_DEVOPS/'
                sh "ls -ltr"
            }
        }
        
        stage("Build the image") {
            steps {
                script {
                    dockerImage = docker.build("devopstp:$BUILD_NUMBER")
                }
            }
        }
        
        stage("Pushing Image") {
            steps {
                script {
                    //sh "echo $DOCKER_HUB"
                    // Uncomment the following lines once you have the correct DockerHub credentials configured in Jenkins
                    withDockerRegistry(
                        [credentialsId:"dockerhub",url:""]
                    ){
                        dockerImage.push("oussemajaouadi/tp_devops:$BUILD_NUMBER")
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo "======== Setting up infra executed successfully ========"
        }
        failure {
            echo "======== Setting up infra execution failed ========"
        }
    }
}
