pipeline {
    agent any
    environment {
        DOCKER_HUB = credentials('dockerhub')
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
                    sh "docker build -t devopstp ."
                    sh "docker images"
                }
            }
        }
        
        stage("Pushing Image") {
            steps {
                script {
                    //sh "echo $DOCKER_HUB"
                    // Uncomment the following lines once you have the correct DockerHub credentials configured in Jenkins
                    sh "docker login -u $DOCKER_HUB_USR -p $DOCKER_HUB_PSW"
                    sh "docker tag devopstp $DOCKER_HUB_USR/tp_devops:$BUILD_NUMBER"
                    sh "docker push $DOCKER_HUB_USRe/tp_devops:$BUILD_NUMBER"
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
