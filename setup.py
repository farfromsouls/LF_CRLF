from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='lf-crlf',
  version='0.0.1',
  author='farfromsouls',
  author_email='farfromsouls@gmail.com',
  description='Here you can fast change files/dirs between LF and CRLF',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/farfromsouls/LF_CRLF',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='dir file lf crlf convert',
  project_urls={
    'GitHub': 'https://github.com/farfromsouls/LF_CRLF'
  },
  python_requires='>=3.6'
)