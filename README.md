# scrapy_parser_pep
Парсер, созданый на фреймворке scrapy.\
Предназначен для сбора информации по каждому из PEP.\
Собраную информациию сохраняет в двух файлах формата .csv .\
В первом файле находится список всех PEP в формате "номер, название, статус". 
Во втором файле общее количетво PEP по каждому из статусов.

## Установка проекта.
***- Клонируйте репозиторий:***
```
git clone https://github.com/Kulikov1/foodgram-project-react.git
```

***- Установите и активируйте виртуальное окружение:***
- для MacOS
```
python3 -m venv venv
```
- для Windows
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```

***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```
## Работа с парсером.
Из дериктории проекта выполните команду:
```
scrapy crawl pep
```
Парсер соберет информацию и сохранит файлы в папке results
