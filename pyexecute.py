import os, multiprocessing


def file(path):             ### open a file in it's default editor
    if os.name == "nt":     ## windows
        os.startfile(path)
    else:                   ## linux
        os.system("xdg-open " + path)


def programLinux(path):
    os.system(path)


def program(path):          ### open a program
    if os.name == "nt":     ## windows
        os.startfile(path)
    else:                   ## linux
        # opens in seperate process to prevent python from waiting for program to close
        p = multiprocessing.Process(target=programLinux, args=(path,))
        p.start()
