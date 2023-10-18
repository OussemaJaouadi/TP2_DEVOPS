pipeline {
    agent {
        docker {
            label : "docker_agent"
        }
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
                    sh "echo $DOCKER_HUB"
                    // Uncomment the following lines once you have the correct DockerHub credentials configured in Jenkins
                    // sh "docker login -u your-dockerhub-username -p your-dockerhub-password"
                    // sh "docker tag devopstp your-dockerhub-username/tp_devops:$BUILD_NUMBER"
                    // sh "docker push your-dockerhub-username/tp_devops:$BUILD_NUMBER"
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
