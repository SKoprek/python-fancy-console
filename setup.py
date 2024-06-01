from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name='fancy_console',
    version='0.1',
    description='Stylized Python console, a project made for fun..',
    author="SKoprek",
    long_description=readme(),
    packages=find_packages(),
    url='https://github.com/SKoprek/python-fancy-console',
    entry_points={
        "console_scripts": [
            "fancy_example_1 = fancy_console.examples:example_1",
            "fancy_example_2 = fancy_console.examples:example_2",
            "fancy_example_3 = fancy_console.examples:example_3",
            "fancy_example_4 = fancy_console.examples:example_4",
        ]
    }
)
