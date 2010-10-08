============
PyOCSP
============

General Description
======================

PyOCSP is a based on the idea of OpenCA's OCSP Responder released under the
OpenCA Licence.

The purpose of PyOCSP is to provide a rfc2560 compliant OCSP responder.

To try PyOCSP::

    $ pyocspd --help


Install
==========

As for every python package, just run::

    $ python setup.py install

Status
=======

OCSP is in early stage of development. Don't blame me with it doesn't work.

Python Compatibility and Dependencies
=====================================

PyOCSP is developped under python2.6 but must be compatible with > 2.5 python
versions.

The following python package are needed to run pyocsp:

* pyasn1 : http://pypi.python.org/pypi/pyasn1/0.0.11a

Licencing
===========

OCSP is released under GPL Licence.

References
===========

OCSP with OPENSSL
-----------------

* Certificate verification with openssl : http://backreference.org/2010/05/09/ocsp-verification-with-openssl/

RFCs
----

* RFC 2560 : http://www.ietf.org/rfc/rfc2560.txt
* RFC 4557 : http://www.ietf.org/rfc/rfc4557.txt
* RFC 5019 : http://www.ietf.org/rfc/rfc5019.txt

Other OCSP Responder
--------------------

* OpenCA OCSP Responder : http://www.openca.org/projects/ocspd/
