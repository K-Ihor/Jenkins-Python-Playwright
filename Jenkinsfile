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
                // Собираем Docker-образ для тестового фреймворка
                sh 'docker build -t aqa-tests .'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Пытаемся запустить тесты внутри контейнера.
                    // Если тесты падают, ошибка ловится, и сборка помечается как UNSTABLE, но дальнейшие стадии выполняются.
                    try {
                        sh 'docker run --rm -v ${WORKSPACE}/allure-results:/app/allure-results aqa-tests'
                    } catch (err) {
                        echo "Tests failed: ${err}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Архивируем результаты Allure, даже если тесты не прошли
                archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Генерируем отчет Allure на основе результатов
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }
    post {
        always {
            // Очистка рабочей области после сборки
            cleanWs()
        }
    }
}
