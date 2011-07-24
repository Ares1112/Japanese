#!/usr/bin/python
#-*-coding:utf-8-*-
import wx, random
import wx.lib.gestures as gest
class MyMenu(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(800, 600),style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
		self.punkt=0
		self.krok =1
		if wybrano == 1:
			self.elementy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
			self.images = ['one.gif', 'two.gif', 'three.gif', 'four.gif', 'five.gif', 'six.gif', 'seven.gif', 'eight.gif', 'nine.gif', 'ten.gif', 'hundred.gif', 'thousand.gif', 'ten thousand.gif', 'yen.gif', 'time.gif']
		elif wybrano == 2:
			self.elementy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
			self.images = ['day.gif', 'book.gif', 'person.gif', 'moon.gif', 'fire.gif', 'water.gif', 'tree.gif', 'gold.gif', 'soil.gif', 'weekday.gif', 'up.gif', 'down.gif', 'middle.gif', 'half.gif']
		self.text1 = wx.StaticText(self, -1, 'czytanie kun yomi',(200, 435), style=wx.ALIGN_CENTRE)
		self.text2 = wx.StaticText(self, -1, 'czytanie on yomi',(200, 475), style=wx.ALIGN_CENTRE)
		self.text3 = wx.StaticText(self, -1, 'znaczenie',(200, 515), style=wx.ALIGN_CENTRE)
		self.display1 = wx.TextCtrl(self, -1, '',(330,430),size=(200,30))
		self.display2 = wx.TextCtrl(self, -1, '',(330,470),size=(200,30))
		self.display3 = wx.TextCtrl(self, -1, '',(330,510),size=(200,30))
		menubar = wx.MenuBar()
		file = wx.Menu()
		help = wx.Menu()
		file.AppendSeparator()
		quit = wx.MenuItem(file, 105, '&Wyjdz\tCtrl+Q', 'Wyjdz z aplikacji')
		file.AppendItem(quit)
		autor = wx.MenuItem(help, 201, '&O autorze', 'O autorach')
		help.AppendItem(autor)
		menubar.Append(file, '&Plik')
		menubar.Append(help, 'P&omoc')
		self.SetMenuBar(menubar)
		wx.Button(self, 1, 'Nastepne', (80, 220))
		wx.Button(self, 2, 'Sprawdz',(80,260))
		self.panel2 = wx.Panel(self, -1, (400,250), (100,100), style=wx.SUNKEN_BORDER)
		self.panel2.SetBackgroundColour('white')
		self.picture2 = wx.StaticBitmap(self.panel2)
		self.picture2.SetBitmap(wx.Bitmap('images/rys/biel.gif'))
		self.mg = gest.MouseGestures(self.picture2, True, wx.MOUSE_BTN_LEFT)
		self.panel = wx.Panel(self, -1, (300, 250), (100, 100),  style=wx.SUNKEN_BORDER)
		self.picture = wx.StaticBitmap(self.panel)
		self.panel.SetBackgroundColour('white')
		self.sizer=wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.sizer)
		self.Centre()
		self.OnNext(-1)
		self.Bind(wx.EVT_MENU, self.Wiad, id = 201)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=105)
		self.Bind(wx.EVT_BUTTON, self.OnNext, id=1)
		self.Bind(wx.EVT_BUTTON, self.OnCheck, id=2)
	def rysuj(self):
		global krok
		if wybrano == 1:
			if self.item == 0:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/one1.gif'))
					self.mg.RemoveGesture('R')
			elif self.item == 1:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/two1.gif'))
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/two2.gif'))
					self.mg.RemoveGesture('R')
					self.krok = 1
					self.punkt+=1
			elif self.item == 2:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/three1.gif'))
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/three2.gif'))
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/three3.gif'))
					self.krok = 1
					self.punkt+=1
					self.mg.RemoveGesture('R')
			elif self.item == 3:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/four1.gif'))
					self.krok = 2
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('RD',self.rysuj)
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/four2.gif'))
					self.krok = 3
					self.mg.RemoveGesture('RD')
					self.mg.AddGesture('1',self.rysuj)
					self.mg.AddGesture('D1', self.rysuj)
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/four3.gif'))
					self.krok = 4
					self.mg.RemoveGesture('1')
					self.mg.RemoveGesture('D1')
					self.mg.AddGesture('DR', self.rysuj)
				elif self.krok == 4:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/four4.gif'))
					self.krok = 5
					self.mg.RemoveGesture('DR')
					self.mg.AddGesture('R', self.rysuj)
				elif self.krok == 5:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/four5.gif'))
					self.mg.RemoveGesture('R')
					self.krok = 1
					self.punkt+=1
			elif self.item == 4:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/five1.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('1', self.rysuj)
					self.mg.AddGesture('D1', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/five2.gif'))
					self.mg.RemoveGesture('1')
					self.mg.RemoveGesture('D1')
					self.mg.AddGesture('RD', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/five3.gif'))
					self.mg.RemoveGesture('RD')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 4
				elif self.krok == 4:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/five4.gif'))
					self.mg.RemoveGesture('R')
					self.krok = 1
					self.punkt+=1
			elif self.item == 5:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/six1.gif'))
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/six2.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('1', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/six3.gif'))
					self.mg.RemoveGesture('1')
					self.mg.AddGesture('3', self.rysuj)
					self.krok = 4
				elif self.krok == 4:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/six4.gif'))
					self.mg.RemoveGesture('3')
					self.krok = 1
					self.punkt+=1
			elif self.item == 6:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/seven1.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('DR', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/seven2.gif'))
					self.mg.RemoveGesture('DR')
					self.krok = 1
					self.punkt+=1
			elif self.item == 7:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/eight1.gif'))
					self.mg.RemoveGesture('1')
					self.mg.AddGesture('3', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/eight2.gif'))
					self.mg.RemoveGesture('3')
					self.krok = 1
					self.punkt+=1
			elif self.item == 8:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/nine1.gif'))
					self.mg.RemoveGesture('D1')
					self.mg.AddGesture('RDRU', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/nine2.gif'))
					self.mg.RemoveGesture('RDRU')
					self.krok = 1
					self.punkt+=1
			elif self.item == 9:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/ten1.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('D', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/ten2.gif'))
					self.mg.RemoveGesture('D')
					self.krok = 1
					self.punkt+=1
			elif self.item == 10:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/hundred1.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('1', self.rysuj)
					self.mg.AddGesture('D', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/hundred2.gif'))
					self.mg.RemoveGesture('1')
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('D', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/hundred3.gif'))
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('RD', self.rysuj)
					self.krok = 4
				elif self.krok == 4:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/hundred4.gif'))
					self.mg.RemoveGesture('RD')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 5
				elif self.krok == 5:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/hundred5.gif'))
					self.krok = 6
				elif self.krok == 6:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/hundred6.gif'))
					self.mg.RemoveGesture('R')
					self.krok = 1
					self.punkt+=1
			elif self.item == 11:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/thousand1.gif'))
					self.mg.RemoveGesture('L')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/thousand2.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('D', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/thousand3.gif'))
					self.mg.RemoveGesture('D')
					self.krok = 1
					self.punkt+=1
			elif self.item == 12:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/tenthousand1.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('RDU', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/tenthousand2.gif'))
					self.mg.RemoveGesture('RDU')
					self.mg.AddGesture('1', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/tenthousand3.gif'))
					self.mg.RemoveGesture('1')
					self.krok = 1
					self.punkt+=1
			elif self.item == 13:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/yen1.gif'))
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('RDL', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/yen2.gif'))
					self.mg.RemoveGesture('RDL')
					self.mg.AddGesture('D', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/yen3.gif'))
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 4
				elif self.krok == 4:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/yen4.gif'))
					self.mg.RemoveGesture('R')
					self.krok = 1
					self.punkt+=1
			elif self.item == 14:
				if self.krok == 1:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time1.gif'))
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('RD', self.rysuj)
					self.krok = 2
				elif self.krok == 2:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time2.gif'))
					self.mg.RemoveGesture('RD')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 3
				elif self.krok == 3:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time3.gif'))
					self.krok = 4
				elif self.krok == 4:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time4.gif'))
					self.krok = 5
				elif self.krok == 5:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time5.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('D', self.rysuj)
					self.krok = 6
				elif self.krok == 6:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time6.gif'))
					self.mg.RemoveGesture('D')
					self.mg.AddGesture('R', self.rysuj)
					self.krok = 7
				elif self.krok == 7:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time7.gif'))
					self.krok = 8
				elif self.krok == 8:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time8.gif'))
					self.mg.RemoveGesture('R')
					self.mg.AddGesture('D7', self.rysuj)
					self.krok = 9
				elif self.krok == 9:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time9.gif'))
					self.mg.RemoveGesture('D7')
					self.mg.AddGesture('3', self.rysuj)
					self.krok = 10
				elif self.krok == 10:
					self.picture2.SetBitmap(wx.Bitmap('images/rys/time10.gif'))
					self.mg.RemoveGesture('3')
					self.krok = 1
					self.punkt+=1
	def Wiad(self, event):
		dlg = wx.MessageDialog(self, 'Program stworzony przez Arkadiusza (Aresa) Błasiaka', 'Autor', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	def sprawdz(self,kun,on,tlum,item):
		if wybrano == 1:
			if item == 0:
				if kun == u'ひと' and (on == u'イチ　イッ' or on == u'イッ　イチ') and tlum == 'one':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 1:
				if kun == u'ふた' and on == u'ニ'  and tlum == 'two':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 2:
				if kun == u'みっ' and on == u'サン' and tlum == 'three':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 3:
				if (kun == u'よん　よっ　よ' or kun == u'よん　よ　よっ' or kun == u'よ　よっ　よん' or kun == u'よ　よん　よっ' or kun == u'よっ　よん　よ' or kun == u'よっ　よ　よん') and on == u'イチ'  and tlum == 'four':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 4:
				if kun == u'いつ' and on == u'ゴ' and tlum == 'five':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 5:
				if kun == u'むっ' and (on == u'ロク　ロッ' or on == u'ロッ　ロク') and tlum == 'six':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 6:
				if kun == u'なな' and on == u'シチ'   and tlum == 'seven':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 7:
				if kun == u'やっ' and (on == u'ハチ　ハッ' or on == u'ハッ　ハチ') and tlum == 'eight':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 8:
				if kun == u'ここの' and (on == u'キュウ　ク' or on == u'ク　キュウ') and tlum == 'nine':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 9:
				if kun == u'とお' and (on == u'ジュウ　ジュッ' or on == u'ジュッ　ジュウ') and tlum == 'ten':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 10:
				if kun == u'' and (on == u'ヒャク　ピャク　ビャク' or on == u'ヒャク　ビャク　ピャク' or on == u'ビャク　ヒャク　ピャク' or on == u'ビャク　ピャク　ヒャク' or on == u'ピャク　ビャク　ヒャク' or on == u'ピャク　ヒャク　ビャク') and tlum == 'hundred':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 11:
				if kun == u'' and (on == u'セン　ゼン' or on == u'ゼン　セン') and tlum == 'thousand':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 12:
				if kun == u'' and on == u'マン' and tlum == 'ten thousand':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 13:
				if kun == u'' and on == u'エン' and (tlum == 'yen circle' or tlum == 'circle yen' or tlum == 'yen' or tlum == 'circle'):
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 14:
				if kun == u'とき' and on == u'ジ' and tlum == 'time':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
		elif wybrano == 2:
			if item == 0:
				if (kun == u'ひ　び' or kun == u'び　ひ') and (on == u'ニ　ニチ　ニッ' or on == u'ニ　ニッ　ニチ' or on == u'ニチ　ニッ　ニ' or on == u'ニチ　ニ　ニッ' or on == u'ニッ　ニ　ニチ' or on == u'ニッ　ニチ　ニ') and (tlum == 'day sun' or tlum == 'sun day' or tlum == 'day' or tlum == 'sun'):
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 1:
				if kun == u'もと' and on == 'ホン' and (tlum == 'book' or tlum == 'basis' or tlum == 'book basis' or tlum == 'basis book'):
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 2:
				if kun == u'ひと' and (on == 'ジン　ニン' or on == 'ニン　ジン') and tlum == 'person':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 3:
				if kun == u'つき' and (on == u'ゲツ　ガツ' or on == u'ガツ　ゲツ') and (tlum == 'moon' or tlum == 'month' or tlum == 'moon month' or tlum == 'month moon'):
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 4:
				if kun == u'ひ' and on == u'カ' and tlum == 'fire':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 5:
				if kun == u'みず' and on == u'スイ' and tlum == 'water':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 6:
				if kun == u'き' and on == u'モク' and tlum == 'tree':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 7:
				if kun == u'かね' and on == 'キン' and (tlum == 'gold' or tlum == 'money' or tlum == 'money gold' or tlum == 'gold money'):
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 8:
				if kun == u'つち' and on == u'ド' and tlum == 'soil':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 9:
				if kun == '' and on == u'ヨウ' and tlum == 'weekday':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 10:
				if kun == u'うえ' and on == u'ジョウ' and tlum == 'up':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 11:
				if kun == u'した' and on == u'カ' and tlum == 'down':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 12:
				if kun == u'なか' and (on == u'チュウ　ジュウ' or on == u'ジュウ　チュウ') and tlum == 'middle':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
			elif item == 13:
				if kun == '' and on == u'ハン' and tlum == 'half':
					self.punkt+=1
					self.OnNext(0)
				else:
					self.OnBlad(0)
	def OnQuit(self, event):
		self.Close()
	def OnNext(self, event):
		self.display1.Clear()
		self.display2.Clear()
		self.display3.Clear()
		del self.krok
		self.krok = 1
		self.mg.RemoveAllGestures()
		self.picture2.SetBitmap(wx.Bitmap('images/rys/biel.gif'))
		random.shuffle(self.elementy)
		dlg = wx.MessageDialog(self, ' Koniec testu, twoj wynik to :%i' % self.punkt, 'Podsumowanie', wx.OK|wx.ICON_INFORMATION)
		try:
			self.item = self.elementy.pop()
			self.picture.SetBitmap(wx.Bitmap('images/' + self.images[self.item]))
			if wybrano == 1:
				if self.item == 0:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 1:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 2:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 3:
					self.mg.AddGesture('D',self.rysuj)
				elif self.item == 4:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 5:
					self.mg.AddGesture('D',self.rysuj)
				elif self.item == 6:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 7:
					self.mg.AddGesture('1',self.rysuj)
				elif self.item == 8:
					self.mg.AddGesture('D1',self.rysuj)
				elif self.item == 9:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 10:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 11:
					self.mg.AddGesture('L',self.rysuj)
				elif self.item == 12:
					self.mg.AddGesture('R',self.rysuj)
				elif self.item == 13:
					self.mg.AddGesture('D',self.rysuj)
				elif self.item == 14:
					self.mg.AddGesture('D',self.rysuj)
		except IndexError:
			dlg.ShowModal()
			dlg.Destroy()
			self.Close()
	def OnBlad(self, event):
		dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest niepoprawna', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	def OnCheck(self,event):
		kun = self.display1.GetValue()
		on = self.display2.GetValue()
		tlum = self.display3.GetValue()
		self.sprawdz(kun,on,tlum,self.item)

class Wybor(wx.Dialog):
	def __init__(self, parent, id, title):
		wx.Dialog.__init__(self, parent, id, title, size=(500, 500))
		wx.Button(self, 1, 'Lekcja 1', (190, 130),(110,-1))
		wx.Button(self, 2, 'Lekcja 2', (190, 200), (110, -1))
		wx.Button(self, 3, 'Lekcja 3', (190, 270),(110,-1))
		wx.Button(self, 4, 'Lekcja 4', (190, 340), (110, -1))
		self.Bind(wx.EVT_BUTTON, self.wybierz1, id=1)
		self.Bind(wx.EVT_BUTTON, self.wybierz2, id=2)
		self.Bind(wx.EVT_BUTTON, self.wybierz3, id=3)
		self.Bind(wx.EVT_BUTTON, self.wybierz4, id=4)
		self.Centre()
		self.ShowModal()
		self.Destroy()
	def wybierz1(self,event):
		global wybrano
		wybrano = 1
		self.Close(True)
	def wybierz2(self,event):
		global wybrano
		wybrano = 2
		self.Close(True)
	def wybierz3(self,event):
		global wybrano
		wybrano = 3
		self.Close(True)
	def wybierz4(self,event):
		global wybrano
		wybrano = 4
		self.Close(True)
	
class MyApp(wx.App):
    def OnInit(self):
    	if Wybor(None, -1, 'Wybor'):
        	frame = MyMenu(None, -1, 'Kanji This !')
        	frame.SetIcon(wx.Icon('images/flag.png', wx.BITMAP_TYPE_PNG))
        	frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
