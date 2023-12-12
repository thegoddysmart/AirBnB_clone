#!/usr/bin/python3
"""creates our unique FileStorage instance for our application"""
from models.engine.file_storage import FileStorage

"""our variable storage, instance of FileStorage"""
storage = FileStorage()
storage.reload()

