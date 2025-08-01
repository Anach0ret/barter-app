# Barter App

Учебный проект на **Django, DRF**, который реализует работу
площадки для бартерного обмена предложений

---

## 🚀 Технологии

| Категория       | Используется                         |
|-----------------|--------------------------------------|
| Backend         | Django 4+, Django REST               |
| БД              | SqLite                               |
| Контейнеризация | Docker                               |
| Аутентификация  | DRF Token Auth                       |


---

## ⚙️ Установка и запуск

### 1. 📥 Клонируйте репозиторий
```bash
git clone https://github.com/Anach0ret/barter-app.git
cd barter-app
```

### 2. 🐳 Запуск с Docker 
```bash
docker build -t barter-app .
docker run -p 8000:8000 barter-app
```
📌 Приложение будет доступно по адресу: http://localhost:8000

---
📖 Документация

    Swagger UI: http://localhost:8000/swagger

    ReDoc: http://localhost:8000/redoc
