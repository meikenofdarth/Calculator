pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_IMAGE_NAME = "smoothlake67/scientific-calculator"
    }

    stages {
        // The Checkout stage has been removed.
        stage('Run Unit Tests') {
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