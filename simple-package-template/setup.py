from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="beatriz_toolkit",  # Nome do seu pacote
    version="0.0.1",
    author="Beatriz Candido",  # Seu nome
    author_email="beatrizpereiracandido@gmail.com",  # Seu e-mail
    description="Um pacote Python para demonstração",  # Uma breve descrição
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BeatrizPCandido/simple-package-template",  # Link do seu repositório GitHub
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
