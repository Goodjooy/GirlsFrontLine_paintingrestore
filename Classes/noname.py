# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GirlsFrontLine", pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem7 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )

		self.m_menu1.AppendSeparator()

		self.m_menu21 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem8 )

		self.m_menuItem9 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem9 )

		self.m_menuItem10 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem10 )

		self.m_menu1.AppendSubMenu( self.m_menu21, u"MyMenu" )

		self.m_menu1.AppendSeparator()

		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem5 )

		self.m_menubar1.Append( self.m_menu1, u"MyMenu" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu2, u"MyMenu" )

		self.SetMenuBar( self.m_menubar1 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RGB" ), wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge_rgb = wx.Gauge( sbSizer1.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_rgb.SetValue( 0 )
		bSizer6.Add( self.m_gauge_rgb, 1, wx.ALL, 5 )

		self.m_staticText_rgb = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_rgb.Wrap( -1 )

		bSizer6.Add( self.m_staticText_rgb, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		sbSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Alpha" ), wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge_alpha = wx.Gauge( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_alpha.SetValue( 0 )
		bSizer61.Add( self.m_gauge_alpha, 1, wx.ALL, 5 )

		self.m_staticText_alpha = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_alpha.Wrap( -1 )

		bSizer61.Add( self.m_staticText_alpha, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		sbSizer2.Add( bSizer61, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer2, 0, wx.EXPAND, 5 )

		self.m_listbook1 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel1 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer3.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		self.m_listbook1.AddPage( self.m_panel1, u"RGB", False )
		self.m_panel2 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		bSizer4.Add( self.m_listBox2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer4 )
		self.m_panel2.Layout()
		bSizer4.Fit( self.m_panel2 )
		self.m_listbook1.AddPage( self.m_panel2, u"Alpha", False )

		bSizer2.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		bSizer7.Add( self.m_listBox3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer7 )
		self.m_panel3.Layout()
		bSizer7.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"skiped", False )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, 0 )
		bSizer9.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer9 )
		self.m_panel4.Layout()
		bSizer9.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"unable", True )

		bSizer62.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer62.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer62.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_gauge3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge3.SetValue( 0 )
		bSizer62.Add( self.m_gauge3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( bSizer62, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setting( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer2.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_hyperlink2 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer2.Add( self.m_hyperlink2, 0, wx.ALL, 5 )


		bSizer10.Add( gSizer2, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer10 )
		self.m_scrolledWindow1.Layout()
		bSizer10.Fit( self.m_scrolledWindow1 )
		self.m_notebook2.AddPage( self.m_scrolledWindow1, u"a page", True )
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		gSizer3 = wx.GridSizer( 0, 3, 0, 0 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"label" ), wx.VERTICAL )

		m_radioBox1Choices = [ u"Radio Button" ]
		self.m_radioBox1 = wx.RadioBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		sbSizer3.Add( self.m_radioBox1, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox2Choices = [ u"Radio Button" ]
		self.m_radioBox2 = wx.RadioBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox2.SetSelection( 0 )
		sbSizer3.Add( self.m_radioBox2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox2 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox3 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox4 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox5 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox5, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer3.Add( sbSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"label" ), wx.VERTICAL )

		m_radioBox3Choices = [ u"Radio Button" ]
		self.m_radioBox3 = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 0 )
		sbSizer4.Add( self.m_radioBox3, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox4Choices = [ u"Radio Button" ]
		self.m_radioBox4 = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox4Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox4.SetSelection( 0 )
		sbSizer4.Add( self.m_radioBox4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox6 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox7 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox7, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer3.Add( sbSizer4, 1, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		sbSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText7 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button2 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button3, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer4, 0, wx.EXPAND, 5 )

		m_listBox5Choices = []
		self.m_listBox5 = wx.ListBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox5Choices, 0 )
		sbSizer5.Add( self.m_listBox5, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer3.Add( sbSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( gSizer3 )
		self.m_scrolledWindow2.Layout()
		gSizer3.Fit( self.m_scrolledWindow2 )
		self.m_notebook2.AddPage( self.m_scrolledWindow2, u"a page", False )
		self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,400 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer14.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer14.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer14.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dirPicker2 = wx.DirPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer14.Add( self.m_dirPicker2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self.m_scrolledWindow3, wx.ID_ANY, u"Toggle me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_toggleBtn1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer14 )
		self.m_scrolledWindow3.Layout()
		self.m_notebook2.AddPage( self.m_scrolledWindow3, u"a page", False )

		bSizer9.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer9.Add( m_sdbSizer1, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()
		bSizer9.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


