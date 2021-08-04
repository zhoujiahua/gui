#!/usr/bin/python3
# -*- coding: utf-8 -*-
import wx
import tkinter as tk
from tkinter import filedialog
 
app= wx.App()
frame= wx.Frame(None, title = 'CSV TO EXCEL', pos = (1000, 200), size = (500, 400))
path_text = wx.TextCtrl(frame, pos = (5, 5), size = (350, 24))
open_button = wx.Button(frame, label = 'OPEN', pos = (370, 5), size = (50, 24))
save_button = wx.Button(frame, label = 'SAVE', pos = (430, 5), size = (50, 24))

# wx.TE_MULTILINE可以实现换行功能,若不加此功能文本文档显示为一行显示
content_text= wx.TextCtrl(frame, pos = (5, 39), size = (475, 300), style = wx.TE_MULTILINE)

def getLocalFile():
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()
    return filePath

def openfile(event):
    fileUrl = getLocalFile()
    path_text.SetValue(fileUrl)
    path = path_text.GetValue()

    # encoding 设置文件打开时指定为utf8编码，避免写文件时出现编码错误
    with open(path, 'r', encoding='utf-8') as f:  
        content_text.SetValue(f.read())

def savefile(event):
     path = path_text.GetValue()
     text = content_text.GetValue()
     print(path, text)

open_button.Bind(wx.EVT_BUTTON, openfile)
save_button.Bind(wx.EVT_BUTTON, savefile)

if __name__ == '__main__':
    frame.Show()
    app.MainLoop()