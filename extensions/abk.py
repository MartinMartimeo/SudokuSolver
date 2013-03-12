#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from markdown import util
from flask.ext.markdown import Extension
from markdown.inlinepatterns import Pattern

__author__ = 'Severin Orth <severin.orth@st.ovgu.de>'
__date__ = '28.01.13 - 01:12'

abks = {"OvGU": ("Otto-von-Guericke-University Magdeburg", "http://www.ovgu.de/")}


class AbbrevationPattern(Pattern):
    """
        Return the span element for this
    """

    def handleMatch(self, m):
        # Text
        t = m.group(2)

        # Tipsy
        if isinstance(abks[t], tuple):
            ei = util.etree.Element("a")
            ei.set("tipsy", abks[t][0])
            ei.set("href", abks[t][1])
        else:
            ei = util.etree.Element("i")
            ei.set("tipsy", abks[t])
        ei.set("class", "abk-tipp")
        ei.text = t

        return ei


class Abbrevation(Extension):
    """
        Matches abk's like |SAML?
    """

    def extendMarkdown(self, md, md_globals):
        for abk in abks.keys():
             md.inlinePatterns['ext-abbrevation-%s' % abk] = AbbrevationPattern(r'(%s)(?:\?\!)?' % abk)
        md.registerExtension(self)