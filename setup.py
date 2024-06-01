from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='dev_fancy_console',
    version='0.1',
    description='Stylized Python console, a project made for fun',
    author="SKoprek",
    long_description=long_description,
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
