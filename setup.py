from setuptools import setup, find_packages

setup(
    name='gritter',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'tweepy',
    ],
    entry_points='''
        [console_scripts]
        gritter=gritter.gritter.cli:cli
    ''',
)