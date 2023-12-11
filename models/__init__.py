#!/usr/bin/python3
"""
This makes the models directory a Python package.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

