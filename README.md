---

````markdown
# 🧾 Order & Ticket Management System

Веб-приложение для управления заказами и тикетами, разработанное на Django.  
Проект поддерживает:

- 👤 Авторизацию и ролевую систему (`Managers`)
- 📦 CRUD-интерфейс для заказов и тикетов
- 🌐 REST API для обновления статуса тикетов извне
- 🐳 Запуск через Docker без ручной настройки окружения

---

## 📦 Быстрый старт (через Docker)

> Убедись, что у тебя установлен Docker и docker-compose.

1. 📁 Перейди в корневую папку проекта:

```bash
cd path/to/your/project
````

2. ▶️ Запусти сборку и приложение:

```bash
docker-compose up --build
```

3. 🔎 Приложение будет доступно по адресу:

```
http://localhost:8000
```

---

## 🛠 Полезные команды

* 📦 Миграции:

  ```bash
  docker-compose exec web python manage.py migrate
  ```

* 👑 Создание суперпользователя:

  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```

* 🧪 Тестирование (если настроено):

  ```bash
  docker-compose exec web python manage.py test
  ```

---

## 🔄 Обновление статуса тикета через API (Postman)

### ✅ Endpoint

```
POST http://localhost:8000/api/tickets/update_status/
```

### 🔐 Заголовки

```
Content-Type: application/json
```

### 📤 Тело запроса (raw JSON)

```json
{
  "code": "abc123",
  "status": "in_progress"
}
```

> 🔁 Возможные статусы:
>
> * `pending` — Ожидает
> * `in_progress` — В работе
> * `completed` — Завершен

### 💬 Ответ при успехе

```json
{
  "message": "Ticket abc123 updated to in_progress."
}
```

### ❗️ Возможные ошибки

| Код | Причина                                                 |
| --- | ------------------------------------------------------- |
| 400 | Отсутствует `code` или `status`, либо статус недопустим |
| 404 | Тикет с таким кодом не найден                           |

---

## 🧑‍💻 Технологии

* 💬 **Python 3.10+**
* 🌐 **Django 4.x**
* 🔁 **Django REST Framework**
* 🐘 **PostgreSQL** (или SQLite)
* 🐳 **Docker & Docker Compose**
* 🎨 Bootstrap (в интерфейсе)

---

## 📂 Структура (основное)

```text
├── Dockerfile
├── docker-compose.yml
├── .env
├── manage.py
├── requirements.txt
├── app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── templates/
```

---

## 🔐 Роли пользователей

| Роль    | Описание                                                       |
| ------- | -------------------------------------------------------------- |
| Manager | Может создавать, редактировать и просматривать заказы и тикеты |
| User    | Нет доступа к интерфейсу заказов                               |

> ⚠️ Только пользователи из группы `Managers` могут работать с системой.

---


![image](https://github.com/user-attachments/assets/f1cfec46-7cb4-4f15-8e65-1b6cec82ccc1)
