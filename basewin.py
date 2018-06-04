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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JCDown", pos = wx.DefaultPosition, size = wx.Size( 582,415 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 582,415 ), wx.Size( 582,415 ) )
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
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.location_lable_staticText = wx.StaticText( self.forum_image_panel, wx.ID_ANY, u"保存位置：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.location_lable_staticText.Wrap( -1 )
		gbSizer2.Add( self.location_lable_staticText, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.TOP, 24 )
		
		self.image_local_dirPicker = wx.DirPickerCtrl( self.forum_image_panel, wx.ID_ANY, u"000", u"Select a folder", wx.DefaultPosition, wx.Size( 450,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.image_local_dirPicker.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gbSizer2.Add( self.image_local_dirPicker, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP, 18 )
		
		
		bSizer10.Add( gbSizer2, 0, wx.SHAPED, 5 )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.image_download_button = wx.Button( self.forum_image_panel, wx.ID_ANY, u"开始下载", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.image_download_button, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.LEFT, 103 )
		
		self.image_save_individual_checkBox = wx.CheckBox( self.forum_image_panel, wx.ID_ANY, u"每个页面的图片保存到对应的子文件夹中", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.image_save_individual_checkBox, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.LEFT, 87 )
		
		
		bSizer10.Add( gbSizer4, 1, 0, 0 )
		
		
		self.forum_image_panel.SetSizer( bSizer10 )
		self.forum_image_panel.Layout()
		bSizer10.Fit( self.forum_image_panel )
		self.m_notebook2.AddPage( self.forum_image_panel, u"论坛图片", False )
		self.video_panel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.video_panel, u"视频", False )
		
		bSizer1.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.exit_menuItemOnMenuSelection, id = self.exit_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.rule_menuItemOnMenuSelection, id = self.rule_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.about_menuItemOnMenuSelection, id = self.about_menuItem.GetId() )
		self.image_download_button.Bind( wx.EVT_BUTTON, self.image_download_buttonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def exit_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def rule_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def about_menuItemOnMenuSelection( self, event ):
		event.Skip()
	
	def image_download_buttonOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class rule_Dialog
###########################################################################

class rule_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 555,375 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

