pipeline{
    agent {label 'preprod-sdpx3'}
    environment{
        APP_NAME="test app name"
    }
    stages{
        stage("Build Image"){
            steps{
                sh "echo ${env.APP_NAME}"
                sh "docker version"
                sh "docker ps"
            }
        }
    }
}