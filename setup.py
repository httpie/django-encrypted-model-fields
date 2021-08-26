#!/usr/bin/env python

import re
import os
from setuptools import setup, find_packages


with open('encrypted_model_fields/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-encrypted-model-fields',
    version=version,
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    description=(
        'A set of django fields that internally are encrypted using the '
        'cryptography.io native python encryption library.'
    ),
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='http://gitlab.com/lansharkconsulting/django/django-encrypted-model-fields/',
    download_url=f'https://gitlab.com/lansharkconsulting/django/django-encrypted-model-fields/repository/archive.tar.gz?ref=v{version}',  # noqa
    author='Scott Sharkey',
    author_email='ssharkey@lanshark.com',
    maintainer="Scott Sharkey",
    maintainer_email="ssharkey@lanshark.com",
    python_requires='>=3.6, <=3.10',
    install_requires=[
        'Django>=2.2',
        'cryptography>=3.4',
    ],
    tests_require=['tox'],
    keywords=['encryption', 'django', 'fields', ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Topic :: Internet :: WWW/HTTP",
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
    ],
)
