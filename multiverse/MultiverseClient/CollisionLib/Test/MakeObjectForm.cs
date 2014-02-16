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

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Axiom.MathLib;
using Multiverse.CollisionLib;

namespace CollisionLibTest
{
    public partial class MakeObjectForm : Form
    {
        public MakeObjectForm()
        {
            InitializeComponent();
        }

        private void MakePanelsInvisible()
        {
            SpherePanel.Visible = false;
            CapsulePanel.Visible = false;
            AABBPanel.Visible = false;
            OBBPanel.Visible = false;
        }
        
        
        private void MakeObjectForm_Load(object sender, EventArgs e)
        {
            MakePanelsInvisible();
        }

        private void ShapeTypeComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            MakePanelsInvisible();
            switch ((ShapeEnum)ShapeTypeComboBox.SelectedIndex)
            {
            case ShapeEnum.ShapeSphere:
                SpherePanel.Visible = true;
                break;
            case ShapeEnum.ShapeCapsule:
                CapsulePanel.Visible = true;
                break;
            case ShapeEnum.ShapeAABB:
                AABBPanel.Visible = true;
                break;
            case ShapeEnum.ShapeOBB:
                OBBPanel.Visible = true;
                break;

            }
        }

        private void AddObjectButton_Click(object sender, EventArgs e)
        {
            // Add the specified object
        }
    }
}
