# web-http-lab

Проект-лабораторная по курсу "Python Backend Developer Pre-Trainee"
## Запуск проекта

Для запуска приложения нужно:

### 1. Клонировать репозиторий
```bash
git clone https://github.com
cd ваш-репозиторий
```

### 2. Создать и активировать виртуальное окружение
* **Для Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Для Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Запустить сервер разработки
```bash
uvicorn main:app --reload
```