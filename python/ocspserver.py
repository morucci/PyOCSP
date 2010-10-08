#!/usr/bin/env python
#
#Copyright 2010, Olivier Hervieu
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the-
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

from pyasn1.codec.der import decoder

OCSP_REQ_TYPE = 'application/ocsp-request'
OCSP_REP_TYPE = 'application/ocsp-response'


def OCSPServer(bind_address, port):
    return HTTPServer((bind_address, port), OCSPRequestHandler)


class OCSPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self, *args, **kwargs):
        self.log_message("Command: %s Path: %s Headers: %r"
                         % (self.command, self.path, self.headers.items()))
        if 'content-type' in self.headers:
            app_type = self.headers['content-type']
        else:
            app_type = None
        if 'content-length' in self.headers and app_type == OCSP_REQ_TYPE:
            length = int(self.headers['content-length'])
            ocsp_request = self.rfile.read(length)
            ocsp_request = decoder.decode(ocsp_request)
            # TODO: parse and read the ocsp request
            pass

        # TODO: Forge an ASN.1 response
        self.send_response(200)
