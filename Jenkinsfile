pipeline{
    agent none
    environment{
        IMAGE_NAME="ghcr.io/spdx-sarkaz-s-funanceside-fable/API:latest"
        APP_NAME="plus API"
        API_REPO="https://github.com/SPDX-Sarkaz-s-Funanceside-fable/Jenkins-Assignment.git"
        ROBOT_REPO="https://github.com/SPDX-Sarkaz-s-Funanceside-fable/Robot_Jenkins.git"
    }

    stages{

        stage("Clone and Unittest"){
            agent{label: "test-sdpx2"}
            steps{
                echo "Clone the api directory"
                sh "git clone ${API_REPO}"
                echo "Running Unit test"
                sh "cd Jenkins-Assignment/src && pip install -r requirements.txt"
                sh "python3 test_flask.py"
            }
        }

        stage("Build and Push to Registry"){
            agent{label: "test-sdpx2"}
            steps{
                echo "Building the Repository"
                sh "docker build -t ${IMAGE_NAME}"
                sh "docker run -p 5000:5000 ${IMAGE_NAME} --name ${APP_NAME}"
                sh "docker login ghcr.io --username --password "
                sh "docker push ${IMAGE_NAME}"
            }
        }

        stage("Run Robot Test"){
            agent{label: "test-sdpx2"}
            steps{
                echo "Cloning Robot Repository"
                sh "git clone ${ROBOT_REPO}"
                echo "Running Robot Framework Test"
                sh "cd Robot_Jenkins && pip install -r requirements.txt"
                sh "robot apitest.robot"
            }
        }

        stage("Stop Docker and prune"){
            agent{
                label: "test-sdpx2"
            }
            steps{
                echo "Stopping Docker container"
                sh "docker stop ${APP_NAME}"
                sh 'docker system prune -a -f'
            }
        }

        stage("Pull Image from registry"){
            agent{label: "preprod-sdpx3"}
            steps{
                echo "Pulling Image from registry"
                sh "docker pull ${IMAGE_NAME}"
                
                echo "Running Preprod Container"
                sh "docker run ${IMAGE_NAME} --name ${APP_NAME} -p 500:5000"
                echo "Container Created!!!"
            }
        }

        stage("load testing with Jmeter"){
            agent{label: "preprod-sdpx3"}
            steps{
                echo "Load testing"
            }
        }
    }
}