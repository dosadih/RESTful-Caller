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

    def __init__(self, verbose=0, serverip=None, port=None):
        """
        Class constructor
        """
        self.verbose = verbose
        self.serverip = None
        self.port = None

        if serverip is not None:
            self.set_ip(serverip=serverip)
        else:
            self.set_ip("localhost")

        if port is not None:
            self.set_port("8080")
        else:
            self.set_port(port)

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

    def set_ip(self, serverip=""):
        """
        IP setter
        """
        if str(serverip[0:3]) is not "http":
            self.serverip = "http://" + str(serverip)
        else:
            self.serverip = str(serverip)
        if self.verbose:
            print "info - caller.py: IP is " + str(self.serverip)

    def get_ip(self):
        """
        IP getter
        """
        return self.serverip

    def check_ip(self):
        """
        Check IP validity
        """
        if self.serverip is "" or self.serverip is None:
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
        self.port = str(port)

        if self.verbose:
            print "info - caller.py: set port is " + self.port

    def get_port(self):
        """
        port getter
        """
        return self.port

    def check_port(self):
        """
        Check port validitya
        """
        if self.port is "" or self.port is None:
            if self.verbose:
                print "error - caller.py: port is wrong. Please set a correct value"
            return 1
        else:
            if self.verbose:
                print "info - caller.py: port is correct"
            return 0

    def call(self, route="", verb="", data=None):
        """
        Function to make a call
        route defines the service to call
        """

        if self.check_ip():
            return 1

        if self.check_port():
            return 1

        call = "curl -X "

        if verb is "":
            if self.verbose:
                print "warning - caller.py: verb is empty. Use POST as default verb"
            call += "POST "
        else:
            call += verb + " "
            if self.verbose:
                print "warning - caller.py: verb is empty. Use POST as default verb"

        if data is not None:
            call += " -d " + data

        call += str(self.serverip) + ":" + str(self.port) + "/"

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

