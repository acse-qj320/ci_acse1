try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='simple_functions',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Sin function with CI.",
      long_descritpion="""Playing with CI. Realize sin function""",
      url='https://github.com/acse-qj320',
      author="Qiuyu Jiang",
      author_email='qj320@imperial.ac.uk',
      packages=['simple_functions'])
