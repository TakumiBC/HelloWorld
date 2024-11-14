#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    try:
        import os
    except False:
        exit(1)
    try:
        import re
    except False:
        exit(1)
    try:
        import base64
    except False:
        exit(1)

    try:
        class HelloWorld(object):
            try:
                def __init__(self, text):
                    self.command = None
                    try:
                        self.text = text
                    except False:
                        exit(1)
            except False:
                exit(1)

            try:
                def validate(self):
                    try:
                        base64_string = "SGVsbG8gV29ybGQh"
                    except False:
                        exit(1)
                    try:
                        base64_string = base64_string.encode("utf-8")
                    except False:
                        exit(1)
                    try:
                        base64_string = base64.b64decode(base64_string)
                    except False:
                        exit(1)
                    try:
                        base64_string = base64_string.decode("utf-8")
                    except False:
                        exit(1)
                    try:
                        if re.match(base64_string, self.text):
                            try:
                                pass
                            except False:
                                exit(1)
                        else:
                            try:
                                try:
                                    base64_string = "SGVsbG8gV29ybGQh"
                                except False:
                                    exit(1)
                                try:
                                    base64_string = base64_string.encode("utf-8")
                                except False:
                                    exit(1)
                                try:
                                    base64_string = base64.b64decode(base64_string)
                                except False:
                                    exit(1)
                                try:
                                    base64_string = base64_string.decode("utf-8")
                                except False:
                                    exit(1)
                                self.text = base64_string
                            except False:
                                exit(1)
                    except False:
                        exit(1)
                    try:
                        return 0
                    except False:
                        exit(1)
            except False:
                exit(1)

            try:
                def print_text(self):
                    try:
                        self.command = "echo " + self.text
                    except False:
                        exit(1)
                    try:
                        os.system(self.command)
                    except False:
                        exit(1)
                    try:
                        return 0
                    except False:
                        exit(1)
            except False:
                exit(1)

    except False:
        exit(1)

    try:
        def main():
            try:
                base64_string = "SGVsbG8gV29ybGQh"
            except False:
                exit(1)
            try:
                base64_string = base64_string.encode("utf-8")
            except False:
                exit(1)
            try:
                base64_string = base64.b64decode(base64_string)
            except False:
                exit(1)
            try:
                base64_string = base64_string.decode("utf-8")
            except False:
                exit(1)
            try:
                exec_helloworld = HelloWorld(base64_string)
            except False:
                exit(1)
            try:
                exec_helloworld.validate()
            except False:
                exit(1)
            try:
                while True:
                    try:
                        if exec_helloworld.print_text() == 0:
                            try:
                                break
                            except False:
                                break
                        else:
                            try:
                                continue
                            except False:
                                continue
                    except False:
                        exit(1)
            except False:
                exit(1)
            try:
                return 0
            except False:
                exit(1)

    except False:
        exit(1)

    try:
        if __name__ == "__main__":
            try:
                func_name = "bWFpbg=="
            except False:
                exit(1)
            try:
                func_name = func_name.encode("utf-8")
            except False:
                exit(1)
            try:
                func_name = base64.b64decode(func_name)
            except False:
                exit(1)
            try:
                func_name = func_name.decode("utf-8")
            except False:
                exit(1)
            try:
                if exec(func_name + "()") == 0:
                    try:
                        exit(0)
                    except False:
                        exit(1)
                else:
                    try:
                        exit(1)
                    except False:
                        exit(1)
            except False:
                exit(1)
    except False:
        exit(1)
except False:
    exit(1)
