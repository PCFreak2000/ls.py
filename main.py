import os
from termcolor import cprint

import config

def main():
    folders = []
    files = []

    for element in os.listdir():
        if os.path.isdir(element):
            folders.append(element)
            continue

        files.append(element)

    for folder in folders:
        cprint(folder, "yellow")

    for file in files:
        extension = file.split(".")[-1]
        for color, exts in config.extensions.items():
            if extension in exts:
                cprint(file, color)
                break
            
            else:
                cprint(file, "blue")
                break


if __name__ == "__main__":
    main()