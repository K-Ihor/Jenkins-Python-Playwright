# Используем официальный образ Python (например, python:3.8-slim)
FROM python:3.8-slim

# Обновляем систему и устанавливаем системные зависимости для Playwright
RUN apt-get update && apt-get install -y \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libxkbcommon0 \
    libpango-1.0-0 \
    libcairo2 \
    xdg-utils \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Задаем PYTHONPATH, чтобы Python видел корень проекта
ENV PYTHONPATH=/app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры Playwright (Chromium, Firefox, WebKit)
RUN playwright install

# Создаем папку для результатов Allure, которую можно монтировать с хоста
RUN mkdir -p /app/allure-results

# Копируем исходный код проекта
COPY . .

# Команда для запуска тестов
CMD ["pytest", "--alluredir=/app/allure-results", "--maxfail=11", "--disable-warnings", "-q"]
