#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import logging
import os
from subprocess import Popen, PIPE
from flask import request

__author__ = 'Severin Orth <severin.orth@nicta.com.au>'
__date__ = '12.03.13 - 17:02'


def build_asserts():
    """
        Builds the list of additional asserts for our yices run
    """

    rtn = []

    for x in range(1, 10, 1):
        for y in range(1, 10, 1):
            n = request.args.get('x%u%u' % (x, y), 0, type=int)
            if n:
                rtn.append("(assert (= x%u%u %u))" % (x, y, n))

    return rtn


def build_input(asserts):
    """
        Get the input we give yices
        :param asserts: List of asserts that will be added to model
    """

    # Get content of file
    ysfile = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "static", "yices", "sudoku.ys"))
    with open(ysfile) as f:
        content = f.read()

    # Replace additional asserts
    content = content.replace("#!REQ###", "\n".join(asserts))

    return content


def run_yices(input):
    """
        Run Yices
    """

    # Open Process
    p = Popen(["yices"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # Write Input
    p.stdin.write(input)
    p.stdin.close()

    # Get Error
    while True:
        line = p.stderr.readline()
        if not line:
            break
        line = line.replace("yices>", "").strip()
        if line:
            logging.error(line)

    # Get Output
    output = p.stdout.read()
    return output


def yices_solve(asserts):
    """
        Runs Yices and parses the output
    """

    rtn = {}

    # Run Yices
    input = build_input(asserts)
    output = run_yices(input)

    # Check Output
    lines = output.split("\n")
    for line in lines:

        if line.endswith("unsat"):
            return False

        if line.find("(= x") > -1 and line.endswith(")"):
            pos = line.find("(= x")

            field = line[pos + 4:pos + 6]
            num = line[pos + 7]

            rtn[field] = num

    return rtn


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

    print "%s" % yices_solve(["(assert (= x11 2))", "(assert (= x33 3))"])