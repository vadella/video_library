import sys

try:
    from setuptools import setup
except ImportError:
    print('Please install or upgrade setuptools or pip to continue')
    sys.exit(1)

long_description = """test description"""
__doc__ = long_description

setup(
    name='video_bibliotheek',
    version='0.1',
    description='parse info from mkv files',
    long_description=long_description,
    keywords='mkv info',
    author='Maarten Fabré',
    author_email='maartenfabre@gmail.com',
    url='https://github.com/vadella/video_library',
    # test_suite='pint.testsuite.testsuite',
    zip_safe=False,
    packages=['video_bibliotheek'],
    # package_data={
    #     'pint': ['default_en.txt',
    #              'constants_en.txt']
    # },
    platforms='any',
    include_package_data=False,
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        # 'Topic :: Scientific/Engineering',
        # 'Topic :: Software Development :: Libraries',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ])
