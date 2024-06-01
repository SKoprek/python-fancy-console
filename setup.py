from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README_PIPY.md').read_text(encoding='utf-8')

setup(
    name='dev_fancy_console',
    version='0.0.1',
    description='Stylized Python console, a project made for fun',
    author="SKoprek",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/SKoprek/python-fancy-console',
    entry_points={
        "console_scripts": [
            "fancy_example_1 = dev_fancy_console.examples:example_1",
            "fancy_example_2 = dev_fancy_console.examples:example_2",
            "fancy_example_3 = dev_fancy_console.examples:example_3",
            "fancy_example_4 = dev_fancy_console.examples:example_4",
        ]
    }
)
