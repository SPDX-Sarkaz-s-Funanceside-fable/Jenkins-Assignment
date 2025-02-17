pipeline {
    agent none
    environment {
        IMAGE_NAME = 'ghcr.io/spdx-sarkaz-s-funanceside-fable/api:latest'
        APP_NAME = 'plus_api'
        API_REPO = 'https://github.com/SPDX-Sarkaz-s-Funanceside-fable/Jenkins-Assignment.git'
        ROBOT_REPO = 'https://github.com/SPDX-Sarkaz-s-Funanceside-fable/Robot_Jenkins.git'
    }

    stages {
        stage('Clone and Unittest') {
            agent { label 'test-sdpx2' }
            steps {
                echo 'Clone the api directory'
                script {
                    if (fileExists('Jenkins-Assignment')) {
                        echo 'Repository exists, pulling latest changes...'
                        sh 'cd Jenkins-Assignment && git pull'
            } else {
                        echo 'Cloning the API repository...'
                        sh "git clone ${API_REPO}"
                    }
                }
                echo 'Running Unit test'
                sh 'cd Jenkins-Assignment/src && pip install -r requirements.txt && python3 test_flask.py'
            }
        }

        stage('Run Robot Test') {
            agent { label 'test-sdpx2' }
            steps {
                script {
                    if (fileExists('Robot_Jenkins')) {
                        echo 'Repository exists, pulling latest changes...'
                        sh 'cd Robot_Jenkins && git pull'
            } else {
                        echo 'Cloning the ROBOT repository...'
                        sh "git clone ${ROBOT_REPO}"
                    }
                }
                echo 'Running Robot Framework Test'
                sh "mkdir -p /home/student/robot_results"
                sh 'cd Robot_Jenkins && pip install -r requirements.txt && python3 -m robot --outputdir /home/student/robot_results apitest.robot'
            }
        }

        stage('Build and Push to Registry') {
            agent { label 'test-sdpx2'}
            steps {
                echo 'Building the Repository'
                sh "cd Jenkins-Assignment/src && docker build -t ${IMAGE_NAME} ."
                sh "docker run -d --name ${APP_NAME} -p 5000:5000 ${IMAGE_NAME} "

                echo 'logging in...'
                withCredentials([usernamePassword(credentialsId: '49f9bc0f-974f-48da-bc43-c5abb21d228c', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "${DOCKER_PASS}" | docker login ghcr.io -u "${DOCKER_USER}" --password-stdin
                    """
                }
                sh "docker push ${IMAGE_NAME}"
            }
        }



        stage('Stop Docker and prune') {
            agent {
                label 'test-sdpx2'
            }
            steps {
                echo 'Stopping Docker container'
                sh "docker stop ${APP_NAME}"
                sh 'docker system prune -a -f'
            }
        }

        stage('Pull Image from registry') {
            agent { label 'preprod-sdpx3' }
            steps {
                echo "loggin in..."
                    withCredentials([usernamePassword(credentialsId: '49f9bc0f-974f-48da-bc43-c5abb21d228c', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "${DOCKER_PASS}" | docker login ghcr.io -u "${DOCKER_USER}" --password-stdin
                    """
                }
                echo 'Pulling Image from registry'
                sh "docker pull ${IMAGE_NAME}"
                echo 'Running Preprod Container'
                sh "docker run -d -p 5000:5000 --name ${APP_NAME} ${IMAGE_NAME} "
                echo 'Container Created!!!'
            }
   