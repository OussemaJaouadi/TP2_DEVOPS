pipeline{
    agent any
    stages{
        stage("Pulling code") {
            steps {
                git url: 'https://github.com/OussemaJaouadi/TP2_DEVOPS/', branch: 'master',
                sh "ls -ltr"
            }
        }
        // Usually some test are integrated here
       //build de l'image
         stage("Build the image"){
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
                        //sh "docker tag devopstp oussemajaouadi/tp_devops:$BUILD_NUMBER"
                        //sh "docker push oussemajaouadi/tp_devops:$BUILD_NUMBER"
                           }        
                        }
                    }              
                }
            post{
                success{
                    echo "======== Setting up infra executed successfully ========"
                }
                failure{
                    echo "======== Setting up infra execution failed ========"
                }
            }
             
        }        