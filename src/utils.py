from json import load
from os import scandir

from desktop_entry import DesktopEntry


def load_config(path):
    with open(path) as f:
        return load(f)

def iterate_dir(path):
    return [file for file in scandir(path) if file.name.split('.')[-1] == 'desktop']

def parse_info(path):
    with open(path) as f:
        lines = f.readlines()

        info = {}
        info['path'] = path

        for line in lines:
            if line.startswith('Name='):
                info['name'] = line[5:-1]
            elif line.startswith('NoDisplay='):
                display = line[10:]
                if display[-1] == '\n':
                    display = display[:-1]

                info['display'] = display != 'true'
            elif line.startswith('Hidden='):
                info['hidden'] = line[7:-1] == 'true'

        return DesktopEntry(info)