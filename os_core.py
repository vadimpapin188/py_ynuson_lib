# os_core.py

class OSKernel:
    def __init__(self):
        self.running_processes = []

    def start(self):
        print("Операционная система запущена.")

    def shutdown(self):
        print("Операционная система выключена.")

    def create_process(self, process_name):
        self.running_processes.append(process_name)
        print(f"Процесс '{process_name}' создан и запущен.")
