pipeline {
    agent any

    environment {
        ALLURE_RESULTS = "${WORKSPACE}/allure-results"
    }

    stages {
        stage('Checkout') {
            steps {
                // Клонируем репозиторий
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Собираем Docker-образ для тестов
                sh 'docker build -t aqa-tests .'
            }
        }
        stage('Run Tests') {
            steps {
                // Запускаем контейнер и монтируем папку для Allure-результатов
                sh 'docker run --rm -v ${WORKSPACE}/allure-results:/app/allure-results aqa-tests'
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Архивируем результаты тестов для дальнейшего анализа
                archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Если установлен плагин Allure, генерируем отчет
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
