# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class TranslatePdf
###########################################################################

class TranslatePdf ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"pdf翻译器", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"pdf：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.source_path_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"选择需要翻译的pdf", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer1.Add( self.source_path_picker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"翻译转换", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		source_Lan_SelectChoices = []
		self.source_Lan_Select = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, source_Lan_SelectChoices, 0 )
		self.source_Lan_Select.SetSelection( 0 )
		self.source_Lan_Select.SetMinSize( wx.Size( 150,-1 ) )
		
		bSizer2.Add( self.source_Lan_Select, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"翻译成", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		target_Lan_SelectChoices = []
		self.target_Lan_Select = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, target_Lan_SelectChoices, 0 )
		self.target_Lan_Select.SetSelection( 0 )
		self.target_Lan_Select.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.target_Lan_Select.SetMinSize( wx.Size( 150,-1 ) )
		
		bSizer2.Add( self.target_Lan_Select, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND|wx.SHAPED, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"翻译器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		translator_selectChoices = []
		self.translator_select = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, translator_selectChoices, 0 )
		self.translator_select.SetSelection( 0 )
		bSizer1.Add( self.translator_select, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"输出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.ouput_dir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.ouput_dir, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Translate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActive )
		self.m_button1.Bind( wx.EVT_BUTTON, self.ClickTranslate )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnActive( self, event ):
		event.Skip()
	
	def ClickTranslate( self, event ):
		event.Skip()
	

