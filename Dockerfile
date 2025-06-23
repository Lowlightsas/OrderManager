# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
COPY . /app/

# Обновляем pip и устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 8000

# Команда по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
