#!/usr/bin/env python3
"""Create a unique storage instance for the application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
