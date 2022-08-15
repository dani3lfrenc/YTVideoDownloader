from setuptools import setup

APP = ['YTVideoDownloader.py']
DATA_FILES = ['icon.png','icon.icns']
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'icon.icns',
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps','pytube','pygame_gui'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)