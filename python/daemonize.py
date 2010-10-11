#!/usr/bin/env python
#
#Copyright 2010, Fabien Boucher
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

import sys

from lockfile import LockFile
from daemon import DaemonContext

class OcspDaemon(DaemonContext):
    def __init__(self, redirect_output = '/tmp/ocsp_responder.log',
                 chroot = None,
                 detach = True,
                 pidfile = '/var/run/ocsp_responder.pid'):

        self.redirect_output = file(redirect_output, 'a')
        self.chroot = chroot
        self.detach = detach
        self.pidfile = pidfile
        if self.pidfile:
            self.pidfile = LockFile(pidfile)
        if not self.detach:
            self.redirect_output = sys.stdout

        DaemonContext.__init__(self,
                               stdout = self.redirect_output,
                               stderr = self.redirect_output,
                               detach_process = self.detach,
                               pidfile = self.pidfile)

# Simple test
if __name__ == '__main__':
    from time import sleep

    def main():
        print 'begin to work'
        sleep(30)
        print 'stop to work'

    with OcspDaemon(detach = False, pidfile = None):
        main()
