/********************************************************************

The Multiverse Platform is made available under the MIT License.

Copyright (c) 2012 The Multiverse Foundation

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.

*********************************************************************/

package multiverse.tests.marshallingtests;

import multiverse.server.network.*;

public class TestClass3 extends TestClass2 {

    public TestClass1 mytc1;
    
    public void marshalObject(MVByteBuffer buf) {
        super.marshalObject(buf);
        byte flags = 0;
        if (mytc1 != null)
            flags |= (byte)1;
        buf.putByte(flags);
        if (mytc1 != null)
            mytc1.marshalObject(buf);
    }
        
    public Object unmarshalObject(MVByteBuffer buf) {
        super.unmarshalObject(buf);
        byte flags = buf.getByte();
        if ((flags & 1) != 0) {
            TestClass1 tmp = new TestClass1();
            mytc1 = (TestClass1)tmp.unmarshalObject(buf);
        }
        return this;
    }
}
