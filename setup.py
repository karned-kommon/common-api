from setuptools import setup, find_packages

setup(
    name="common-api",
    version="0.1.0",
    packages=find_packages(where=".", include=["common_api", "common_api.*"]),
    install_requires=[
        "httpx",
        "fastapi",
        "starlette",
        "redis",
    ],
    author="Karned",
    author_email="<EMAIL>",
    description="Shared FastAPI common utilities and services",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/karned-kommon/shared",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)