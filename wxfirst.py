import wx#Imports the wxython frame for python

app = wx.App()#Creates an app wx
window = wx.Frame(None,title="wxPython Frame",size=(300,200))#Sets dimensions and title for the wx windows
panel=wx.Panel(window)#Creates a panel for wx widgets
label=wx.StaticText(panel,label="Hello World",pos=(100,50))#Sets position of text and in-panel label
button=wx.Button(panel, label="Button 1", pos= (100,100))
window.Show(True)#Makes sure the wx window is shown
app.MainLoop()#loops the main window