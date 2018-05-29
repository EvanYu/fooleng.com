#!/usr/bin/env python3
# coding: utf-8


import os
from fooleng import create_app
from flask_script import Manager, Shell


fooleng = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(fooleng)


def make_shell_context():
    return dict(app=fooleng)


manager.add_command("shell", Shell(make_context=make_shell_context()))


if __name__ == '__main__':
    manager.run()
