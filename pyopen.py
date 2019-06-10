import os

def file(path): # open a file in it's default editor
    if os.name == "nt": # windows
        os.startfile(content)
    else:               # linux
        os.system("xdg-open " + path)


def program(path):  # open a program
    if os.name == "nt": # windows
        os.startfile(content)
    else:               # linux
        os.system(path)
