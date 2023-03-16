## Тесты на Python + PyTest
> pip install virtualenv

> virtualenv venv

> pip install -r requirements.txt

> pip freeze > requirements.txt

#### Для запуска всех тестов:
> pytest -s -v

#### Для запуска ui тестов с возможностью выбора браузера:

> cd test reqres

> cd ui_web

> pytest -s -v —browser_name=chrome
или
> pytest -s -v —browser_name=firefox
