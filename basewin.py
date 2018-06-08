# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class baseMainWindow
###########################################################################

class baseMainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JCDown", pos = wx.DefaultPosition, size = wx.Size( 582,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 582,450 ), wx.Size( 582,450 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.exit_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Exit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.exit_menuItem )
		
		self.menubar.Append( self.file_menu, u"文件" ) 
		
		self.edit_menu = wx.Menu()
		self.rule_menuItem = wx.MenuItem( self.edit_menu, wx.ID_ANY, u"Rule", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_menu.Append( self.rule_menuItem )
		
		self.menubar.Append( self.edit_menu, u"编辑" ) 
		
		self.help_menu = wx.Menu()
		self.about_menuItem = wx.MenuItem( self.help_menu, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.about_menuItem )
		
		self.menubar.Append( self.help_menu, u"帮助" ) 
		
		self.SetMenuBar( self.menubar )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_notebook2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.video_panel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.urls_lable_staticText1 = wx.StaticText( self.video_panel, wx.ID_ANY, u"输入网址", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.urls_lable_staticText1.Wrap( -1 )
		bSizer41.Add( self.urls_lable_staticText1, 0, wx.LEFT, 5 )
		
		
		bSizer41.Add( ( 0, 0), 0, wx.BOTTOM|wx.TOP, 2 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.video_url_textCtrl = wx.TextCtrl( self.video_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 430,-1 ), 0 )
		gSizer1.Add( self.video_url_textCtrl, 0, wx.ALL, 5 )
		
		self.fetch_button = wx.Button( self.video_panel, wx.ID_ANY, u"获取", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		gSizer1.Add( self.fetch_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer41.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		Stream_listBoxChoices = []
		self.Stream_listBox = wx.ListBox( self.video_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 430,150 ), Stream_listBoxChoices, 0 )
		bSizer41.Add( self.Stream_listBox, 0, wx.ALL, 5 )
		
		
		bSizer101.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.video_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer101.Add( self.m_staticline11, 0, wx.EXPAND|wx.TOP, 10 )
		
		
		self.video_panel.SetSizer( bSizer101 )
		self.video_panel.Layout()
		bSizer101.Fit( self.video_panel )
		self.m_notebook2.AddPage( self.video_panel, u"视频", False )
		self.forum_image_panel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.forum_image_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.urls_lable_staticText = wx.StaticText( self.forum_image_panel, wx.ID_ANY, u"页面网址(一行一条)：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.urls_lable_staticText.Wrap( -1 )
		bSizer4.Add( self.urls_lable_staticText, 0, wx.LEFT, 22 )
		
		
		bSizer4.Add( ( 0, 0), 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.image_urls_textCtrl = wx.TextCtrl( self.forum_image_panel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 520,188 ), wx.TE_MULTILINE )
		bSizer4.Add( self.image_urls_textCtrl, 1, wx.LEFT|wx.RIGHT, 25 )
		
		
		bSizer10.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.forum_image_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline1, 0, wx.EXPAND|wx.TOP, 10 )
		
		
		self.forum_image_panel.SetSizer( bSizer10 )
		self.forum_image_panel.Layout()
		bSizer10.Fit( self.forum_image_panel )
		self.m_notebook2.AddPage( self.forum_image_panel, u"论坛图片", False )
		
		bSizer1.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.location_lable_staticText = wx.StaticText( self, wx.ID_ANY, u"保存位置：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.location_lable_staticText.Wrap( -1 )
		gbSizer2.Add( self.location_lable_staticText, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.LEFT|wx.TOP, 10 )
		
		self.save_local_dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 465,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.save_local_dirPicker.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gbSizer2.Add( self.save_local_dirPicker, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 10 )
		
		
		bSizer9.Add( gbSizer2, 0, wx.SHAPED, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer4.SetMinSize( wx.Size( 560,-1 ) ) 
		self.save_individual_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保存到对应子文件夹中", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer4.Add( self.save_individual_checkBox, 0, wx.ALL, 10 )
		
		fgSizer1 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.proxy_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Proxy:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.proxy_checkBox.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		
		fgSizer1.Add( self.proxy_checkBox, 0, wx.ALL, 10 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, u"socks5://127.0.0.1:1086/", wx.Point( -1,-1 ), wx.Size( 180,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.download_button = wx.Button( self, wx.ID_ANY, u"开始下载", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		fgSizer4.Add( self.download_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 44 )
		
		
		bSizer22.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		gSizer4.Add( bSizer22, 1, 0, 0 )
		
		
		bSizer9.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.exit_menuItemOnMenuSelection, id = self.exit_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.rule_menuItemOnMenuSelection, id = self.rule_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.about_menuItemOnMenuSelection, id = self.about_menuItem.GetId() )
		self.fetch_button.Bind( wx.EVT_BUTTON, self.fetch_buttonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def exit_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def rule_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def about_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def fetch_buttonOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class rule_Dialog
###########################################################################

class rule_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 555,375 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, u"保存使用状态", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_checkBox9, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

