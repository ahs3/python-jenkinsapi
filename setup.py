from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.2.16'
PROJECT_NAME = 'JenkinsAPI'
PROJECT_AUTHORS = "Salim Fadhley, Ramon van Alteren, Ruslan Lutsenko"
PROJECT_EMAILS = 'salimfadhley@gmail.com, ramon@vanalteren.nl, ruslan.lutcenko@gmail.com'
PROJECT_URL = "https://github.com/salimfadhley/jenkinsapi"
SHORT_DESCRIPTION = 'A Python API for accessing resources on a Jenkins continuous-integration server.'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "README.rst")).read()
except IOError, _:
    DESCRIPTION = SHORT_DESCRIPTION

GLOBAL_ENTRY_POINTS = {
    "console_scripts": ["jenkins_invoke=jenkinsapi.command_line.jenkins_invoke:main"]
}

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=['jenkinsapi', 'jenkinsapi.utils', 'jenkinsapi.command_line', 'jenkinsapi_tests'],
    zip_safe=True,
    include_package_data=False,
    install_requires=['requests>=1.2.3', 'pytz>=2013b'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage'],
    entry_points=GLOBAL_ENTRY_POINTS,
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ],
)
