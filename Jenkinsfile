pipeline{
    agent {label 'test-sdpx2'}
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