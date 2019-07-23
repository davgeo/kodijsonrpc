#!/usr/bin/env python3
"""kodijsonrpc.py

Set up Kodi specific JSON RPC client.

All Kodi JSON methods can be called as functions
to the KodiJSONClient instance.
"""

from jsonrpcclient.http_server import HTTPServer

KODI_JSON_NAMESPACES = [
    "VideoLibrary", "Settings", "Favourites", "AudioLibrary", "Application",
    "Player", "Input", "System", "Playlist", "Addons", "AudioLibrary", "Files",
    "GUI", "JSONRPC", "PVR", "xbmc"
]


class KodiNamespaceMethodCatcher(object):
    """KodiNamespaceMethodCatcher

    This provides a __getattr__ method which
    catches all method calls and makes the
    corresponding server requests.
    """

    def __init__(self, server, namespace):
        """__init__"""
        self.server = server
        self.namespace = namespace

    def __getattr__(self, function):
        """__getattr__ : catch all function calls"""
        def func(*args, **kwargs):
            return self.server.request(
                "{0}.{1}".format(self.namespace, function), *args, **kwargs)

        return func


class KodiJSONClient(object):
    """KodiJSONClient

    Insantiate KodiNamespaceMethodCatcher classes
    for all Kodi JSON namespaces. This allows any
    of the Kodi JSON methods to be called as methods
    of the KodiJSONClient

    e.g <KodiJSONClient object>.JSONRPC.Ping()
    would result in a ping request sent to the
    configured kodi server.
    """

    def __init__(self, host, port, user, pwd):
        """__init__"""
        self.url = 'http://{0}:{1}/'.format(host, port)
        self.server = HTTPServer(
            self.url + 'jsonrpc',
            headers={'content-type': 'application/json'},
            auth=(user, pwd))
        for namespace in KODI_JSON_NAMESPACES:
            self.__dict__[namespace] = KodiNamespaceMethodCatcher(
                self.server, namespace)


def enable_json_logging():
    """EnableJSONLogging

    Enable logging on jsconrpcclient module
    """
    import logging
    logging.getLogger('jsonrpcclient').setLevel(logging.INFO)
    logging.basicConfig()
