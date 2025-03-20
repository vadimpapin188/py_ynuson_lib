# py_ynuson_lib
Это библиотека для создания операционных систем на Python.

## Установка

Вы можете установить библиотеку через pip:

pip install py_ynuson_lib

csharp


## Пример использования

```python
import py_ynuson_lib

# Создание и запуск операционной системы
os = my_library.OSKernel()
os.start()
os.create_process("Процесс 1")

# Создание и использование интерфейса
interface = my_library.OSInterface()
interface.create_label("Добро пожаловать в мою ОС!")
interface.create_button("Нажми меня", lambda: print("Кнопка нажата"))
interface.run()