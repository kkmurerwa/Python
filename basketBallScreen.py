import wx

class LeftPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.text = '0'
        self.teams = wx.StaticText(self, -1, 'Team 1', (50, 10))
        self.text = wx.StaticText(self, -1, '0', (70, 60))
        button1 = wx.Button(self, -1, '3 Pointer', (30, 110))
        button2 = wx.Button(self, -1, '2 Pointer', (30, 160))
        button3 = wx.Button(self, -1, 'Free Throw', (30, 210))
        button4 = wx.Button(self, -1, 'Reset', (30, 260))
        self.Bind(wx.EVT_BUTTON, self.onePointer, id=button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.twoPointer, id=button2.GetId())
        self.Bind(wx.EVT_BUTTON, self.freeThrow, id=button3.GetId())
        self.Bind(wx.EVT_BUTTON, self.confirm, id=button4.GetId())

    def onePointer(self, event):
        value = int(self.text.GetLabel())
        value = value + 3
        self.text.SetLabel(str(value))

    def twoPointer(self, event):
        value = int(self.text.GetLabel())
        value = value + 2
        self.text.SetLabel(str(value))

    def freeThrow(self, event):
        value = int(self.text.GetLabel())
        value = value + 1
        self.text.SetLabel(str(value))

    def confirm(self, event):
        conf = wx.MessageBox("Are you sure you want to reset the score?","Confirm Dialog")
        if (conf==4):
            self.reset(event);

    def reset(self, event):
        value = int(self.text.GetLabel())
        value = 0
        self.text.SetLabel(str(value))

class RightPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.text = '0'
        self.teams = wx.StaticText(self, -1, 'Team 2', (50, 10))
        self.text = wx.StaticText(self, -1, '0', (70, 60))
        button1 = wx.Button(self, -1, '3 Pointer', (30, 110))
        button2 = wx.Button(self, -1, '2 Pointer', (30, 160))
        button3 = wx.Button(self, -1, 'Free Throw', (30, 210))
        button4 = wx.Button(self, -1, 'Reset', (30, 260))
        self.Bind(wx.EVT_BUTTON, self.onePointer, id=button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.twoPointer, id=button2.GetId())
        self.Bind(wx.EVT_BUTTON, self.freeThrow, id=button3.GetId())
        self.Bind(wx.EVT_BUTTON, self.confirm, id=button4.GetId())

    def onePointer(self, event):
        value = int(self.text.GetLabel())
        value = value + 3
        self.text.SetLabel(str(value))

    def twoPointer(self, event):
        value = int(self.text.GetLabel())
        value = value + 2
        self.text.SetLabel(str(value))

    def freeThrow(self, event):
        value = int(self.text.GetLabel())
        value = value + 1
        self.text.SetLabel(str(value))

    def confirm(self, event):
        conf = wx.MessageBox("Are you sure you want to reset the score?","Confirm Dialog")
        if (conf==4):
            self.reset(event);

    def reset(self, event):
        value = int(self.text.GetLabel())
        value = 0
        self.text.SetLabel(str(value))

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 400))
        panel = wx.Panel(self, -1)
        self.rightPanel = RightPanel(panel, -1)
        leftPanel = LeftPanel(panel, -1)
        hbox = wx.BoxSizer()
        hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(hbox)
        self.Centre()
        self.Show(True)

app = wx.App()
MainFrame(None, -1, 'widgets communicate')
app.MainLoop()
exit()