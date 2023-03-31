from setuptools import setup, find_packages

setup(
    name="Dyne Telegram Bot",
    version="0.1.0",
    author="Puria Nafisi Azizi",
    author_email="puria@dyne.org",
    packages=find_packages(),
    install_requires=[
        "emoji==0.5.1",
        "redis==4.4.4",
        "inflect==2.1.0",
        "environs==4.2.0",
        "SQLAlchemy==1.3.5",
        "python-telegram-bot==11.1.0",
    ],
    tests_require=["pytest", "codecov", "requests", "pytest-cov"],
)
