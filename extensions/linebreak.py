#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from flask.ext.markdown import Extension
from markdown.inlinepatterns import SubstituteTagPattern

__author__ = 'Severin Orth <severin.orth@st.ovgu.de>'
__date__ = '28.01.13 - 01:02'


class LineBreak(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['ext-linebreak'] = SubstituteTagPattern(r'~\n', 'br')
        md.registerExtension(self)