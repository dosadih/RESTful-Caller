#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bug in pylint leading to unfound some arguments of a function
# pylint: disable=E1120
# line too long
# pylint: disable=C0301
# too many lines in module
# pylint: disable=C0302

"""
Class to make call to micro-service
"""

import os

class Caller(object):

    """
    Class to make call to web service
    """

    def __init__(self, verbose=0, ip="", port=""):
        """
        Class constructor
        """
        self.verbose = verbose
        self.ip = None
        self.port = None
        self.verb = None

        if ip is "":
            self.set_ip(ip)
        else:
            self.set_ip("localhost")

        if port is "":
            self.set_port("8080")
        else:
            self.set_port(port)

        self.set_verb(verb="POST")
        self.data = ""

    def set_verbose(self, verbose=0):
        """
        verbose mode setter
        """
        self.verbose = verbose

    def get_verbose(self):
        """
        verbose mode getter
        """
        return self.verbose

    def set_ip(self, ip=""):
        """
        IP setter
        """
        if type(ip) is basestring:
            if ip[0:3] is not "http":
                self.ip = "http://" + ip
            else:
                self.ip = ip

    def get_ip(self):
        """
        IP getter
        """
        return self.ip

    def check_ip(self):
        """
        Check IP validity
        """
        if self.ip is "":
            if self.verbose:
                print "error - caller.py: IP is wrong. Please set a correct value"
            return 1
        else:
            if self.verbose:
                print "info - caller.py: IP is correct"
            return 0

    def set_port(self, port=""):
        """
        port setter
        """
        if type(port) is not basestring:
            self.port = str(port)
        else:
            self.port = port

    def get_port(self):
        """
        port getter
        """
        return self.port

    def check_port(self):
        """
        Check port validitya
        """
        if self.port is "":
            if self.verbose:
                print "error - caller.py: port is wrong. Please set a correct value"
            return 1
        else:
            if self.verbose:
                print "info - caller.py: port is correct"
            return 0

    def set_data(self, data=""):
        """
        port setter
        """
        self.data = data

    def get_data(self):
        """
        port getter
        """
        return self.data

    def set_verb(self, verb):
        """
        port setter
        """
        self.verb = verb

    def get_verb(self):
        """
        port getter
        """
        return self.verb

    def call_route(self, route="", verb="", data=None):
        """
        Function to make a call
        route defines the service to call
        """

        call = "curl -X "

        if self.check_ip():
            return 1

        if self.check_port():
            return 1

        if isinstance(verb, basestring):
            if verb is "" and self.verb is None:
                if self.verbose:
                    print "warning - caller.py: verb is empty. Use POST as default verb"
                call += " POST "
            else:
                if self.verb is not None:
                    call += self.verb + " "
                else:
                    call += " POST "
                    if self.verbose:
                        print "warning - caller.py: verb is empty. Use POST as default verb"

        call += self.ip + ":" + self.port + "/"

        if self.data is not "" or self.data is not None:
            call += " -d " + self.data

        elif data is not None:
            call += " -d " + data

        if isinstance(route, basestring):
            if route[0] is "/":
                call += route[1:]
            else:
                call += route
            if self.verbose:
                print "info - caller.py: Call done : " + str(call)
            os.system(call)
            return 0
        else:
            if self.verbose:
                print "error - caller.py: route is wrong. Please specify it as string"
            return 1

