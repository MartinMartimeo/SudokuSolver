#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from flask import render_template, current_app

__author__ = 'Severin Orth <severin.orth@st.ovgu.de>'
__date__ = '14.12.12 - 17:20'


@current_app.route('/')
def index():
    return render_template('index.html')