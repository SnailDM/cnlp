from setuptools import setup
from setuptools import find_packages

setup(
    name='cnlp',
    version='0.0.2',
    author='HaveTwoBrush',
    author_email='kinggreenhall@gmail.com',
    url='https://cnlp.dovolopor.com',
    packages=find_packages(),
    install_requires=[],
    description='Chinese Natural Language Processing.',
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    entry_points={
        'console_scripts': [
                'cnlp=cnlp.shell.usage:run'
        ]
    },
    data_files=[
        ("/tmp/cnlp", ["./cnlp/src/vocab.txt",
                       "./cnlp/src/dict.txt"])
    ]
)
