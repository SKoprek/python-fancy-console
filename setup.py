from setuptools import setup, find_packages

setup(
    name='fancy_console',
    version='0.1',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fancy_example_1 = fancy_console.examples:example_1",
            "fancy_example_2 = fancy_console.examples:example_2",
            "fancy_example_3 = fancy_console.examples:example_3",
            "fancy_example_4 = fancy_console.examples:example_4",
        ]
    }
)
