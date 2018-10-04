import wx

class WxClass(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id, title="wxPython Frame",size=(300,200))
#The elements below add a menu bar element "File" with the item "Quit"
        menubar = wx.MenuBar()
        file = wx.Menu()

        fileMenuItem = wx.MenuItem(file,-1,"Quit\tCTRL+Q")#The item after the \t specifies a shortcut
        file.Append(fileMenuItem)
        menubar.Append(file, '&File')

        self.Bind(wx.EVT_MENU, self.eventI,id=-1)

        edit = wx.Menu()
        really = wx.MenuItem(edit,"Maximize\tCTRL+E",id=-2)
        edit.Append(really)
        menubar.Append(edit,"&Edit")
        self.Bind(wx.EVT_MENU, self.message, id=-2)

        self.SetMenuBar(menubar)

        self.Center()
        self.Show(True)

    def eventI(self,event):
        exit()

    def message(self,event):
        wx.MessageBox("I am a message box","Hey Yo")

app = wx.App()
WxClass(None,-0)
app.MainLoop()