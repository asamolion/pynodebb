#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""./fabric.py

Copyright (c) 2015 David Vuong <david.vuong256@gmail.com>
Licensed MIT
"""
from fabric.api import task, local


@task
def clean():
    """Cleans up compiled or trash files."""
    local('find . -type f -name "*.pyc" -delete')
    local('find . -type f -name ".DS_Store" -delete')
    local('find . -type d -name "__pycache__" -delete')


@task(alias='pep')
def pep8():
    """Validate syntax style against PEP8."""
    local('pep8 pynodebb/ --ignore=E501')  # Ignore >79 char lines.


@task
def test():
    """Runs unit tests."""
    local('nosetests test/*.py')


@task
def cover():
    """Determines test coverage."""
    local('nosetests test/*.py --with-coverage --cover-package=pynodebb')