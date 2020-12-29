#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import datetime
from tkinter import *
from seckill.seckill_taobao import ChromeDrive



def run_killer(txt, txt2):
    seckill_time = txt.get()
    password = str(txt2.get())
    print(seckill_time, password)
    ChromeDrive(seckill_time = seckill_time, password = password).sec_kill()



def main():
    win = Tk()
    win.configure(bg='white')  # 设置背景颜色为白色
    win.title('liliai')
    width = 380
    height = 300
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    win.geometry(alignstr)

    lbl = Label(win, text = "time: ", width = 8, height = 2)
    lbl.grid(column = 0, row = 0)
    start_time = StringVar()
    txt = Entry(win, textvariable = start_time, width = 18)
    txt.grid(column = 1, row = 0)
    start_time.set(str(datetime.datetime.now()))

    lbl2 = Label(win, text = "password：", width = 8, height = 2)
    lbl2.grid(column = 0, row = 1)
    txt2 = Entry(win, width = 18, show = '*')
    txt2.grid(column = 1, row = 1)

    b1 = Button(win, text = '开始', command = lambda: run_killer(txt, txt2))
    b1.config(font = 'Helvetica -10 bold', bg = 'red', relief = 'sunken', width = 8, height = 6)
    b1.place(x=300, y=5)
    win.resizable(width = False, height = False)

    win.mainloop()


if __name__ == '__main__':
    main()
    # print(datetime.date.today())
