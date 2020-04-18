try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Instagram bot for increasing engagement',
    'author': 'Anghel Adrian',
    'url': 'Not Yet',
    'download_url': 'Not yet',
    'author_email': 'greuceanu98@gmail.com',
    'version': '0.1',
    'install_requires': ['selenium', 'pandas'],
    'packages': ['instabot', 'bot'],
    'scripts': [],
    'name': 'instabot'
}

setup(**config)