#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages
import shop
try:
    from pypandoc import convert
except ImportError:
    import io

    def convert(filename, fmt):
        with io.open(filename, encoding='utf-8') as fd:
            return fd.read()

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Jacob Rief",
    author_email="jacob.rief@gmail.com",
    name="django-shop",
    version=shop.__version__,
    description="A RESTful e-commerce framework based on Django",
    long_description=convert('README.md', 'rst'),
    url='http://www.django-shop.org/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['example', 'docs', 'testshop']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.10,<2.0',
        'django-post-office>=3.0.0',
        'django-filer>=1.3.0',
        'django-ipware>=1.1.1',
        'django-fsm>=2.5',
        'django-fsm-admin>=1.2.4',
        'djangorestframework>=3.7',
        'django-angular>=2.0',
        'Django-Select2>=5.11',
        'django-rest-auth>=0.9',
        'django-admin-sortable2>=0.6.15',
        'django-formtools>=1.0',
        'djangocms-cascade>=0.14',
    ],
    # Note: this requires setuptools >= 18.0.
    extras_require={
        ':python_version<"3.4"': ['enum34'],
    },
)
