# filesystem.py

def create_file(filename):
    with open(filename, 'w') as file:
        file.write("Это новый файл операционной системы.")
    print(f"Файл '{filename}' создан.")

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(f"Содержимое файла '{filename}': {content}")

def delete_file(filename):
    import os
    os.remove(filename)
    print(f"Файл '{filename}' удалён.")
