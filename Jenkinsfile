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
                // Собираем Docker-образ
                sh 'docker build -t aqa-tests .'
            }
        }
        stage('Run Tests') {
            steps {
                // Запускаем контейнер с монтированием папки для Allure-результатов
                sh 'docker run --rm -v ${WORKSPACE}/allure-results:/app/allure-results aqa-tests'
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Сохраняем результаты тестов для последующего анализа
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

