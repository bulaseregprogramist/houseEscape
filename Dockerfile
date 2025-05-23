# Используем официальный образ Python как базовый
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы из текущей директории в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Команда для запуска приложения
CMD ["python", "main.py"]
