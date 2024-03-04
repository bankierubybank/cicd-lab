pipeline {
    agent {
        label 'runner-linux'
    }

    stages {
        stage('SCM: Checkout') {
            steps {
                sh 'git clone https://github.com/bankierubybank/cicd-lab.git'
                sh 'ls -l'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t cicd-lab:$BUILD_NUMBER .'
                sh 'docker images'
            }
        }
    }
    post { 
        cleanup {
            // Remove workspace
            cleanWs()
            sh 'docker rmi cicd-lab:$BUILD_NUMBER'
        }
    }
}
