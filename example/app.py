#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bug in pylint leading to unfound some arguments of a function
# pylint: disable=E1120
# line too long
# pylint: disable=C0301
# too many lines in module
# pylint: disable=C0302

import os, sys
import argparse

sys.path.append("./src")

from caller import Caller

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description='Options to access micro service')

    PARSER.add_argument('--service', dest='service', help='service to access')
    PARSER.add_argument('--job', dest='job', help='job to report')
    PARSER.add_argument('--status', dest='status', help='job status to report')

    args = PARSER.parse_args()

    APP = Caller(verbose=1, serverip="localhost", port="8080")
    APP.set_verbose(1)
    APP.set_ip(serverip="localhost")
    APP.set_port(port="8080")

    if "create" in args.service:
        ROUTE = "create/" + str(args.job)
        APP.call(route=ROUTE, verb="POST", data=None)

    elif "delete" in args.service:
        ROUTE = "delete/" + str(args.job)
        APP.call(route=ROUTE, verb="DELETE", data=None)

    elif "search" in args.service:
        ROUTE = "search/" + str(args.job)
        APP.call(route=ROUTE, verb="GET", data=None)

    elif "report" in args.service:
        ROUTE = "report/" + str(args.job) + "/" + str(args.status)
        APP.call(route=ROUTE, verb="PUT", data=None)

    elif "dump" in args.service:
        ROUTE = "dump"
        APP.call(route=ROUTE, verb="GET", data=None)

    else:
        APP.call(route="/dashboard", verb="GET", data=None)
