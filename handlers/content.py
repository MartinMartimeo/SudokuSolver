#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Serves a file from static/content in modal template
"""
import os
from flask import render_template, request, current_app
from werkzeug.exceptions import abort

__author__ = 'Severin Orth <severin.orth@st.ovgu.de>'
__date__ = '18.12.12 - 13:57'

@current_app.route('/content/<path>')
def show_content(path):
    """
     Shows a content file
    :param path:
    """

    # Get Path and sane it
    base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    file_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "static", "content", path))
    if not file_path.startswith(base_path):
        abort(403)
        return

    # The name
    name = path.rsplit(".", 1)[0]

    # Print Content
    with open(file_path) as f:
        content = f.read()
        if not request.is_xhr:
            return render_template('layout.html', body=content)
        else:
            return render_template('modal.html', body=content, name=name)



