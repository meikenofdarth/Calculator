// pipeline {
//     agent any

//     // ADD THIS TOOLS BLOCK
//     tools {
//         dockerTool 'docker-tool'
//     }

//     environment {
//         DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
//         DOCKER_IMAGE_NAME = "smoothlake67/scientific-calculator"
//     }

//     stages {
//         stage('Run Unit Tests') {
//             agent {
//                 // This part remains the same
//                 docker { image 'python:3.9-slim' }
//             }
//             steps {
//                 echo 'Running unit tests...'
//                 sh 'python -m unittest discover'
//             }
//         }
//         stage('Build Docker Image') {
//             steps {
//                 echo 'Building the Docker image...'
//                 script {
//                     dockerImage = docker.build(DOCKER_IMAGE_NAME, ".")
//                 }
//             }
//         }
//         stage('Push to Docker Hub') {
//             steps {
//                 echo "Pushing the Docker image to Docker Hub..."
//                 script {
//                     docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
//                         dockerImage.push("${env.BUILD_NUMBER}")
//                         dockerImage.push("latest")
//                     }
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             echo 'Pipeline finished.'
//         }
//     }
// }

// pipeline {
//     agent any // This now works because the agent has Docker installed.

//     // The 'tools' block has been removed.

//     environment {
//         DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
//         DOCKER_IMAGE_NAME = "smoothlake67/scientific-calculator"
//     }

//     stages {
//         stage('Run Unit Tests') {
//             agent {
//                 docker { image 'python:3.9-slim' }
//             }
//             steps {
//                 echo 'Running unit tests...'
//                 sh 'python -m unittest discover'
//             }
//         }
//         stage('Build Docker Image') {
//             steps {
//                 echo 'Building the Docker image...'
//                 script {
//                     dockerImage = docker.build(DOCKER_IMAGE_NAME, ".")
//                 }
//             }
//         }
//         stage('Push to Docker Hub') {
//             steps {
//                 echo "Pushing the Docker image to Docker Hub..."
//                 script {
//                     docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
//                         dockerImage.push("${env.BUILD_NUMBER}")
//                         dockerImage.push("latest")
//                     }
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             echo 'Pipeline finished.'
//         }
//     }
// }


pipeline {
    agent any

    tools {
        dockerTool 'docker-tool'
    }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_IMAGE_NAME = "smoothlake67/scientific-calculator"
    }

    stages {
        stage('Run Unit Tests') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest discover'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                script {
                    dockerImage = docker.build(DOCKER_IMAGE_NAME, ".")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                echo "Pushing the Docker image to Docker Hub..."
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}