try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Collection of some courses for learning Python',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose', 'flake8'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'PythonBeginner'
}

setup(**config)
