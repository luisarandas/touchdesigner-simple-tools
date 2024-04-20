
# luisarandas 20-04-2024

import os
import ctypes
import platform
from datetime import datetime

class AttrList(ctypes.Structure):
        _fields_ = [
            ("bitmapcount", ctypes.c_uint16),
            ("reserved", ctypes.c_uint16),
            ("commonattr", ctypes.c_uint32),
            ("volattr", ctypes.c_uint32),
            ("dirattr", ctypes.c_uint32),
            ("fileattr", ctypes.c_uint32),
            ("forkattr", ctypes.c_uint32)
        ]

attr_list = AttrList(bitmapcount=ctypes.sizeof(AttrList),
                         commonattr=0x00000800)  # ATTR_CMN_FLAGS

class AttributeBuffer(ctypes.Structure):
        _fields_ = [
            ("length", ctypes.c_uint32),
            ("flags", ctypes.c_uint32)
        ]


def get_desktop_path():
    return os.path.join(os.path.expanduser('~'), 'Desktop')


def has_hidden_attribute(filepath):    
    if platform.system() == 'Windows':
        try:
            attrs = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))
            assert attrs != -1
            return bool(attrs & 2) # FILE_ATTRIBUTE_HIDDEN
        except (AttributeError, AssertionError):
            return False
    elif platform.system() == 'Darwin': # not tested
        if os.path.basename(filepath).startswith('.'):
            return True
        try:
            from ctypes.util import find_library
            libc = ctypes.CDLL(find_library('c'))
            buffer = AttributeBuffer()
            buffer_size = ctypes.sizeof(buffer)
            result = libc.getattrlist(filepath.encode('utf-8'), ctypes.byref(attr_list), ctypes.byref(buffer), buffer_size, 0)
            if result == 0:  # Success, hidden flag: (UF_HIDDEN = 0x00008000)
                is_hidden = bool(buffer.flags & 0x00008000)
                return is_hidden
        except (AttributeError, AssertionError):
            return False
    else:
        return os.path.basename(filepath).startswith('.')


def scan_directory(table_dat):
    watch_directory = get_desktop_path()
    known_files = {}  # This can persist outside the function if needed repeatedly
    current_files = {}
    for f in os.listdir(watch_directory):
        full_path = os.path.join(watch_directory, f)
        if os.path.isfile(full_path):
            stat = os.stat(full_path)
            current_files[f] = {
                'path': full_path,
                'hidden': has_hidden_attribute(full_path),
                'last_modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'size': stat.st_size
            }
    new_files = {f: info for f, info in current_files.items() if f not in known_files}
    known_files.update(current_files)
    # Sort by size
    sorted_files = sorted(new_files.items(), key=lambda item: item[1]['size'], reverse=True)
    if sorted_files:
        table_dat.clear()
        table_dat.appendRow(["Filename", "Path", "Hidden", "Last Modified", "Size (bytes)"])
        for filename, info in sorted_files:
            table_dat.appendRow([filename, info['path'], str(info['hidden']), info['last_modified'], str(info['size'])])
            print(f"Added new file: {filename}")


scan_directory(op('file_table'))

