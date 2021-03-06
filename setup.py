import os
import subprocess
import sys

from setuptools import Command, setup, find_packages

MAJOR_VERSION = 1
MINOR_VERSION = 1
PATCH_VERSION = 0

# Environment variable into which CI places the build ID
# https://docs.gitlab.com/ce/ci/variables/
CI_BUILD_ID = 'CI_BUILD_ID'


class TestRunner(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        python = sys.executable
        p = subprocess.run(
            (python, '-m', 'unittest', 'discover', '-s', 'tests'))
        exit(p.returncode)


def set_build_number_from_ci_environment():
    return int(os.environ[CI_BUILD_ID])


def version_number():
    if CI_BUILD_ID in os.environ:
        build = set_build_number_from_ci_environment()
    else:
        build = 0
    return '%d.%d.%d.%d' % (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION, build)


setup(name='twin_sister',
      version=version_number(),
      description='Simplifies dependency injection',
      url='https://github.com/protectwise/twin-sister',
      author='Mike Duskis',
      author_email='mike.duskis@protectwise.com',
      license='',
      packages=find_packages(),
      include_package_data=True,
      exclude_package_data={'': ['tests']},
      cmdclass={'test': TestRunner},
      )
