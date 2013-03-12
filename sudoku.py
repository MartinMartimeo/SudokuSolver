#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
    Flask Main Entry Point
"""
import os

from flask import Flask

# Init Flask
app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

# Init Markdown
from flaskext.markdown import Markdown
md = Markdown(app)

# Extensions
from extensions.abk import Abbrevation
md.register_extension(Abbrevation)
from extensions.comment import Comment
md.register_extension(Comment)
from extensions.linebreak import LineBreak
md.register_extension(LineBreak)

with app.app_context():

    # noinspection PyUnresolvedReferences
    from processors import *
    # noinspection PyUnresolvedReferences
    from handlers import *

    app.md = md

# Get extra files
basename = os.path.dirname(__file__)
extra_files = [os.path.join(basename, x) for x in ["processors", "static/content", "static/js"]]

if __name__ == '__main__':
    app.run(extra_files=extra_files)
