import wx
from wxLed import led



class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(500, 325))
        #self.log = log
        #self.Bind(wx.EVT_PAINT, self.OnPaint) # Bind the paint event
        #wx.Panel.__init__(self, parent, -1)
        #self.panel== wx.Panel(self)
        statusList = ['ON', 'OFF']
        colorList = ['RED', 'GREEN', 'BLUE', 'YELLOW']

        self.rb_led1_status = wx.RadioBox(self, label = 'Status', pos = (60,10), choices = statusList,
                               majorDimension = 1, style = wx.RA_SPECIFY_ROWS)        
        self.rb_led1_color = wx.RadioBox(self, label = 'Color', pos = (180,10), choices = colorList,
                               majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox1_S, self.rb_led1_status)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox1_C, self.rb_led1_color)

        status=self.rb_led1_status.GetSelection()
        #print(status)
        color=self.rb_led1_color.GetSelection()
        print("EvtRadioBox_LED1:  Status={} Color={}\n".format(status, color))
        #sig_led1 = led(self,-1,pos=(10,50),size=(50,50), style=wx.TRANSPARENT_WINDOW, color='B')
        self.sig_led1 = led(self,pos=(20,30),size=(30,30), color='B')
        #sig_led2 = led(self,pos=(20,70),size=(25,25), color='G')
        self.sig_led3 = led(self,pos=(20,110),size=(30,30), color='R')
        #sig_led4 = led(self,pos=(20,150),size=(25,25), color='Y')

        if status==0:
            self.sig_led1.SetStatus(True)
        else:
            self.sig_led1.SetStatus(False)

        if color==0:
            self.sig_led1.SetColor('R')
        elif color==1:
            self.sig_led1.SetColor('G')
        elif color==2:
            self.sig_led1.SetColor('B')
        elif color==3:
            self.sig_led1.SetColor('Y')
        else:
            print('choice error')

        self.sig_led3.SetStatus(True)
        self.sig_led3.SetColor('B')
        #sig_led2.SetStatus(True)
        #sig_led2.SetColor('R')
        #sig_led4.SetStatus(True)
        #sig_led4.SetColor('Y')

        self.slider = wx.Slider(
            self, wx.ID_ANY, 25, 10, 50, pos=(180, 110) ,size=(250, -1),
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS
            )
        
        self.slider.SetTickFreq(5)
        self.Bind(wx.EVT_SLIDER, self.EvtSlider, self.slider)

    def EvtRadioBox1_S(self, event):
        print('EvtRadioBox_1: %d\n' % event.GetInt())
        evt_nr = event.GetInt()
        if evt_nr==0:
            self.sig_led1.SetStatus(True)
        else:
            self.sig_led1.SetStatus(False)

    def EvtRadioBox1_C(self, event):
        print('EvtRadioBox_1: %d\n' % event.GetInt())
        evt_nr = event.GetInt()
        if evt_nr==0:
            self.sig_led1.SetColor('R')
        elif evt_nr==1:
            self.sig_led1.SetColor('G')
        elif evt_nr==2:
            self.sig_led1.SetColor('B')
        elif evt_nr==3:
            self.sig_led1.SetColor('Y')
        else:
            print('choice error')
            
    def EvtSlider(self, event):
        print('Slider: %d\n' % event.GetInt())
        self.sig_led3.SetSize(event.GetInt())
        #self.sig_led3.SetClientSize(event.GetInt(),event.GetInt())

# Create the application and run the main loop
app = wx.App()
frame=MyFrame(None, 'Led Demo')
frame.Centre()
frame.Show(True)
app.MainLoop()
