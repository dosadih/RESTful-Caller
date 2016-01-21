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

import subprocess

class RESTfulCaller(object):

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
        self.namespace = None
        self.version = "v1"

        if serverip is not None:
            self.set_ip(serverip=serverip)
        else:
            self.set_ip("localhost")

        if port is not None:
            self.set_port(port)
        else:
            self.set_port("8080")

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

    def setup(self, cfg):
        """
        Global configuration setter
        """
        if "ip" in cfg:
            self.set_ip(cfg["ip"])

        if "port" in cfg:
            self.set_port(cfg["port"])

        if "version" in cfg:
            self.set_version(cfg["version"])

        if "namespace" in cfg:
            self.set_namespace(cfg["namespace"])

    def set_ip(self, serverip=""):
        """
        IP setter
        """
        if str(serverip[0:3]) is not "http":
            self.serverip = "http://" + str(serverip)
        else:
            self.serverip = str(serverip)
        if self.verbose:
            print "INFO: caller.py: IP is " + str(self.serverip)

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
                print "ERROR: caller.py: IP is wrong. Please set a correct value"
            return 1
        else:
            if self.verbose:
                print "INFO: caller.py: IP is correct"
            return 0

    def set_port(self, port=""):
        """
        port setter
        """
        self.port = str(port)

        if self.verbose:
            print "INFO: caller.py: set port is " + self.port

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
                print "ERROR: caller.py: port is wrong. Please set a correct value"
            return 1
        else:
            if self.verbose:
                print "INFO: caller.py: port is correct"
            return 0

    def set_version(self, version):
        """
        API version setter
        """
        self.version = str(version)

    def get_version(self):
        """
        API version getter
        """
        return self.version

    def set_namespace(self, namespace):
        """
        Service namespace setter
        """
        self.namespace = str(namespace)

    def get_namespace(self):
        """
        Service namepace getter
        """
        return self.namespace

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

        if data is not None:
            call += " -d " + data

        call += str(self.serverip) + ":" + str(self.port) + "/" + str(self.version) + "/" + str(self.namespace) + "/"

        if isinstance(route, basestring):
            if route[0] is "/":
                call += route[1:]
            else:
                call += route
            if self.verbose:
                print "INFO: caller.py: Call done : " + str(call)
            call = call.split(" ")
            proc = subprocess.Popen(call)
            proc.wait()
            (stdout, stderr) = proc.communicate()
            return stdout
        else:
            if self.verbose:
                print "ERROR: caller.py: route is wrong. Please specify it as string"
            return 1

