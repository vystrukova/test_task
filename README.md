## Тесты на Python3 (PyTest + Selenium + Requests)

- Для создания виртуальной среды выполните следующие команды:
> pip install virtualenv

> virtualenv venv

- Для установки зависимостей выполните следующие команды:
> pip install -r requirements.txt

> pip freeze > requirements.txt

- Для запуска всех тестов используйте команду:
> pytest -s -v

### Генерация отчетов Allure:

1. Создайте папку, в которую allure будет складывать необходимые для генерации отчета файлы. Например, папка reports в директории проекта.

![image](https://user-images.githubusercontent.com/106829774/229935744-2e82e1bf-ec81-4949-8943-d295d4c53832.png)

2. Для генерации отчета используйте следующую команду:

> pytest --alluredir=reports

- По завершении выполнения тестов выполните команду для формирования отчета на основе имеющихся файлов с результатами:

> allure serve reports

![image](https://user-images.githubusercontent.com/106829774/229936570-25f315cc-b656-4306-b0fc-32ec1d0f4727.png)
