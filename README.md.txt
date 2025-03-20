# py_ynuson_lib
��� ���������� ��� �������� ������������ ������ �� Python.

## ���������

�� ������ ���������� ���������� ����� pip:

pip install py_ynuson_lib

csharp


## ������ �������������

```python
import py_ynuson_lib

# �������� � ������ ������������ �������
os = my_library.OSKernel()
os.start()
os.create_process("������� 1")

# �������� � ������������� ����������
interface = my_library.OSInterface()
interface.create_label("����� ���������� � ��� ��!")
interface.create_button("����� ����", lambda: print("������ ������"))
interface.run()