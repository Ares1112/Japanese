#!/usr/bin/python
#-*-coding:utf-8-*-
import wx, random
elementy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
class MyMenu(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(1024, 768))
		self.punkt=0
		if wybrano == 1:
			self.images = ['one.gif', 'two.gif', 'three.gif', 'four.gif', 'five.gif', 'six.gif', 'seven.gif', 'eight.gif', 'nine.gif', 'ten.gif', 'hundred.gif', 'thousand.gif', 'ten thousand.gif', 'yen.gif', 'time.gif']
		elif wybrano == 2:
			self.images = ['day.gif', 'book.gif', 'person.gif', 'moon.gif', 'fire.gif', 'water.gif', 'tree.gif', 'gold.gif', 'soil.gif', 'weekday.gif', 'up.gif', 'down.gif', 'middle.gif', 'half.gif']
		self.text1 = wx.StaticText(self, -1, 'czytanie kun yomi',(270, 500), style=wx.ALIGN_CENTRE)
		self.text2 = wx.StaticText(self, -1, 'czytanie on yomi',(270, 540), style=wx.ALIGN_CENTRE)
		self.text3 = wx.StaticText(self, -1, 'znaczenie',(270, 580), style=wx.ALIGN_CENTRE)
		self.display1 = wx.TextCtrl(self, -1, '',(410,495),size=(200,30))
		self.display2 = wx.TextCtrl(self, -1, '',(410,535),size=(200,30))
		self.display3 = wx.TextCtrl(self, -1, '',(410,575),size=(200,30))
		menubar = wx.MenuBar()
		file = wx.Menu()
		help = wx.Menu()
		file.AppendSeparator()
		quit = wx.MenuItem(file, 105, '&Wyjdz\tCtrl+Q', 'Wyjdz z aplikacji')
		file.AppendItem(quit)
		autor = wx.MenuItem(help, 201, '&Autor', 'O autorach')
		help.AppendItem(autor)
		menubar.Append(file, '&Plik')
		menubar.Append(help, '&Pomoc')
		self.SetMenuBar(menubar)
		wx.Button(self, 1, 'Nastepne', (80, 220))
		wx.Button(self, 2, 'Sprawdz',(80,260))
		self.panel = wx.Panel(self, -1, (450, 200), (100, 100),  style=wx.SUNKEN_BORDER)
		self.picture = wx.StaticBitmap(self.panel)
		self.panel.SetBackgroundColour('white')
		self.panel.Centre()
		self.sizer=wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.sizer)
		self.Centre()
		self.OnNext(-1)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=105)
		self.Bind(wx.EVT_BUTTON, self.OnNext, id=1)
		self.Bind(wx.EVT_BUTTON, self.OnCheck, id=2)
	def sprawdz(self,kun,on,tlum,item):
		if wybrano == 1:
			if item == 0:
				if kun == u'ひと' and (on == u'イチ　イッ' or on == u'イッ　イチ') and tlum == 'one':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 1:
				if kun == u'ふた' and on == u'ニ'  and tlum == 'two':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
       	 			dlg.Destroy()
			elif item == 2:
				if kun == u'みっ' and on == u'サン' and tlum == 'three':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 3:
				if (kun == u'よん　よっ　よ' or kun == u'よん　よ　よっ' or kun == u'よ　よっ　よん' or kun == u'よ　よん　よっ' or kun == u'よっ　よん　よ' or kun == u'よっ　よ　よん') and on == u'イチ'  and tlum == 'four':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 4:
				if kun == u'いつ' and on == u'ゴ' and tlum == 'five':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 5:
				if kun == u'むっ' and (on == u'ロク　ロッ' or on == u'ロッ　ロク') and tlum == 'six':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 6:
				if kun == u'なな' and on == u'シチ'   and tlum == 'seven':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 7:
				if kun == u'やっ' and (on == u'ハチ　ハッ' or on == u'ハッ　ハチ') and tlum == 'eight':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 8:
				if kun == u'ここの' and (on == u'キュウ　ク' or on == u'ク　キュウ') and tlum == 'nine':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 9:
				if kun == u'とお' and (on == u'ジュウ　ジュッ' or on == u'ジュッ　ジュウ') and tlum == 'ten':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 10:
				if kun == u'' and (on == u'ヒャク　ピャク　ビャク' or on == u'ヒャク　ビャク　ピャク' or on == u'ビャク　ヒャク　ピャク' or on == u'ビャク　ピャク　ヒャク' or on == u'ピャク　ビャク　ヒャク' or on == u'ピャク　ヒャク　ビャク') and tlum == 'hundred':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 11:
				if kun == u'' and (on == u'セン　ゼン' or on == u'ゼン　セン') and tlum == 'thousand':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 12:
				if kun == u'' and on == u'マン' and tlum == 'ten thousand':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 13:
				if kun == u'' and on == u'エン' and (tlum == 'yen circle' or tlum == 'circle yen' or tlum == 'yen' or tlum == 'circle'):
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
			elif item == 14:
				if kun == u'とき' and on == u'ジ' and tlum == 'time':
					self.punkt+=1
					self.OnNext(0)
				else:
					dlg = wx.MessageDialog(self, 'Jedna z odpowiedzi jest zla', 'Komunikat', wx.OK|wx.ICON_INFORMATION)
        			dlg.ShowModal()
        			dlg.Destroy()
        
	def OnQuit(self, event):
		self.Close()
	def OnNext(self, event):
		self.display1.Clear()
		self.display2.Clear()
		self.display3.Clear()
		random.shuffle(elementy)
		dlg = wx.MessageDialog(self, ' Koniec testu, twoj wynik to :%i' % self.punkt, 'Podsumowanie', wx.OK|wx.ICON_INFORMATION)
		try:
			self.item = elementy.pop()
			self.picture.SetBitmap(wx.Bitmap('images/' + self.images[self.item]))
		except IndexError:
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
        	frame = MyMenu(None, -1, 'Japonski')
        	frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
