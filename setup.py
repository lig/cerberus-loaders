import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

install_requires = [
    'cerberus',
]

if sys.version_info < (3, 4):
    install_requires += [
        'pathlib',
    ]

setup(
    name='cerberus-loaders',
    version='0.1dev',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'YaML': ["PyYAML"],
    },
    tests_require=[
        'pytest',
        'tox',
    ],
    cmdclass={'test': Tox},
    author='Serge Matveenko',
    author_email='s@matveenko.ru',
    description=(
        'Cerberus loaders to load Validators from various data formats'
        ' including JSON, YaML and Python Classes'),
    url='https://github.com/lig/cerberus-loaders',
    license='BSD',
)
