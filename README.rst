kodijsonrpc
==================

This provides a Kodi JSON-RPC client. All Kodi JSON methods can be
called as methods to the KodiJSONClient instance.

Usage
-------
This is an example given a kodi server at 192.168.0.1, using port 8000 (username='user1', password='pwd'):

.. code:: python

  server = KodiJSONClient('192.168.0.1', '8000', 'user1', 'pwd')
  server.JSONRPC.Ping()

All other Kodi JSON methods can be called in a similar way, with parameters provides as appropriate.

e.g. This would provide movie details:

.. code:: python

  params = {'properties':['title',
                          'lastplayed',
                          'thumbnail',
                          'plot',
                          'playcount',
                          'resume',
                          'file']}
  movies = server.VideoLibrary.GetMovies(params)

Requirements
---------------
This is a python package and requires the following:

- Python 3.4+
- Python jsonrpcclient package
- Python requests package

And of course to have a purpose a Kodi instance is required:

- Kodi v13 or later

Installation
---------------
Install using pip:

.. code-block:: bash

    $ pip install kodijsonrpc

Requests, Issues, Bugs or Suggestions
---------------------------------------------
Add any feature requests, issues, bugs or suggestions here: https://github.com/davgeo/kodijsonrpc/issues

Please give as much detail as possible.
