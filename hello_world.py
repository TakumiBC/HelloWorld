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
try:
    import base64
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
            base64_string = "SGVsbG8gV29ybGQh"
        except:
            exit(1)
        try:
            base64_string = base64_string.encode("utf-8")
        except:
            exit(1)
        try:
            base64_string = base64.b64decode(base64_string)
        except:
            exit(1)
        try:
            base64_string = base64_string.decode("utf-8")
        except:
            exit(1)
        try:
            if re.match(base64_string, self.text):
                try:
                    pass
                except:
                    exit(1)
            else:
                try:
                    try:
                        base64_string = "SGVsbG8gV29ybGQh"
                    except:
                        exit(1)
                    try:
                        base64_string = base64_string.encode("utf-8")
                    except:
                        exit(1)
                    try:
                        base64_string = base64.b64decode(base64_string)
                    except:
                        exit(1)
                    try:
                        base64_string = base64_string.decode("utf-8")
                    except:
                        exit(1)
                    self.text = base64_string
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
        base64_string = "SGVsbG8gV29ybGQh"
    except:
        exit(1)
    try:
        base64_string = base64_string.encode("utf-8")
    except:
        exit(1)
    try:
        base64_string = base64.b64decode(base64_string)
    except:
        exit(1)
    try:
        base64_string = base64_string.decode("utf-8")
    except:
        exit(1)
    try:
        exec_helloworld = HelloWorld(base64_string)
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
        func_name = "bWFpbg=="
    except:
        exit(1)
    try:
        func_name = func_name.encode("utf-8")
    except:
        exit(1)
    try:
        func_name = base64.b64decode(func_name)
    except:
        exit(1)
    try:
        func_name = func_name.decode("utf-8")
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
