#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from urlparse import urlparse
from flask import current_app, request

__author__ = 'Severin Orth <severin.orth@st.ovgu.de>'
__date__ = '09.02.13 - 12:04'



@current_app.context_processor
def inject_server():

    isdevelop = False

    server_name = urlparse(request.host_url).netloc
    if server_name.find("localhost") > -1:
        isdevelop = True
    if server_name.find("127.0.0.1") > -1:
        isdevelop = True

    return dict(server_name=server_name, server_develop=isdevelop)
