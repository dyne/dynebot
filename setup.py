from setuptools import setup, find_packages

setup(
    name="Dyne Telegram Bot",
    version="0.1.0",
    author="Puria Nafisi Azizi",
    author_email="puria@dyne.org",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==11.1.0",
        "emoji==0.5.1",
        "redis==3.2.0",
    ],
    tests_require=["pytest", "codecov", "requests", "pytest-cov"],
)
