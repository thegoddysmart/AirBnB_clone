#!/usr/bin/python3
"""create unique FileStorage instance for our application"""
from models.engine.file_storage import FileStorage

"""Variable storage, instance of FileStorage"""
storage = FileStorage()
storage.reload()

