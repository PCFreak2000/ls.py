import sys
import os
from termcolor import cprint

import config

def main(args):
    path = args[1] if len(args) > 1 else "."
    folders = []
    files = []
    links = []

    for element in os.listdir(path):
        absolute_path = os.path.join(path, element)

        if os.path.isdir(absolute_path):
            folders.append(element)
            continue
            
        files.append(element)

    for folder in folders:
        cprint(folder, "yellow")

    highlighted = []

    for file in files:
        extension = file.split(".")[-1]

        if extension == "lnk":
            links.append(file)

        for color, exts in config.extensions.items():
            if extension in exts:
                highlighted.append((file, color))
                break
            
    for link in links:
        cprint(link, "red")
        files.remove(link)

    for file, color in highlighted:
        cprint(file, color)
        files.remove(file)
        
    for file in files:
        cprint(file, "blue")

if __name__ == "__main__":
    main(sys.argv)