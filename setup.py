# -*- mode: python ; coding: utf-8 -*-

from setuptools import setup

APP = ['script.py']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'Hello World',
        'CFBundleIdentifier': 'com.example.hello',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)