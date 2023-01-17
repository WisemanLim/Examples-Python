# Ref : https://www.studytonight.com/python-howtos/upgrade-all-packages-in-python-using-pip
# -*- coding:utf-8 -*-
# !/usr/bin/python
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)