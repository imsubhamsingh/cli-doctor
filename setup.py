from setuptools import setup, find_packages

setup(
    name="doctor",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "doctor=cli_doctor.cli:main",
        ],
    },
    author="Shubham Singh",
    author_email="geekysubham@gmail.com",
    description="A CLI application to chat with AI.",
)
