#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# bug in pylint leading to unfound some arguments of a function
# pylint: disable=E1120 
# line too long
# pylint: disable=C0301
# too many lines in module
# pylint: disable=C0302

import os, sys

sys.path.append("./src")

from caller import Caller

if __name__ == '__main__':

    APP = Caller(verbose=1, serverip="localhost", port="8080")
    APP.set_verbose(1)
    APP.set_ip(serverip="localhost")
    APP.set_port(port="8080")
    APP.call(route="/dashboard", verb="GET", data=None)
    APP.call(route="/help", verb="GET", data=None)
