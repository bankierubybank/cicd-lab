pipeline {
    agent {
        label 'runner-linux'
    }
    stages {
        stage('SCM: Checkout') {
            steps {
                sh 'git clone https://github.com/bankierubybank/cicd-lab.git'
            }
        }
        stage('SCA/SAST') {
            steps {
                echo 'SCA/SAST scaning... (DUMMY)'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t cicd-lab:$BUILD_NUMBER .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying... (DUMMY)'
            }
        }
        stage('Test') {
            steps {
                echo 'Starting application functional testing... (DUMMY)'
                echo 'Starting application security testing... (DUMMY)'
                echo 'Starting application performance testing... (DUMMY)'
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
