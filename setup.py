from setuptools import setup

setup(
    name='cnlp',
    version='0.0.1',
    author='HaveTwoBrush',
    author_email='kinggreenhall@gmail.com',
    url='https://cnlp.dovolopor.com',
    packages=['cnlp'],
    install_requires=[],
    description='Chinese Natural Language Processing.',
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    entry_points={
        'console_scripts': [
                'cnlp=cnlp:hello'
        ]
    }
)
