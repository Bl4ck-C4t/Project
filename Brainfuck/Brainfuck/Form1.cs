using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;


namespace Brainfuck
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        OpenFileDialog ofd = new OpenFileDialog();

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }
        
        private void button2_Click(object sender, EventArgs e)
        {
            ofd.Filter = "BF|*.txt;*.bf";
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                StreamReader str = new StreamReader(ofd.OpenFile());
                Input_box.Text = str.ReadToEnd();
                string info = Input_box.Text;
                info = info.Replace("\n", "");
                Input_box.Text = info;
                str.Dispose();
                if (info.Contains(','))
                {
                    MessageBox.Show("This program requires input.\nEnter it in the input field");
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string info = Input_box.Text;
            List<int> ind = new List<int>();
            ind.Add(0);
            int curr = 0;
            int point = 0;
            string str = "";
            int str_ind = 0;
            int loop_start = 0;
            int loop_end = 0;
            string asd = "";
            char x;
            try {
                while (point < info.Length)
                {
                    x = info[point];
                    if (x == '+')
                    {
                        ind[curr]++;
                    }
                    else if (x == '-')
                    {
                        ind[curr]--;
                        if (ind[curr] < 0)
                        {
                            ind[curr] = 0;
                        }
                    }
                    else if (x == '>')
                    {
                        curr++;
                        if (curr == ind.Count)
                        {
                            ind.Add(0);
                        }
                    }
                    else if (x == '<')
                    {
                        curr--;
                        if (curr < 0)
                        {
                            curr = 0;
                            ind.Insert(0, 0);
                        }

                    }
                    else if (x == '.')
                    {
                        asd += (char)ind[curr];
                    }
                    else if (x == ',')
                    {
                        if (str == "")
                        {
                          
                            str = Input.Text;

                        }
                        if (str_ind == str.Length)
                        {
                            ind[curr] = 0;
                        }
                        else
                        {
                            ind[curr] = str[str_ind];
                            str_ind++;
                        }
                    }
                    else if (x == '^')
                    {
                        ind[curr] = Convert.ToInt32(Input.Text);
                    }
                    else if (x == '[')
                    {
                        loop_start = point;
                        loop_end = point + info.Substring(point).IndexOf("]");
                        if (ind[curr] == 0)
                        {
                            point = loop_end;
                        }
                    }
                    else if (x == ']')
                    {
                        if (ind[curr] != 0)
                        {
                            point = loop_start;
                        }
                    }
                    else if (x == '*')
                    {
                        ind[curr] *= 2;
                    }
                    else if (x == '/')
                    {
                        asd += Convert.ToString(ind[curr]);
                    }
                    else if (x == '!')
                    {
                        ind[curr] = 0;
                    }
                    point++;
                }
                output_box.Text = asd;
            }
            catch
            {
                MessageBox.Show("There was an Error");
            }

        }
    }
}
