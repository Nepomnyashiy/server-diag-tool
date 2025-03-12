# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями из корня проекта
COPY ../requirements.txt /app/requirements.txt

# Обновляем pip перед установкой зависимостей
RUN python -m pip install --upgrade pip

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем весь проект (исключая .git, __pycache__)
COPY ../ /app

# Убеждаемся, что папка reports доступна и подключена из внешнего хоста
RUN mkdir -p /app/reports

# Запуск диагностики при старте контейнера
CMD ["python", "diagnostics/cpu_ram.py"]
