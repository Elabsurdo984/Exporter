from setuptools import setup, find_packages

setup(
    name="exporter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "reportlab",
        "Pillow",
        "pandas",
    ],
    author="Elabsurdo984",
    author_email="matiassfernandez00@gmail.com",
    description="Una libreria para exportar archivos a formato PDF.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tu_usuario/export_to_pd",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)