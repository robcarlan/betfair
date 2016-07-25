import sys
from distutils.core import setup, Extension
from setuptools.command.test import test as TestCommand
from betfairlightweight.__init__ import __version__


INSTALL_REQUIRES = [
    'requests>=2.6.2',
]
TEST_REQUIRES = [
    'pytest'
]


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--verbose']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
        name='betfairlightweight',
        version=__version__,
        packages=['betfairlightweight', 'betfairlightweight.parse',
                  'betfairlightweight.streaming', 'betfairlightweight.endpoints'],
        package_dir={'betfairlightweight': 'betfairlightweight'},
        install_requires=INSTALL_REQUIRES,
        requires=['requests'],
        url='https://github.com/LiamPa/betfairlightweight',
        license='',
        author='liampauling',
        author_email='',
        description='Lightweight python wrapper for Betfair API-NG',
        test_suite='tests',
        tests_require=TEST_REQUIRES,
        cmdclass={'test': PyTest}
)
