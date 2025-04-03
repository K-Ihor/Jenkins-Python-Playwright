Сборка Docker-образа
В корне проекта (где находится Dockerfile) выполните команду:

bash

docker build -t aqa-tests .


Запуск контейнера
Запустите контейнер с тестами:

bash
docker run --rm aqa-tests

docker run --rm -v $(pwd)/allure-results:/app/allure-results aqa-tests





Или, если вы используете docker-compose:

bash

docker-compose up --build


Чтобы запустить тесты локально (без Docker-контейнера), откройте терминал в корневой папке проекта и выполните команду:

bash

pytest --maxfail=1 --disable-warnings -q
Эта команда:

--maxfail=1: останавливает выполнение тестов после первого сбоя,

--disable-warnings: отключает вывод предупреждений,

-q: включает компактный (quiet) режим вывода результатов.

Если вам не нужны эти опции, достаточно выполнить просто:

bash
Копировать код
pytest

Для генерации HTML‑отчёта выполните
allure serve allure-results




Jenkins docker
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

