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

package multiverse.server.events;

import multiverse.server.engine.*;
import multiverse.server.objects.*;
import multiverse.server.network.*;

/**
 * this event contains information about the ambient light.
 * the server usually sends this event to the user when they log in
 * in the loginhandler.
 * it doesnt have an entity_id associated with it because
 * its general information about the world
 */
public class AmbientLightEvent extends Event {
    public AmbientLightEvent() {
	super();
    }

    public AmbientLightEvent(MVByteBuffer buf, ClientConnection con) {
	super(buf,con);
    }

    public AmbientLightEvent(Color color) {
	super();
	setAmbientLight(color);
    }

    public void setAmbientLight(Color color) {
	this.color = color;
    }
    public Color getAmbientLight() {
	return color;
    }

    public MVByteBuffer toBytes() {
	int msgId = Engine.getEventServer().getEventID(this.getClass());
	MVByteBuffer buf = new MVByteBuffer(20);
	buf.putLong(0); 
	buf.putInt(msgId);
	buf.putColor(getAmbientLight());
	buf.flip();
	return buf;
    }

    protected void parseBytes(MVByteBuffer buf) {
	buf.rewind();
	buf.getLong(); // ignore
	/* int msgId = */ buf.getInt();
	setAmbientLight(buf.getColor());
    }

    public String getName() {
	return "AmbientLightEvent";
    }

    private Color color = null;
}
