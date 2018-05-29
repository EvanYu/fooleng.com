from . import bsd

@bsd.route('/')
def show():
    return "Hello BSD"