.. image:: https://img.shields.io/badge/build-passing-green.svg
    :target: https://github.com/ninjatrench/GoDebian_api
.. image:: https://img.shields.io/badge/version-dev-green.svg
    :target:https://github.com/ninjatrench/GoDebian_api
.. image:: https://img.shields.io/badge/with%20love%20from-india-ff69b4.svg
    :alt: Make In India <3


Features
--------

- Consume deb.li and go.debian.net API | URL shoretening service
- Check for IP whitelist for this service
- Add new URL against randomly generated key
- Add static URL against pre-defined KEY
- Get existing URL via KEY
- Generate preview URL
- Pure Python Module
- Works with Python 2.6+ and 3.2+
- No dependencies


Documentation and Wiki
-------------
Python client for go.debian.net and deb.li URL shortening service

Full documentation is available at https://wiki.debian.org/deb.li

Usage Examples
--------------

.. code-block:: pycon

    >>> import GoDebian
    >>> a = GoDebian.GoDebianApi()

    >>> a.add_url("http://www.debian.org")
    'http://go.debian.net/3xEIl'

    >>> a.get_url("3xEIl")
    'http://www.debian.org'

    >>> a.get_preview_url("3xEIl")
    'http://go.debian.net/p/3xEIl'

    >>> a.add_static_url("http://harshdaftary.com", "harsh")
    'http://go.debian.net/harsh'

    >>>a.get_url("harsh")
    'http://harshdaftary.com'
