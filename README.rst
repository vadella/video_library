========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/video_library/badge/?style=flat
    :target: https://readthedocs.org/projects/video_library
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/vadella/video_library.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/vadella/video_library

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/vadella/video_library?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/vadella/video_library

.. |requires| image:: https://requires.io/github/vadella/video_library/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/vadella/video_library/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/vadella/video_library/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/vadella/video_library

.. |version| image:: https://img.shields.io/pypi/v/video-library.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/video-library

.. |commits-since| image:: https://img.shields.io/github/commits-since/vadella/video_library/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/vadella/video_library/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/video-library.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/video-library

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/video-library.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/video-library

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/video-library.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/video-library


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: Apache Software License 2.0

Installation
============

::

    pip install video-library

Documentation
=============

https://video_library.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
