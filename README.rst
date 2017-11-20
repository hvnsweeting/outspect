========
outspect
========


.. image:: https://img.shields.io/pypi/v/outspect.svg
        :target: https://pypi.python.org/pypi/outspect

.. image:: https://img.shields.io/travis/hvnsweeting/outspect.svg
        :target: https://travis-ci.org/hvnsweeting/outspect

.. image:: https://readthedocs.org/projects/outspect/badge/?version=latest
        :target: https://outspect.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/hvnsweeting/outspect/shield.svg
     :target: https://pyup.io/repos/github/hvnsweeting/outspect/
     :alt: Updates


Better `inspect` for Python.


* Free software: MIT license
* Documentation: https://outspect.readthedocs.io.

Usage
-----

::

  In []: import django

  In []: import django.http

  In []: from outspect import *

  In []: classes(django.http)
  Out[]: ['BadHeaderError', 'FileResponse', 'Http404', 'HttpRequest', 'HttpResponse', 'HttpResponseBadRequest', 'HttpResponseForbidden', 'HttpResponseGone', 'HttpResponseNotAllowed', 'HttpResponseNotFound', 'HttpResponseNotModified', 'HttpResponsePermanentRedirect', 'HttpResponseRedirect', 'HttpResponseServerError', 'JsonResponse', 'QueryDict', 'R11awPostDataException', 'SimpleCookie', 'StreamingHttpResponse', 'UnreadablePostError']

  In []: import logging

  In []: pub_funcs(logging)
  Out[]: ['addLevelName', 'basicConfig', 'captureWarnings', 'critical', '<lambda>', 'debug', 'disable', 'error', 'exception', 'critical', 'getLevelName', 'getLogRecordFactory', 'getLogger', 'getLoggerClass', 'info', 'log', 'makeLogRecord', 'setLogRecordFactory', 'setLoggerClass', 'shutdown', 'warn', 'warning']

  In []: constants(logging)
  Out[]: ['BASIC_FORMAT', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'INFO', 'NOTSET', 'WARN', 'WARNING', '_STYLES']


Features
--------

- Inspecting objects, modules ...

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

