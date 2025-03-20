# setup.py
from setuptools import setup, find_packages

setup(
    name="py_ynuson_lib",
    version="0.1",
    packages=find_packages(),
    description="Библиотека для создания операционных систем на Python",
    author="Vadim Papin",
    author_email="vadimpapin188@gmail.com",
    url="",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)
