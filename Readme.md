# Simple Backup

## Программа для копирования файлов (Пример)

### Зависимости

  - Python 2
  - PySide
  - Qt4
  
# Запуск и принцип работы

Gui запускаются по файлу main.py 
  ```bash
  python main.py
  ```

Без GUI 

 ```bash
 python backup.py -p data\NameProject.json data\NameSecondProject.json
 ```
 
 Программа считывает правила из файла name.json который создается через GUI и 
 запускает в отдельном потоке копирование файлов по заданному в правилах расписанию