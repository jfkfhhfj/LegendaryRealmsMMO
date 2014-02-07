#
#
#  The Multiverse Platform is made available under the MIT License.
#
#  Copyright (c) 2012 The Multiverse Foundation
#
#  Permission is hereby granted, free of charge, to any person 
#  obtaining a copy of this software and associated documentation 
#  files (the "Software"), to deal in the Software without restriction, 
#  including without limitation the rights to use, copy, modify, 
#  merge, publish, distribute, sublicense, and/or sell copies 
#  of the Software, and to permit persons to whom the Software 
#  is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be 
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
#  OR OTHER DEALINGS IN THE SOFTWARE.
#
#  

from multiverse.mars import *
from multiverse.mars.objects import *
from multiverse.mars.util import *
from multiverse.server.math import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.util import *
from multiverse.msgsys import *
from multiverse.simpleclient import *
from java.lang import *

loginType = 4

loginResponseHandler = LoginResponseHandler()
SimpleClient.getDispatcher().registerHandler(loginType,
                                             loginResponseHandler)

# set up the login response handler to exit when it gets the msg
# this is useful for a monitoring script
LoginResponseHandler.EXIT_ON_MSG = 1

# start a thread that will exit after 30 seconds
# this is in case the server actually accepts our
# connection, but never sends us a login response
class ExitThread (Runnable):
    def run(self):
        Log.debug("ExitThread: waiting for 30 seconds")
        Thread.sleep(30000)
        Log.error("ExitThread: exited due to no login response")
        System.exit(1)

exitThread = ExitThread()
Thread(exitThread).start()

Log.debug("completed simpleclient.py")
