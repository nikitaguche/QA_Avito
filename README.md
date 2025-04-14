# README.md

## Тестирование API сервиса объявлений

### Предварительные требования

1. **Установите Python 3.13**:
   - Скачайте с [официального сайта](https://www.python.org/downloads/)
   - Проверьте установку: `python --version`

2. **Установите зависимости**:
   ```bash
   pip install pytest requests
   ```

### Клонирование репозитория
```bash
git clone https://github.com/nikitaguche/QA_Avito
cd avito-tech-internship
```

### Запуск тестов

**Основные тесты:**
```bash
pytest test_avito_api.py -v
```

**С генерацией отчета:**
```bash
pytest test_avito_api.py --html=report.html
```

**Запуск конкретного теста:**
```bash
pytest test_avito_api.py::test_create_ad_success -v
```

### Структура проекта
```
.
├── README.md          # Инструкция
├── test_avito_api.py  # Автотесты
├── TESTCASES.md       # Тест-кейсы
└── BUGS.md            # Отчет о дефектах
```

### Переменные окружения
Для работы с другим окружением измените базовый URL в файле `test_avito_api.py`:
```python
BASE_URL = "https://your-custom-url.com"  # По умолчанию qa-internship.avito.com
```

### Анализ результатов
- Успешные тесты отмечаются как **PASSED**
- Неудачные - **FAILED**
- Ошибки валидации - **ERROR**

**Пример вывода:**
```
============================= test session starts =============================
test_avito_api.py::test_create_ad_success PASSED                         [ 11%]
test_avito_api.py::test_create_ad_missing_price FAILED                   [ 22%]
...
========================= 7 passed, 2 failed in 1.45s =========================
```

### Контакты
Гутченко Никита
