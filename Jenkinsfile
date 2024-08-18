pipeline {
    agent any

    environment {
        containerRegistryName = 'containerregistry1z.azurecr.io'
        dockerImageName = 'ul-renewables1'
    }

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Get the latest commit hash
                    def hash = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    echo "Commit Hash: ${hash}"
                    
                    // Define build number
                    def buildNumber = env.BUILD_NUMBER
                    echo "Build Number: ${buildNumber}"
                    
                    // Build Docker image
                    sh "docker build . -t ${dockerImageName}:${hash}"
                    sh "docker tag ${dockerImageName}:${hash} ${containerRegistryName}/${dockerImageName}:${hash}"
                    sh "docker tag ${containerRegistryName}/${dockerImageName}:${hash} ${containerRegistryName}/${dockerImageName}:${buildNumber}"
                    
                    // Docker login and push
                    withCredentials([usernamePassword(credentialsId: 'dockerCredentialsId', usernameVariable: 'D_USERNAME', passwordVariable: 'D_PASSWORD')]) {
                        sh "echo ${D_PASSWORD} | docker login ${containerRegistryName} -u ${D_USERNAME} --password-stdin"
                        sh "docker push ${containerRegistryName}/${dockerImageName}:${buildNumber}"
                    }
                }
            }
        }
    }
}
