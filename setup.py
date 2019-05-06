from setuptools import setup
from easy_math import VERSION

setup(
    name='python-easy-math',
    version=VERSION,
    py_modules=['easy_math.addition', 'easy_math.subtraction'],
    url='https://github.com/svpernova09/python-easy-math',
    download_url='https://github.com/svpernova09/python-easy-math/tarball/{}'.format(VERSION),
    license='MIT',
    author='Joe Ferguson',
    author_email='joe@joeferguson.me',
    description='Python library for basic addition and subtraction of two numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'addition=easy_math.addition:main',
            'subtraction=easy_math.subtraction:main'
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
