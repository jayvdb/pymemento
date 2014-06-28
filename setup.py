from setuptools import setup

setup(
    name='pymemento',
    version='0.1-SNAPSHOT',
    author='Shawn M. Jones',
    author_email='sjone@cs.odu.edu',
    packages=['pymemento'],
    url='https://github.com/mementoweb/pymemento',
    license='LICENSE.txt',
    description='Official Python library for using the Memento Protocol',
    long_description=open('README.txt').read(),
    install_requires=[
        'python-dateutil',
    ],
    keywords='memento http',

)
