from distutils.core import setup

setup(
    name = 'anhsetup',
    pakages = 'anhsetup',
    version = 'anhsetup',
    long_description = open("egg.txt").read(),
    licence = 'anhsetup', requires=['numpy', 'matplotlib']
)