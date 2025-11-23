import wx
#import time

class led(wx.Window):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TRANSPARENT_WINDOW, color='R', status=False):
        #super(led, self).__init__(parent, id, pos, size, style, color)
        super().__init__(parent, id, pos, size, style)
        
        self.Bind(wx.EVT_PAINT, self.OnPaint) # Bind the paint event
        self.col = color
        self.LedStatus = status
        self.LedSize = size
        #self.SetWindowStyleFlag(wx.TRANSPARENT_WINDOW);
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT);

    def OnPaint(self, event):
        
        # Create a paint device context
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        x1,y1 = self.GetClientSize()
        #x1 = self.LedSize
        #y1 = self.LedSize
        #x1,y1 = wx.Size(self.LedSize)
        #print(x1,y1)
        print(self.LedSize)
        stops = wx.GraphicsGradientStops()

        if self.LedStatus:

            if self.col=='R' or self.col=='r':
                stops.Add(wx.Colour(255,255,255),0.0)
                stops.Add(wx.Colour(255,0,0),1.0)

            elif self.col=='G' or self.col=='g':
                stops.Add(wx.Colour(255,255,255),0.0)
                stops.Add(wx.Colour(0,255,0),1.0)

            elif self.col=='B' or self.col=='b':
                stops.Add(wx.Colour(255,255,255),0.0)
                stops.Add(wx.Colour(0,0,255),1.0)

            elif self.col=='Y' or self.col=='y':
                stops.Add(wx.Colour(255,255,255),0.0)
                stops.Add(wx.Colour(255,255,0),1.0)

            else:
                stops.Add(wx.Colour(0,0,0),0.0)
                stops.Add(wx.Colour(0,0,0),1.0)
        else:
            if self.col=='R' or self.col=='r':        
                stops.Add(wx.Colour(128,0,0),0.0)
                stops.Add(wx.Colour(0,0,0),1.0)

            elif self.col=='G' or self.col=='g':
                stops.Add(wx.Colour(0,128,0),0.0)
                stops.Add(wx.Colour(0,0,0),1.0)

            elif self.col=='B' or self.col=='b':
                stops.Add(wx.Colour(0,0,128),0.0)
                stops.Add(wx.Colour(0,0,0),1.0)

            elif self.col=='Y' or self.col=='y':
                stops.Add(wx.Colour(128,128,0),0.0)
                stops.Add(wx.Colour(0,0,0),1.0)
               
            else:
                stops.Add(wx.Colour(0,0,0),0.0)
                stops.Add(wx.Colour(0,0,0),1.0)

             
        # Draw the elipse: (x_center, y_center, radius)
        pen = wx.Pen(wx.Colour(0, 0, 0), 1,wx.TRANSPARENT) # Black
        gc.SetPen(pen)
        gc.SetBrush(gc.CreateLinearGradientBrush(0,0,x1,x1,wx.Colour(35,35,35),wx.Colour(180,180,180)))
        gc.DrawEllipse(0, 0, x1, x1)

        y1=(2*x1)/3
        x2=x1/6
        y2=x2
        print(int(x1),int(y1),int(x2),int(y2))
        gc.SetBrush(gc.CreateRadialGradientBrush(x1/2,x1/2,x1/2,x1/2,y1/2,stops))
        gc.DrawEllipse(int(x2), int(y2), int(y1),int(y1))

        event.Skip() # Important to allow the event to propagate further if needed


    def SetStatus(self,status):
        self.LedStatus = status
        self.Refresh()


    def SetColor(self, color):
        self.col = color
        self.Refresh()

    def SetSize(self, size):
        #self.LedSize = size
        self.SetClientSize(size,size)
        self.Refresh()


