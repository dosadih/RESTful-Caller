#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# bug in pylint leading to unfound some arguments of a function
# pylint: disable=E1120 
# line too long
# pylint: disable=C0301
# too many lines in module
# pylint: disable=C0302

"""
Class to make call to micro service
"""

import os

class Caller(object):
    
    """
    Class to make call to web service
    """

    def __init__(self, verbose=0):
        """
        Class constructor
        """
        self.verbose = verbose
        self.ip = "localhost" 
        self.port = "8080"
        self.verb = "POST"
    
    def verbose_setter(self, verbose=0):
        """
        verbose mode setter
        """
        self.verbose = verbose

    def verbose_getter(self, verbose=0):
        """
        verbose mode getter
        """
        return self.verbose
        
    def ip_setter(self, ip=""):
        """
        IP setter
        """
        if type(ip) is string:
            
            if ip[0:3] is not "http":
                self.ip = "http://" + ip
            else:
                self.ip = ip

    def ip_getter(self):
        """
        IP getter
        """
        return self.ip

    def port_setter(self, port=""):
        """
        port setter
        """
        if type(port) is not string:
            self.port = str(port)
        else:
            self.port = port

    def port_getter(self):
        """
        port getter
        """
        return self.port

    def verb_setter(self, verb):
        """
        port setter
        """
        self.verb = verb

    def verb_getter(self):
        """
        port getter
        """
        return self.verb

    def call_route(self, route="", verb=""):
        """
        Function to make a call
        route defines the service to call
        """
        
        call = "curl -X "  
        
        if self.ip is "":
            if self.verbose:
                print "caller.py: IP is wrong. Please set a correct value"
            return 1

        if self.port is "":
            if self.verbose:
                print "caller.py: port is wrong. Please set a correct value"
            return 1
            
        if type(verb) is string:
            if verb is not "":
                if self.verbose:
                    print "caller.py: verb is empty. Use POST as default verb"
                call += verb + " "
        
        call += self.ip + ":" + self.port + "/"

        if type(route) is string:
            if route[0] is "/":
                call += route[1:]  
            else:
                call += route
            if self.verbose:
                print "caller.py: Call done : " + str(call)
            os.system(call)
            return 0
        else:
            if self.verbose:
                print "caller.py: route is wrong. Please specify it as string"
            return 1

