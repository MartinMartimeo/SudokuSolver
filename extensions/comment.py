#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from markdown import util
from flask.ext.markdown import Extension
from markdown.inlinepatterns import Pattern

__author__ = 'Severin Orth <severin.orth@st.ovgu.de>'
__date__ = '28.01.13 - 01:12'

class CommentPattern(Pattern):
    """
        Return the span element for this
    """

    def handleMatch(self, m):
        ei = util.etree.Element("span")
        ei.set("class", "hidden-comment")
        return ei


class Comment(Extension):
    """
        Matches abk's like |SAML?
    """

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['ext-comment'] = CommentPattern(r'\[\!.*\!\]')
        md.registerExtension(self)