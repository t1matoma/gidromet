# Gidromet FastAPI

Проект FastAPI для визуализации данных GRIB (температура, давление) по Центральной Азии.

---

## Установка и запуск

1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/t1matoma/gidromet.git
    cd gidromet
    ```

1. Создать виртуальное окружение и активировать:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Запустить FastAPI:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Открыть браузер и перейти на:
    http://localhost:8000/docs#/

## Эндпоинты

1. /temperature
    Возвращает PNG-график температуры для указанного времени.

    **Пример запроса:**
    ```
    GET /temperature?time=2026-01-30T00%3A00
    ```

2. /pressure
    Возвращает PNG-график давления для указанного времени.
    **Пример запроса:**
    ```
    GET /pressure?time=2026-01-30T00%3A00
    ```

## Архитектура кода:

- app/main.py — создаёт объект FastAPI и подключает маршруты.

- app/endpoints.py — содержит все маршруты API.

- app/grib_service.py — функции для работы с GRIB:

    - загрузка файла

    - выбор данных по времени

    - вырезка региона

    - корректировка координат

- app/plot_utils.py — функции для построения PNG-графиков с помощью matplotlib.

- app/settings.py — все настройки, координаты региона, пути к файлам.
