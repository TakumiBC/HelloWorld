#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import os
except:
    exit(1)
try:
    import re
except:
    exit(1)


class HelloWorld(object):
    def __init__(self, text):
        try:
            self.text = text
        except False:
            exit(1)

    def validate(self):
        try:
            if re.match("Hello World!", self.text):
                try:
                    pass
                except:
                    exit(1)
            else:
                try:
                    self.text = "Hello World!"
                except:
                    exit(1)
        except:
            exit(1)
        try:
            return 0
        except:
            exit(1)

    def print_text(self):
        try:
            self.command = "echo " + self.text
        except:
            exit(1)
        try:
            os.system(self.command)
        except:
            exit(1)
        try:
            return 0
        except:
            exit(1)


def main():
    try:
        text = "Hello World!"
    except:
        exit(1)
    try:
        exec_helloworld = HelloWorld(text)
    except:
        exit(1)
    try:
        exec_helloworld.validate()
    except:
        exit(1)
    while True:
        try:
            if exec_helloworld.print_text() == 0:
                try:
                    break
                except:
                    break
            else:
                try:
                    continue
                except:
                    continue
        except:
            exit(1)
    try:
        return 0
    except:
        exit(1)


if __name__ == "__main__":
    try:
        func_name = "main"
    except:
        exit(1)
    try:
        if exec(func_name + "()") == 0:
            try:
                exit(0)
            except:
                exit(1)
        else:
            try:
                exit(1)
            except:
                exit(1)
    except:
        exit(1)
