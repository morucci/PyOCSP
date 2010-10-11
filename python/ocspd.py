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

from optparse import OptionParser
from ocspserver import OCSPServer
from daemonize import OCSPDaemon
from config import ConfigObject

version = 0.1

usage = "pyocspd %s - Python OCSP Resonder - Based on OpenCA's OCSP Responder\
\n(c) 2010 by Olivier Hervieu\n" % version


def _parse_config(config_file):

    return ConfigObject(config_file)


def _main_loop(config_object):

    def _keep_running():
        # TODO : implement
        return True

    server = OCSPServer(config_object.bind_addr,
                        config_object.bind_port)
    while _keep_running():
        server.handle_request()


def _init_parser():
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--daemon",
                      help="Daemon, detach from current console")
    #parser.add_option("-r", "--chroot",
    #                  help="Directory where to jail the process")
    parser.add_option("-p", "--port", default=2560,
                      help="Start listening on port (default: 2560)")
    parser.add_option("-b", "--bind", default="*",
                      help="Binds to ip (default: *)")
    parser.add_option("-c", "--config",
                      help="A Configuration File")
    #parser.add_option("-m", "--digest",
    #                  help="Set digest to be used (default : md5)")
    #parser.add_option("-k", "--password_key",
    #                  help="Password that protect the private key")
    parser.add_option("-d", "--debug",
                      help="Turns on usefull information")

    return parser


def main():
    parser = _init_parser()

    options, args = parser.parse_args()

    # Error Handling
    if not options.config:
        print "Please provide a configuration file"
    else:
        cfg = _parse_config(options.config)

        if options.daemon:
            with OCSPDaemon():
                __main_loop(cfg)
        else:
            _main_loop(cfg)
