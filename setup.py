"""
Setup.py for my song picker package
"""
from setuptools import setup, find_packages  # Always prefer setuptools over distutils

setup(
    name="song_picker",
    version="1.0.0",
    description="Really awesome library for choosing songs",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ], 
    py_modules=["song_picker"],
    scripts=["pick-songs"],
)
    
