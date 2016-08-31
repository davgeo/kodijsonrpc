#!/usr/bin/env python3

'''
kodijsonrpc.py

Set up Kodi specific JSON RPC client.

All Kodi JSON methods can be called as functions
to the KodiJSONClient instance.

'''

from jsonrpcclient.http_server import HTTPServer

KODI_JSON_NAMESPACES = ["VideoLibrary",
                        "Settings",
                        "Favourites",
                        "AudioLibrary",
                        "Application",
                        "Player",
                        "Input",
                        "System",
                        "Playlist",
                        "Addons",
                        "AudioLibrary",
                        "Files",
                        "GUI" ,
                        "JSONRPC",
                        "PVR",
                        "xbmc"]

#################################################
#
# KodiNamespaceMethodCatcher
#
# This provides a __getattr__ method which
# catches all method calls and makes the
# corresponding server requests.
#
#################################################
class KodiNamespaceMethodCatcher(object):
  #################################################
  # __init__
  #################################################
  def __init__(self, server, namespace):
    self.server = server
    self.namespace = namespace

  #################################################
  # __getattr__ : catch all function calls
  #################################################
  def __getattr__(self, function):
    def func(*args, **kwargs):
      return self.server.request("{0}.{1}".format(self.namespace, function), *args, **kwargs)
    return func

#################################################
#
# KodiJSONClient
#
# Insantiate KodiNamespaceMethodCatcher classes
# for all Kodi JSON namespaces. This allows any
# of the Kodi JSON methods to be called as methods
# of the KodiJSONClient
#
# e.g <KodiJSONClient object>.JSONRPC.Ping()
# would result in a ping request sent to the
# configured kodi server.
#
#################################################
class KodiJSONClient(object):
  #################################################
  # __init__
  #################################################
  def __init__(self, host, port, user, pwd):
    self.url = 'http://{0}:{1}/'.format(host, port)
    self.server = HTTPServer(self.url + 'jsonrpc', headers={'content-type': 'application/json'}, auth=(user, pwd))
    for namespace in KODI_JSON_NAMESPACES:
      inst = "self.{0} = KodiNamespaceMethodCatcher(self.server, '{0}')".format(namespace)
      exec(inst)

#################################################
#
# EnableJSONLogging
#
# Enable logging on jsconrpcclient module
#
#################################################
def EnableJSONLogging():
  import logging
  logging.getLogger('jsonrpcclient').setLevel(logging.INFO)
  logging.basicConfig()


