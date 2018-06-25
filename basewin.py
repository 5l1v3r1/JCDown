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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JCDown", pos = wx.DefaultPosition, size = wx.Size( 582,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 582,470 ), wx.Size( 582,470 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.exit_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Exit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.exit_menuItem )
		
		self.menubar.Append( self.file_menu, u"文件" ) 
		
		self.edit_menu = wx.Menu()
		self.rule_menuItem = wx.MenuItem( self.edit_menu, wx.ID_ANY, u"Setting", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_menu.Append( self.rule_menuItem )
		
		self.menubar.Append( self.edit_menu, u"编辑" ) 
		
		self.help_menu = wx.Menu()
		self.about_menuItem = wx.MenuItem( self.help_menu, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.about_menuItem )
		
		self.menubar.Append( self.help_menu, u"帮助" ) 
		
		self.SetMenuBar( self.menubar )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.notebook.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.notebook.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.video_panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer6 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.urls_lable_staticText1 = wx.StaticText( self.video_panel, wx.ID_ANY, u"输入网址", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.urls_lable_staticText1.Wrap( -1 )
		fgSizer6.Add( self.urls_lable_staticText1, 0, wx.LEFT, 5 )
		
		
		fgSizer6.Add( ( 0, 0), 0, wx.BOTTOM|wx.TOP, 2 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.video_url_textCtrl = wx.TextCtrl( self.video_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 430,-1 ), 0 )
		gSizer1.Add( self.video_url_textCtrl, 0, wx.ALL, 5 )
		
		self.fetch_button = wx.Button( self.video_panel, wx.ID_ANY, u"获取", wx.Point( -1,-1 ), wx.Size( -1,25 ), 0 )
		gSizer1.Add( self.fetch_button, 0, wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.ALL, 5 )
		
		
		fgSizer6.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gbSizer31 = wx.GridBagSizer( 0, 0 )
		gbSizer31.SetFlexibleDirection( wx.BOTH )
		gbSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.title_staticText = wx.StaticText( self.video_panel, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_staticText.Wrap( -1 )
		gbSizer31.Add( self.title_staticText, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT, 5 )
		
		self.merge_VideoAndSound_checkBox = wx.CheckBox( self.video_panel, wx.ID_ANY, u"合并(V+S)\n(YouTube)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer31.Add( self.merge_VideoAndSound_checkBox, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.LEFT, 15 )
		
		self.Stream_listCtrl = wx.ListCtrl( self.video_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 430,150 ), wx.LC_REPORT|wx.SIMPLE_BORDER )
		gbSizer31.Add( self.Stream_listCtrl, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		Stream_listBoxChoices = []
		self.Stream_listBox = wx.ListBox( self.video_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 430,150 ), Stream_listBoxChoices, wx.LB_HSCROLL )
		gbSizer31.Add( self.Stream_listBox, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		fgSizer6.Add( gbSizer31, 1, wx.EXPAND, 5 )
		
		
		bSizer101.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		
		self.video_panel.SetSizer( bSizer101 )
		self.video_panel.Layout()
		bSizer101.Fit( self.video_panel )
		self.notebook.AddPage( self.video_panel, u"视频", False )
		
		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.location_lable_staticText = wx.StaticText( self, wx.ID_ANY, u"保存位置：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.location_lable_staticText.Wrap( -1 )
		gbSizer2.Add( self.location_lable_staticText, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 15 )
		
		self.save_local_dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 476,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.save_local_dirPicker.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gbSizer2.Add( self.save_local_dirPicker, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 20 )
		
		
		bSizer9.Add( gbSizer2, 0, wx.SHAPED, 0 )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.save_individual_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保存到对应子文件夹中", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.save_individual_checkBox.Enable( False )
		
		gbSizer3.Add( self.save_individual_checkBox, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.proxy_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Proxy:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.proxy_checkBox.SetValue(True) 
		self.proxy_checkBox.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		
		gbSizer3.Add( self.proxy_checkBox, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.proxy_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"socks5://127.0.0.1:1080/", wx.Point( -1,-1 ), wx.Size( 180,-1 ), 0 )
		gbSizer3.Add( self.proxy_textCtrl, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.stop_button = wx.Button( self, wx.ID_ANY, u"暂停", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		gbSizer3.Add( self.stop_button, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 40 )
		
		self.download_button = wx.Button( self, wx.ID_ANY, u"开始下载", wx.Point( -1,-1 ), wx.Size( -1,25 ), 0 )
		gbSizer3.Add( self.download_button, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 40 )
		
		
		bSizer9.Add( gbSizer3, 1, wx.ALL|wx.SHAPED, 10 )
		
		
		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 5, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.baseMainWindowOnClose )
		self.Bind( wx.EVT_MENU, self.exit_menuItemOnMenuSelection, id = self.exit_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.rule_menuItemOnMenuSelection, id = self.rule_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.about_menuItemOnMenuSelection, id = self.about_menuItem.GetId() )
		self.fetch_button.Bind( wx.EVT_BUTTON, self.fetch_buttonOnButtonClick )
		self.merge_VideoAndSound_checkBox.Bind( wx.EVT_CHECKBOX, self.merge_VideoAndSound_checkBoxOnCheckBox )
		self.Stream_listCtrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.Stream_listCtrlOnListItemSelected )
		self.Stream_listBox.Bind( wx.EVT_LISTBOX, self.Stream_listBoxOnListBox )
		self.stop_button.Bind( wx.EVT_BUTTON, self.stop_buttonOnButtonClick )
		self.download_button.Bind( wx.EVT_BUTTON, self.download_buttonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def baseMainWindowOnClose( self, event ):
		event.Skip()
	
	def exit_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def rule_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def about_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def fetch_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def merge_VideoAndSound_checkBoxOnCheckBox( self, event ):
		event.Skip()
	
	def Stream_listCtrlOnListItemSelected( self, event ):
		event.Skip()
	
	def Stream_listBoxOnListBox( self, event ):
		event.Skip()
	
	def stop_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def download_buttonOnButtonClick( self, event ):
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
	

