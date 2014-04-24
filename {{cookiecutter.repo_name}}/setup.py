from setuptools import setup, find_packages

version = '{{cookiecutter.version}}'

install_requires = []
install_requires.append('ordereddict')

setup(name='{{cookiecutter.repo_name}}',
      version=version,
      description="{{cookiecutter.description}}",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='{{cookiecutter.author}}',
      author_email='{{cookiecutter.email}}',
      url='',
      license='',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      install_requires=install_requires,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      slimerjs=scripts:slimerjs
      bower-dev=jstools:bower
      """,
      )
