import tkinter as tk
from tkinter import messagebox

import pandas as pd
import pymysql
import calendar
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox
import pickle
import numpy as np
import math
import serial

from socket import *

global_dict1 = {}
udp_socket = socket(AF_INET, SOCK_DGRAM)
local_addr = ('192.168.1.3', 50000)
dest_addr = ('192.168.1.3', 50000)
udp_socket.bind(local_addr)


def windows2():  # 功能界面
    win2 = tk.Toplevel()
    win2.geometry('1000x400')
    win2.title('操作')

    photo = tk.PhotoImage(file="8.png")  # 背景
    theLabel = tk.Label(win2, image=photo, compound=tk.CENTER)
    theLabel.place(x=0, y=0)

    global tree
    tree = ttk.Treeview(win2, show='headings', height=12)
    tree['columns'] = ("姓名", "卡号", "金额", "手机号")
    tree.column("姓名", width=100, anchor="center")
    tree.column("卡号", width=100, anchor="center")
    tree.column("金额", width=150, anchor="center")
    tree.column("手机号", width=150, anchor="center")
    tree.heading("姓名", text='姓名')
    tree.heading("卡号", text='卡号')
    tree.heading("金额", text='金额')
    tree.heading("手机号", text='手机号')

    btn = tk.Button(win2, text='添卡', bg='yellow', font=('黑体', 10, 'bold'), command=insert)
    btn.place(x=600, y=0)
    btn2 = tk.Button(win2, text='删卡', bg='yellow', font=('黑体', 10, 'bold'), command=delete)
    btn2.place(x=600, y=110)
    btn = tk.Button(win2, text='充值', bg='yellow', font=('黑体', 10, 'bold'), command=recharge)
    btn.place(x=600, y=130)
    btn = tk.Button(win2, text='消费', bg='yellow', font=('黑体', 10, 'bold'), command=pay)
    btn.place(x=600, y=170)
    # 2021-4-14

    Label_21 = tk.Label(win2, text='姓名', font=("Arial", 12))
    Label_21.place(x=650, y=0)
    Label_22 = tk.Label(win2, text='卡号', font=("Arial", 12))
    Label_22.place(x=650, y=20)
    Label_23 = tk.Label(win2, text='金额', font=("Arial", 12))
    Label_23.place(x=650, y=40)
    Label_23 = tk.Label(win2, text='手机', font=("Arial", 12))
    Label_23.place(x=650, y=60)
    Label_23 = tk.Label(win2, text='会员', font=("Arial", 12))
    Label_23.place(x=650, y=80)
    Label_24 = tk.Label(win2, text='卡号', font=("Arial", 12))
    Label_24.place(x=650, y=110)
    Label_31 = tk.Label(win2, text='卡号', font=("Arial", 12))
    Label_31.place(x=650, y=130)
    Label_31 = tk.Label(win2, text='金额', font=("Arial", 12))
    Label_31.place(x=650, y=150)
    Label_31 = tk.Label(win2, text='卡号', font=("Arial", 12))
    Label_31.place(x=650, y=170)
    Label_31 = tk.Label(win2, text='金额', font=("Arial", 12))
    Label_31.place(x=650, y=190)
    # 2021-4-14
    btn = tk.Button(win2, text='添卡的卡号', bg='yellow', font=('黑体', 10, 'bold'), command=getcard)
    btn.place(x=600, y=300)
    btn = tk.Button(win2, text='充值的卡号', bg='yellow', font=('黑体', 10, 'bold'), command=getcard3)
    btn.place(x=600, y=340)
    btn = tk.Button(win2, text='消费的卡号', bg='yellow', font=('黑体', 10, 'bold'), command=getcard4)
    btn.place(x=600, y=360)

    text = tk.Text(win2, width=71, height=5)
    text.place(x=0, y=300)
    text.insert(tk.INSERT, "操作说明："
                           "1.输入姓名、卡号、金额、手机号、及会员码（0-普通会员 1-白金会员 2-钻石会员）可以进行添卡操作 不能添加已经存在的卡"
                           "2·白金会员和钻石会员在充值时会得到部分返利"
                )  # INSERT索引表示插入光标当前的位置

    global E1  # 要添加的姓名
    E1 = tk.StringVar()
    Entry1 = tk.Entry(win2, textvariable=E1)
    Entry1.place(x=700, y=0)

    global E2  # 要添加的卡号
    E2 = tk.StringVar()
    Entry2 = tk.Entry(win2, textvariable=E2)
    Entry2.place(x=700, y=20)

    global E3  # 要添加的金额
    E3 = tk.StringVar()
    Entry3 = tk.Entry(win2, textvariable=E3)
    Entry3.place(x=700, y=40)

    global Ep  # 要添加的手机号
    Ep = tk.StringVar()
    Entry_p = tk.Entry(win2, textvariable=Ep)
    Entry_p.place(x=700, y=60)

    global Ev  # 要添加的vip
    Ev = tk.StringVar()
    Entry_v = tk.Entry(win2, textvariable=Ev)
    Entry_v.place(x=700, y=80)

    global E4  # 要删除的卡号
    E4 = tk.StringVar()
    Entry4 = tk.Entry(win2, textvariable=E4)
    Entry4.place(x=700, y=109)

    global E5  # 充值的金额
    E5 = tk.StringVar()
    Entry5 = tk.Entry(win2, textvariable=E5)
    Entry5.place(x=700, y=151)

    global E6  # 充值的卡号
    E6 = tk.StringVar()
    Entry6 = tk.Entry(win2, textvariable=E6)
    Entry6.place(x=700, y=130)

    global E7  # 消费的金额
    E7 = tk.StringVar()
    Entry7 = tk.Entry(win2, textvariable=E7)
    Entry7.place(x=700, y=191)

    global E8  # 消费的卡号
    E8 = tk.StringVar()
    Entry8 = tk.Entry(win2, textvariable=E8)
    Entry8.place(x=700, y=170)
    win2.mainloop()


def getcard():
    send_data = ("1")
    udp_socket.sendto(send_data.encode('gbk'), dest_addr)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('gbk'))
    E2.set(recv_data[0].decode('gbk'))


# 2021-4-14
def getmoney():
    global send_data
    money = E3.get()
    state = Ev.get()
    # print(type(state),type(state[2]))
    if state[2] == "0":
        send_data = ("2")
    if state[2] == "1":
        if len(money) == 1:
            send_data = ("000" + money)
        if len(money) == 2:
            send_data = ("00" + money)
        if len(money) >= 3:
            send_data = ("0" + money)
    if state[2] == "2":
        if len(money) == 1:
            send_data = ("a00" + money)
        if len(money) == 2:
            send_data = ("a0" + money)
        if len(money) >= 3:
            send_data = ("a" + money)
    # 2021-4-14
    udp_socket.sendto(send_data.encode('gbk'), dest_addr)  # 2021-4-14给注释掉的


# 充值卡3
def getcard3():
    send_data = ("3")
    udp_socket.sendto(send_data.encode('gbk'), dest_addr)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('gbk'))
    E6.set(recv_data[0].decode('gbk'))


# 消费卡5
def getcard4():
    send_data = ("5")
    udp_socket.sendto(send_data.encode('gbk'), dest_addr)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('gbk'))
    E8.set(recv_data[0].decode('gbk'))


def getcard5():
    send_data = ("7")
    udp_socket.sendto(send_data.encode('gbk'), dest_addr)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('gbk'))
    E_42.set(recv_data[0].decode('gbk'))


# 2021-4-14
def insert():  # 添卡
    global s
    name = E1.get()
    sno = E2.get()
    money = E3.get()
    phonenumber = Ep.get()
    vip = Ev.get()
    sql_insert = 'insert into yonghu values ("%s","%s","%s","%s","%s")' % (
        E1.get(), E2.get(), E3.get(), Ep.get(), Ev.get())
    sql_insert1 = 'insert into record(sno, money,time)values ("%s","+%s",now())' % (E2.get(), E3.get())
    sql_choice = "select * from yonghu"
    try:
        cursor.execute(sql_choice)
        data_1 = cursor.fetchall()
        for word in data_1:
            global_dict1[str(word[0])] = int(word[1])
        # print(global_dict1)
        if name == '':
            messagebox.showerror(title=u"error", message=u"请输入姓名")
            return
        if sno == '':
            messagebox.showerror(title=u"error", message=u"请输入卡号")
            return
        if money == '':
            messagebox.showerror(title=u"error", message=u"请输入金额")
            return
        if phonenumber == '':
            messagebox.showerror(title=u"error", message=u"请输入手机号")
            return
        if vip == '':
            messagebox.showerror(title=u"error", message=u"请输入vip码")
            return
        for key in global_dict1:
            if global_dict1[key] == int(sno):
                messagebox.showerror(title=u"error", message=u"sno已存在")
                return
    except Exception as err:
        print("SQL执行错误! 原因是", err)
    try:
        cursor.execute(sql_insert)
        cursor.execute(sql_insert1)
        db.commit()
    except Exception as err:
        db.rollback()
        print("SQL执行错误! 原因是", err)
    # 2021-4-14
    getmoney()
    sql_query = 'select * from yonghu'
    yonghu = pd.read_sql_query(sql_query, db)

    def delButton(tree):  # 清空原来的tree
        x = tree.get_children()
        for item in x:
            tree.delete(item)

    delButton(tree)

    a = len(yonghu)
    # print("a is:", a)
    result1 = np.array(yonghu)
    j = 0
    for j in range(a):
        b = (result1[j][0], result1[j][1], result1[j][2], result1[j][3])
        tree.insert('', j, values=(b))
    tree.place(x=0, y=0)


# 2021-4-14
def delete():  # 删卡
    sno = E4.get()
    cursor = db.cursor()
    sql_delete = 'delete from yonghu where sno = "%s" ' % (E4.get())
    sql_delete1 = 'delete from record where sno = "%s" ' % (E4.get())
    try:
        if sno == '':
            messagebox.showerror(title=u"error", message=u"请输入sno")
            return
        else:
            messagebox.showinfo(title="删卡", message=u"删卡成功!")
        cursor.execute(sql_delete)
        cursor.execute(sql_delete1)
        db.commit()
    finally:
        cursor.close()
        sql_query = 'select * from yonghu'
        yonghu = pd.read_sql_query(sql_query, db)

        # print(yonghu)
        def delButton(tree):  # 清空原来的tree
            x = tree.get_children()
            for item in x:
                tree.delete(item)

        delButton(tree)
        a = len(yonghu)
        result1 = np.array(yonghu)
        # print(result1)
        j = 0
        for j in range(a):
            b = (result1[j][0], result1[j][1], result1[j][2], result1[j][3])
            tree.insert('', j, values=(b))
        tree.place(x=0, y=0)


# 2021-4-14
def recharge():  # 充值
    k = 0
    global s, r, send_data
    sql_select = 'select * from yonghu'
    sql_vip = 'select vip from yonghu where sno="%s"' % (E6.get())
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    cursor.execute(sql_select)
    cursor2.execute(sql_vip)
    rs = cursor.fetchall()
    vip = cursor2.fetchone()
    sb = str(vip[0])
    try:
        sno = E6.get()  # 输入卡号
        money = E5.get()  # 输入金额
        # print("money的长度及其类型", len(money), type(money))
        if sno == '':
            messagebox.showerror(title=u"error", message=u"请输入卡号")
            return
        if money == '':
            messagebox.showerror(title=u"error", message=u"请输入金额")
            return
        for r in rs:  # 判断卡号是否存在
            s = str(r[1])
            if sno == s:
                k = 1
        if k == 0:
            messagebox.showerror(title=u"error", message=u"该卡号不存在")
            return
        if sb[2] == "0":  # 判断字符串state的第三个字符是不是0
            sql_money = 'UPDATE  yonghu SET money= money +"%s" WHERE sno="%s"' % (E5.get(), E6.get())
            sql_insert = 'insert into record(sno, money, time)values ("%s","+%s",now());' % (
                E6.get(), 1 * int(E5.get()))
            cursor.execute(sql_money)
            cursor.execute(sql_insert)
            # 2021-4-14
            if len(money) == 1:
                send_data = ("400" + money)
            if len(money) == 2:
                send_data = ("40" + money)
            if len(money) >= 3:
                send_data = ("4" + money)
            # print(send_data.encode('gbk'))
            udp_socket.sendto(send_data.encode('gbk'), dest_addr)

        if sb[2] == "1":  # 判断字符串state的第三个字符是不是1

            sql_money = 'UPDATE  yonghu SET money= money +2*"%s" WHERE sno="%s"' % (E5.get(), E6.get())
            sql_insert = 'insert into record(sno, money, time)values ("%s","+%s",now());' % (
                E6.get(), 2 * int(E5.get()))
            cursor.execute(sql_money)
            cursor.execute(sql_insert)
            # 2021-4-14
            if len(money) == 1:
                send_data = ("c00" + money)
            if len(money) == 2:
                send_data = ("c0" + money)
            if len(money) >= 3:
                send_data = ("c" + money)
            # print(send_data.encode('gbk'))
            udp_socket.sendto(send_data.encode('gbk'), dest_addr)

        if sb[2] == "2":  # 判断字符串state的第三个字符是不是2
            sql_money = 'UPDATE  yonghu SET money= money +3*"%s" WHERE sno="%s"' % (E5.get(), E6.get())
            sql_insert = 'insert into record(sno, money, time)values ("%s","+%s",now());' % (
                E6.get(), 3 * int(E5.get()))
            cursor.execute(sql_money)
            cursor.execute(sql_insert)
            # 2021-4-14
            if len(money) == 1:
                send_data = ("d00" + money)
            if len(money) == 2:
                send_data = ("d0" + money)
            if len(money) >= 3:
                send_data = ("d" + money)
            # print(send_data.encode('gbk'))
            udp_socket.sendto(send_data.encode('gbk'), dest_addr)
        messagebox.showinfo(title="充值", message=u"充值成功!")
        db.commit()
    finally:
        cursor.close()
        cursor1.close()
        cursor2.close()

        sql_query = 'select * from yonghu'
        yonghu = pd.read_sql_query(sql_query, db)

        def delButton(tree):  # 清空原来的tree
            x = tree.get_children()
            for item in x:
                tree.delete(item)

        delButton(tree)
        a = len(yonghu)
        result1 = np.array(yonghu)
        j = 0
        for j in range(a):
            b = (result1[j][0], result1[j][1], result1[j][2], result1[j][3])
            tree.insert('', j, values=(b))
        tree.place(x=0, y=0)


# 2021-4-14
def pay():  # 消费
    k = 0
    global s, send_data
    sql_money = 'UPDATE yonghu SET money= money -"%s" WHERE sno="%s"' % (E7.get(), E8.get())  #
    sql_insert = 'insert into record(sno, money, time)values ("%s","-%s",now());' % (E8.get(), E7.get())
    sql_select = 'select * from yonghu'
    sql_money1 = 'select money from yonghu where sno="%s"' % (E8.get())
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    cursor.execute(sql_select)
    cursor2.execute(sql_money1)
    rs = cursor.fetchall()
    money1 = cursor2.fetchone()
    try:
        for r in rs:
            s = str(r[1])

        sno = E8.get()
        money = E7.get()
        if sno == '':
            messagebox.showerror(title=u"error", message=u"请输入卡号")
            return
        if money == '':
            messagebox.showerror(title=u"error", message=u"请输入金额")
            return
        Q = messagebox.askquestion(title='提示', message='请再次确定消费金额')
        if Q == 'no':
            return
        if str(money1)[2] == ("-") or str(money1[0]) == "0":  # 判断金额
            messagebox.showerror(title=u"error", message=u"余额不足")
            return
        else:
            for r in rs:  # 判断卡号是否存在
                s = str(r[1])
                if sno == s:
                    k = 1
            if k == 0:
                messagebox.showerror(title=u"error", message=u"该卡号不存在")
                return
            messagebox.showinfo(title=u"消费", message=u"消费成功!")
            # 2021-4-14
            if len(money) == 1:
                send_data = ("600" + money)
            if len(money) == 2:
                send_data = ("60" + money)
            if len(money) >= 3:
                send_data = ("6" + money)
            # print(send_data.encode('gbk'))
            udp_socket.sendto(send_data.encode('gbk'), dest_addr)
        cursor.execute(sql_insert)
        cursor.execute(sql_money)
        db.commit()

    finally:
        cursor.close()
        cursor1.close()
        cursor2.close()
        sql_query = 'select * from yonghu'
        yonghu = pd.read_sql_query(sql_query, db)

        def delButton(tree):  # 清空原来的tree
            x = tree.get_children()
            for item in x:
                tree.delete(item)

        delButton(tree)
        a = len(yonghu)
        result1 = np.array(yonghu)
        j = 0
        for j in range(a):
            b = (result1[j][0], result1[j][1], result1[j][2], result1[j][3])
            tree.insert('', j, values=(b))
        tree.place(x=0, y=0)


def windows4():  # 查询界面
    win4 = tk.Toplevel()
    win4.geometry('300x200')
    win4.title('查询')
    btn = tk.Button(win4, text='查询信息', bg='yellow', font=('黑体', 10, 'bold'), command=find)
    btn.place(x=10, y=10)
    btn = tk.Button(win4, text='查询记录', bg='yellow', font=('黑体', 10, 'bold'), command=record1)
    btn.place(x=10, y=80)
    # 2021-4-14
    btn41 = tk.Button(win4, text='获取卡号', bg='yellow', font=('黑体', 10, 'bold'), command=getcard5)
    btn41.place(x=10, y=180)
    Label_41 = tk.Label(win4, text='请输入手机号：', font=("Arial", 12))
    Label_41.place(x=0, y=40)
    Label_42 = tk.Label(win4, text='请输入卡号：', font=("Arial", 12))
    Label_42.place(x=0, y=100)
    global E_41  # phonenumber
    E_41 = tk.StringVar()
    Entry_41 = tk.Entry(win4, textvariable=E_41)
    Entry_41.place(x=150, y=40)
    global E_42
    E_42 = tk.StringVar()
    Entry_42 = tk.Entry(win4, textvariable=E_42)
    Entry_42.place(x=150, y=100)


def find():  # 通过手机号查询卡号信息
    k = 0
    sno = E_41.get()
    win5 = tk.Toplevel()
    win5.geometry('550x450')
    win5.title('查询操作')

    sql_find = 'select * from yonghu where phonenumber = %s ' % (E_41.get())
    sql_select = 'select * from yonghu'
    cursor = db.cursor()
    cursor.execute(sql_select)
    rs = cursor.fetchall()
    global result
    try:
        if sno == '':
            messagebox.showerror(title=u"error", message=u"请输入sno")
            return
        else:
            for r in rs:  # 判断卡号是否存在
                s = str(r[3])
                if sno == s:
                    k = 1
            if k == 0:
                messagebox.showerror(title=u"error", message=u"该手机号不存在")
                return
        cursor.execute(sql_find)
        result = cursor.fetchall()
        db.commit()
    finally:
        cursor.close()
    global tree
    tree = ttk.Treeview(win5, show='headings', height=12)
    tree['columns'] = ("姓名", "卡号", "金额", "手机号")
    tree.column("姓名", width=100, anchor="center")
    tree.column("卡号", width=100, anchor="center")
    tree.column("金额", width=150, anchor="center")
    tree.column("手机号", width=150, anchor="center")
    tree.heading("姓名", text='姓名')
    tree.heading("卡号", text='卡号')
    tree.heading("金额", text='金额')
    tree.heading("手机号", text='手机号')
    a = len(result)
    result = np.array(result)
    j = 0
    for j in range(a):
        b = (result[j][0], result[j][1], result[j][2], result[j][3])
        tree.insert('', j, values=(b))
    tree.place(x=40, y=40)


def record1():  # 查询消费记录
    k = 0
    sno = E_42.get()
    win6 = tk.Toplevel()
    win6.geometry('500x500')
    win6.title('查询消费记录')
    sql_record = 'select * from record where sno = "%s" ' % (E_42.get())
    sql_select = 'select * from yonghu'
    sql_money = 'select money from yonghu where sno = "%s" ' % (E_42.get())
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor.execute(sql_select)
    cursor1.execute(sql_money)
    rs = cursor.fetchall()
    money1 = cursor1.fetchone()
    if money1 == None:
        tk.messagebox.showerror('错误', '该卡号不存在')
        return
    money = str(money1[0])
    try:
        if sno == '':
            messagebox.showerror(title=u"error", message=u"请输入卡号")
            return
        else:
            for r in rs:  # 判断卡号是否存在
                s = str(r[1])
                # print(s, sno)
                if sno == s:
                    k = 1
            if k == 0:
                messagebox.showerror(title=u"error", message=u"该卡号不存在")
                return
        if len(money) == 1:
            send_data = ("800" + money)
        if len(money) == 2:
            send_data = ("80" + money)
        if len(money) >= 3:
            send_data = ("8" + money)
        # print(send_data.encode('gbk'))
        udp_socket.sendto(send_data.encode('gbk'), dest_addr)
        cursor.execute(sql_record)
        db.commit()
    finally:
        cursor.close()
        cursor1.close()
        result1 = cursor.fetchall()
    global tree
    tree = ttk.Treeview(win6, show='headings', height=12)
    tree['columns'] = ("卡号", "记录", "时间")
    tree.column("卡号", width=100, anchor="center")
    tree.column("记录", width=55, anchor="center")
    tree.column("时间", width=150, anchor="center")
    tree.heading("卡号", text='卡号')
    tree.heading("记录", text='记录')
    tree.heading("时间", text='时间')
    a = len(result1)
    result1 = np.array(result1)
    j = 0
    for j in range(a):
        b = (result1[j][0], result1[j][1], result1[j][2])
        tree.insert('', j, values=(b))
    tree.place(x=40, y=40)


def windows5():  # 日历-------------111.py

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    class Calendar:

        def __init__(s, point=None, position=None):
            # point    提供一个基点，来确定窗口位置
            # position 窗口在点的位置 'ur'-右上, 'ul'-左上, 'll'-左下, 'lr'-右下
            # s.master = tk.Tk()
            global x, y
            s.master = tk.Toplevel()
            s.master.withdraw()
            fwday = calendar.SUNDAY

            year = datetime.now().year
            month = datetime.now().month
            locale = None
            sel_bg = '#ecffc4'
            sel_fg = '#05640e'

            s._date = datetime(year, month, 1)
            s._selection = None  # 设置为未选中日期

            s.G_Frame = ttk.Frame(s.master)

            s._cal = s.__get_calendar(locale, fwday)

            s.__setup_styles()  # 创建自定义样式
            s.__place_widgets()  # pack/grid 小部件
            s.__config_calendar()  # 调整日历列和安装标记
            # 配置画布和正确的绑定，以选择日期。
            s.__setup_selection(sel_bg, sel_fg)

            # 存储项ID，用于稍后插入。
            s._items = [s._calendar.insert('', 'end', values='') for _ in range(6)]

            # 在当前空日历中插入日期
            s._update()

            s.G_Frame.pack(expand=1, fill='both')
            s.master.overrideredirect(1)
            s.master.update_idletasks()
            width, height = s.master.winfo_reqwidth(), s.master.winfo_reqheight()
            if point and position:
                if position == 'ur':
                    x, y = point[0], point[1] - height
                elif position == 'lr':
                    x, y = point[0], point[1]
                elif position == 'ul':
                    x, y = point[0] - width, point[1] - height
                elif position == 'll':
                    x, y = point[0] - width, point[1]
            else:
                x, y = (s.master.winfo_screenwidth() - width) / 2, (s.master.winfo_screenheight() - height) / 2
            s.master.geometry('%dx%d+%d+%d' % (width, height, x, y))  # 窗口位置居中
            s.master.after(300, s._main_judge)
            s.master.deiconify()
            s.master.focus_set()
            s.master.wait_window()  # 这里应该使用wait_window挂起窗口，如果使用mainloop,可能会导致主程序很多错误

        def __get_calendar(s, locale, fwday):
            # 实例化适当的日历类
            if locale is None:
                return calendar.TextCalendar(fwday)
            else:
                return calendar.LocaleTextCalendar(fwday, locale)

        def __setitem__(s, item, value):
            if item in ('year', 'month'):
                raise AttributeError("attribute '%s' is not writeable" % item)
            elif item == 'selectbackground':
                s._canvas['background'] = value
            elif item == 'selectforeground':
                s._canvas.itemconfigure(s._canvas.text, item=value)
            else:
                s.G_Frame.__setitem__(s, item, value)

        def __getitem__(s, item):
            if item in ('year', 'month'):
                return getattr(s._date, item)
            elif item == 'selectbackground':
                return s._canvas['background']
            elif item == 'selectforeground':
                return s._canvas.itemcget(s._canvas.text, 'fill')
            else:
                r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(s, item)})
                return r[item]

        def __setup_styles(s):
            # 自定义TTK风格
            style = ttk.Style(s.master)
            arrow_layout = lambda dir: (
                [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
            )
            style.layout('L.TButton', arrow_layout('left'))
            style.layout('R.TButton', arrow_layout('right'))

        def __place_widgets(s):
            # 标头框架及其小部件
            Input_judgment_num = s.master.register(s.Input_judgment)  # 需要将函数包装一下，必要的
            hframe = ttk.Frame(s.G_Frame)
            gframe = ttk.Frame(s.G_Frame)
            bframe = ttk.Frame(s.G_Frame)
            hframe.pack(in_=s.G_Frame, side='top', pady=5, anchor='center')
            gframe.pack(in_=s.G_Frame, fill=tk.X, pady=5)
            bframe.pack(in_=s.G_Frame, side='bottom', pady=5)

            lbtn = ttk.Button(hframe, style='L.TButton', command=s._prev_month)
            lbtn.grid(in_=hframe, column=0, row=0, padx=12)
            rbtn = ttk.Button(hframe, style='R.TButton', command=s._next_month)
            rbtn.grid(in_=hframe, column=5, row=0, padx=12)

            s.CB_year = ttk.Combobox(hframe, width=5, values=[str(year) for year in
                                                              range(datetime.now().year, datetime.now().year - 11, -1)],
                                     validate='key', validatecommand=(Input_judgment_num, '%P'))
            s.CB_year.current(0)
            s.CB_year.grid(in_=hframe, column=1, row=0)
            s.CB_year.bind('<KeyPress>', lambda event: s._update(event, True))
            s.CB_year.bind("<<ComboboxSelected>>", s._update)
            tk.Label(hframe, text='年', justify='left').grid(in_=hframe, column=2, row=0, padx=(0, 5))

            s.CB_month = ttk.Combobox(hframe, width=3, values=['%02d' % month for month in range(1, 13)],
                                      state='readonly')
            s.CB_month.current(datetime.now().month - 1)
            s.CB_month.grid(in_=hframe, column=3, row=0)
            s.CB_month.bind("<<ComboboxSelected>>", s._update)
            tk.Label(hframe, text='月', justify='left').grid(in_=hframe, column=4, row=0)

            # 日历部件
            s._calendar = ttk.Treeview(gframe, show='', selectmode='none', height=7)
            s._calendar.pack(expand=1, fill='both', side='bottom', padx=5)

            ttk.Button(bframe, text="确 定", width=6, command=lambda: s._exit(True)).grid(row=0, column=0, sticky='ns',
                                                                                        padx=20)
            ttk.Button(bframe, text="取 消", width=6, command=s._exit).grid(row=0, column=1, sticky='ne', padx=20)

            tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=0, rely=0, relwidth=1, relheigh=2 / 200)
            tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=0, rely=198 / 200, relwidth=1, relheigh=2 / 200)
            tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=0, rely=0, relwidth=2 / 200, relheigh=1)
            tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=198 / 200, rely=0, relwidth=2 / 200, relheigh=1)

        def __config_calendar(s):
            # cols = s._cal.formatweekheader(3).split()
            cols = ['日', '一', '二', '三', '四', '五', '六']
            s._calendar['columns'] = cols
            s._calendar.tag_configure('header', background='grey90')
            s._calendar.insert('', 'end', values=cols, tag='header')
            # 调整其列宽
            font = tkFont.Font()
            maxwidth = max(font.measure(col) for col in cols)
            for col in cols:
                s._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                                   anchor='center')

        def __setup_selection(s, sel_bg, sel_fg):
            def __canvas_forget(evt):
                canvas.place_forget()
                s._selection = None

            s._font = tkFont.Font()
            s._canvas = canvas = tk.Canvas(s._calendar, background=sel_bg, borderwidth=0, highlightthickness=0)
            canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

            canvas.bind('<Button-1>', __canvas_forget)
            s._calendar.bind('<Configure>', __canvas_forget)
            s._calendar.bind('<Button-1>', s._pressed)

        def _build_calendar(s):
            year, month = s._date.year, s._date.month

            # update header text (Month, YEAR)
            header = s._cal.formatmonthname(year, month, 0)

            # 更新日历显示的日期
            cal = s._cal.monthdayscalendar(year, month)
            for indx, item in enumerate(s._items):
                week = cal[indx] if indx < len(cal) else []
                fmt_week = [('%02d' % day) if day else '' for day in week]
                s._calendar.item(item, values=fmt_week)

        def _show_select(s, text, bbox):
            """为新的选择配置画布。"""
            x, y, width, height = bbox

            textw = s._font.measure(text)

            canvas = s._canvas
            canvas.configure(width=width, height=height)
            canvas.coords(canvas.text, (width - textw) / 2, height / 2 - 1)
            canvas.itemconfigure(canvas.text, text=text)
            canvas.place(in_=s._calendar, x=x, y=y)

        def _pressed(s, evt=None, item=None, column=None, widget=None):
            """在日历的某个地方点击。"""
            if not item:
                x, y, widget = evt.x, evt.y, evt.widget
                item = widget.identify_row(y)
                column = widget.identify_column(x)

            if not column or not item in s._items:
                # 在工作日行中单击或仅在列外单击。
                return

            item_values = widget.item(item)['values']
            if not len(item_values):  # 这个月的行是空的。
                return

            text = item_values[int(column[1]) - 1]
            if not text:  # 日期为空
                return

            bbox = widget.bbox(item, column)
            if not bbox:  # 日历尚不可见
                s.master.after(20, lambda: s._pressed(item=item, column=column, widget=widget))
                return

            # 更新，然后显示选择
            text = '%02d' % text
            s._selection = (text, item, column)
            s._show_select(text, bbox)

        def _prev_month(s):
            """更新日历以显示前一个月。"""
            s._canvas.place_forget()
            s._selection = None

            s._date = s._date - timedelta(days=1)
            s._date = datetime(s._date.year, s._date.month, 1)
            s.CB_year.set(s._date.year)
            s.CB_month.set(s._date.month)
            s._update()

        def _next_month(s):
            """更新日历以显示下一个月。"""
            s._canvas.place_forget()
            s._selection = None

            year, month = s._date.year, s._date.month
            s._date = s._date + timedelta(
                days=calendar.monthrange(year, month)[1] + 1)
            s._date = datetime(s._date.year, s._date.month, 1)
            s.CB_year.set(s._date.year)
            s.CB_month.set(s._date.month)
            s._update()

        def _update(s, event=None, key=None):
            """刷新界面"""
            if key and event.keysym != 'Return': return
            year = int(s.CB_year.get())
            month = int(s.CB_month.get())
            if year == 0 or year > 9999: return
            s._canvas.place_forget()
            s._date = datetime(year, month, 1)
            s._build_calendar()  # 重建日历

            if year == datetime.now().year and month == datetime.now().month:
                day = datetime.now().day
                for _item, day_list in enumerate(s._cal.monthdayscalendar(year, month)):
                    if day in day_list:
                        item = 'I00' + str(_item + 2)
                        column = '#' + str(day_list.index(day) + 1)
                        s.master.after(100, lambda: s._pressed(item=item, column=column, widget=s._calendar))

        def _exit(s, confirm=False):
            """退出窗口"""
            if not confirm: s._selection = None
            s.master.destroy()

        def _main_judge(s):
            pass

            # s.master.tk_focusFollowsMouse() # 焦点跟随鼠标

        def selection(s):
            """返回表示当前选定日期的日期时间。"""
            if not s._selection: return None

            year, month = s._date.year, s._date.month
            return str(datetime(year, month, int(s._selection[0])))[:10]

        def Input_judgment(s, content):
            """输入判断"""
            # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
            if content.isdigit() or content == "":
                return True
            else:
                return False

    if __name__ == '__main__':
        root = tk.Toplevel()

        width, height = root.winfo_reqwidth() + 50, 50  # 窗口大小
        x, y = (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))  # 窗口位置居中

        date_str = tk.StringVar()
        date = ttk.Entry(root, textvariable=date_str)
        date.place(x=0, y=0, relx=5 / 20, rely=1 / 6, relwidth=14 / 20, relheigh=2 / 3)

        # Calendar((x, y), 'ur').selection() 获取日期，x,y为点坐标
        date_str_gain = lambda: [
            date_str.set(date)
            for date in [Calendar((x, y), 'ur').selection()]
            if date]
        tk.Button(root, text='日期:', command=date_str_gain).place(x=0, y=0, relx=1 / 20, rely=1 / 6, relwidth=4 / 20,
                                                                 relheigh=2 / 3)
        root.mainloop()


def windowsc():  # 计算器-------------calc.py
    class calculator:
        # 界面布局方法
        def __init__(self):
            # 创建主界面，并且保存到成员属性中
            self.root = tkinter.Toplevel()
            self.root.minsize(280, 450)
            self.root.maxsize(280, 470)
            self.root.title('计算器1.0')
            # 设置显式面板的变量
            self.result = tkinter.StringVar()
            self.result.set(0)
            # 设置一个全局变量  运算数字和f符号的列表
            self.lists = []
            # 添加一个用于判断是否按下运算符号的标志
            self.ispresssign = False
            # 界面布局
            self.menus()
            self.layout()
            self.root.mainloop()

        # 计算器菜单界面摆放
        def menus(self):
            # 添加菜单
            # 创建总菜单
            allmenu = tkinter.Menu(self.root)
            # 添加子菜单
            filemenu = tkinter.Menu(allmenu, tearoff=0)
            # 添加选项卡
            filemenu.add_command(label='标准型(T)            Alt+1', command=self.myfunc)
            filemenu.add_command(label='科学型(S)            Alt+2', command=self.myfunc)
            filemenu.add_command(label='程序员(P)            Alt+3', command=self.myfunc)
            filemenu.add_command(label='统计信息(A)        Alt+4', command=self.myfunc)
            # 添加分割线
            filemenu.add_separator()
            # 添加选项卡
            filemenu.add_command(label='历史记录(Y)      Ctrl+H', command=self.myfunc)
            filemenu.add_command(label='数字分组(I)', command=self.myfunc)
            # 添加分割线
            filemenu.add_separator()
            # 添加选项卡
            filemenu.add_command(label='基本(B)             Ctrl+F4', command=self.myfunc)
            filemenu.add_command(label='单位转换(U)      Ctrl+U', command=self.myfunc)
            filemenu.add_command(label='日期计算(D)      Ctrl+E', command=self.myfunc)
            menu1 = tkinter.Menu(filemenu, tearoff=0)
            menu1.add_command(label='抵押(M)', command=self.myfunc)
            menu1.add_command(label='汽车租赁(V)', command=self.myfunc)
            menu1.add_command(label='油耗(mpg)(F)', command=self.myfunc)
            menu1.add_command(label='油耗(l/100km)(U)', command=self.myfunc)
            filemenu.add_cascade(label='工作表(W)', menu=menu1)
            allmenu.add_cascade(label='查看(V)', menu=filemenu)

            # 添加子菜单2
            editmenu = tkinter.Menu(allmenu, tearoff=0)
            # 添加选项卡
            editmenu.add_command(label='复制(C)         Ctrl+C', command=self.myfunc)
            editmenu.add_command(label='粘贴(V)         Ctrl+V', command=self.myfunc)
            # 添加分割线
            editmenu.add_separator()
            # 添加选项卡
            menu2 = tkinter.Menu(filemenu, tearoff=0)
            menu2.add_command(label='复制历史记录(I)', command=self.myfunc)
            menu2.add_command(label='编辑(E)                      F2', command=self.myfunc)
            menu2.add_command(label='取消编辑(N)            Esc', command=self.myfunc)
            menu2.add_command(label='清除(L)    Ctrl+Shift+D', command=self.myfunc)
            editmenu.add_cascade(label='历史记录(H)', menu=menu2)
            allmenu.add_cascade(label='编辑(E)', menu=editmenu)

            # 添加子菜单3
            helpmenu = tkinter.Menu(allmenu, tearoff=0)
            # 添加选项卡
            helpmenu.add_command(label='查看帮助(V)       F1', command=self.myfunc)
            # 添加分割线
            helpmenu.add_separator()
            # 添加选项卡
            helpmenu.add_command(label='关于计算器(A)', command=self.myfunc)
            allmenu.add_cascade(label='帮助(H)', menu=helpmenu)

            self.root.config(menu=allmenu)

        # 计算器主界面摆放
        def layout(self):
            # 显示屏
            result = tkinter.StringVar()
            result.set(0)
            show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e',
                                       textvariable=self.result)
            show_label.place(x=5, y=20, width=270, height=70)
            # 功能按钮MC
            button_mc = tkinter.Button(self.root, text='MC', command=self.wait)
            button_mc.place(x=5, y=95, width=50, height=50)
            # 功能按钮MR
            button_mr = tkinter.Button(self.root, text='MR', command=self.wait)
            button_mr.place(x=60, y=95, width=50, height=50)
            # 功能按钮MS
            button_ms = tkinter.Button(self.root, text='MS', command=self.wait)
            button_ms.place(x=115, y=95, width=50, height=50)
            # 功能按钮M+
            button_mjia = tkinter.Button(self.root, text='M+', command=self.wait)
            button_mjia.place(x=170, y=95, width=50, height=50)
            # 功能按钮M-
            button_mjian = tkinter.Button(self.root, text='M-', command=self.wait)
            button_mjian.place(x=225, y=95, width=50, height=50)
            # 功能按钮←
            button_zuo = tkinter.Button(self.root, text='←', command=self.dele_one)
            button_zuo.place(x=5, y=150, width=50, height=50)
            # 功能按钮CE
            button_ce = tkinter.Button(self.root, text='CE', command=lambda: self.result.set(0))
            button_ce.place(x=60, y=150, width=50, height=50)
            # 功能按钮C
            button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
            button_c.place(x=115, y=150, width=50, height=50)
            # 功能按钮±
            button_zf = tkinter.Button(self.root, text='±', command=self.zf)
            button_zf.place(x=170, y=150, width=50, height=50)
            # 功能按钮√
            button_kpf = tkinter.Button(self.root, text='√', command=self.kpf)
            button_kpf.place(x=225, y=150, width=50, height=50)
            # 数字按钮7
            button_7 = tkinter.Button(self.root, text='7', command=lambda: self.pressnum('7'))
            button_7.place(x=5, y=205, width=50, height=50)
            # 数字按钮8
            button_8 = tkinter.Button(self.root, text='8', command=lambda: self.pressnum('8'))
            button_8.place(x=60, y=205, width=50, height=50)
            # 数字按钮9
            button_9 = tkinter.Button(self.root, text='9', command=lambda: self.pressnum('9'))
            button_9.place(x=115, y=205, width=50, height=50)
            # 功能按钮/
            button_division = tkinter.Button(self.root, text='/', command=lambda: self.presscalculate('/'))
            button_division.place(x=170, y=205, width=50, height=50)
            # 功能按钮%
            button_remainder = tkinter.Button(self.root, text='//', command=lambda: self.presscalculate('//'))
            button_remainder.place(x=225, y=205, width=50, height=50)
            # 数字按钮4
            button_4 = tkinter.Button(self.root, text='4', command=lambda: self.pressnum('4'))
            button_4.place(x=5, y=260, width=50, height=50)
            # 数字按钮5
            button_5 = tkinter.Button(self.root, text='5', command=lambda: self.pressnum('5'))
            button_5.place(x=60, y=260, width=50, height=50)
            # 数字按钮6
            button_6 = tkinter.Button(self.root, text='6', command=lambda: self.pressnum('6'))
            button_6.place(x=115, y=260, width=50, height=50)
            # 功能按钮*
            button_multiplication = tkinter.Button(self.root, text='*', command=lambda: self.presscalculate('*'))
            button_multiplication.place(x=170, y=260, width=50, height=50)
            # 功能按钮1/x
            button_reciprocal = tkinter.Button(self.root, text='1/x', command=self.ds)
            button_reciprocal.place(x=225, y=260, width=50, height=50)
            # 数字按钮1
            button_1 = tkinter.Button(self.root, text='1', command=lambda: self.pressnum('1'))
            button_1.place(x=5, y=315, width=50, height=50)
            # 数字按钮2
            button_2 = tkinter.Button(self.root, text='2', command=lambda: self.pressnum('2'))
            button_2.place(x=60, y=315, width=50, height=50)
            # 数字按钮3
            button_3 = tkinter.Button(self.root, text='3', command=lambda: self.pressnum('3'))
            button_3.place(x=115, y=315, width=50, height=50)
            # 功能按钮-
            button_subtraction = tkinter.Button(self.root, text='-', command=lambda: self.presscalculate('-'))
            button_subtraction.place(x=170, y=315, width=50, height=50)
            # 功能按钮=
            button_equal = tkinter.Button(self.root, text='=', command=lambda: self.pressequal())
            button_equal.place(x=225, y=315, width=50, height=105)
            # 数字按钮0
            button_0 = tkinter.Button(self.root, text='0', command=lambda: self.pressnum('0'))
            button_0.place(x=5, y=370, width=105, height=50)
            # 功能按钮.
            button_point = tkinter.Button(self.root, text='.', command=lambda: self.pressnum('.'))
            button_point.place(x=115, y=370, width=50, height=50)
            # 功能按钮+
            button_plus = tkinter.Button(self.root, text='+', command=lambda: self.presscalculate('+'))
            button_plus.place(x=170, y=370, width=50, height=50)

        # 计算器菜单功能
        def myfunc(self):
            tkinter.messagebox.showinfo('', '功能在努力的实现，请期待2.0版本的更新')

        # 数字方法
        def pressnum(self, num):
            # 全局化变量
            # 判断是否按下了运算符号
            if self.ispresssign == False:
                pass
            else:
                self.result.set(0)
                # 重置运算符号的状态
                self.ispresssign = False
            if num == '.':
                num = '0.'
            # 获取面板中的原有数字
            oldnum = self.result.get()
            # 判断界面数字是否为0
            if oldnum == '0':
                self.result.set(num)
            else:
                # 连接上新按下的数字
                newnum = oldnum + num

                # 将按下的数字写到面板中
                self.result.set(newnum)

        # 运算函数
        def presscalculate(self, sign):
            # 保存已经按下的数字和运算符号
            # 获取界面数字
            num = self.result.get()
            self.lists.append(num)
            # 保存按下的操作符号
            self.lists.append(sign)
            # 设置运算符号为按下状态
            self.ispresssign = True

        # 获取运算结果
        def pressequal(self):
            # 获取所有的列表中的内容（之前的数字和操作）
            # 获取当前界面上的数字
            curnum = self.result.get()
            # 将当前界面的数字存入列表
            self.lists.append(curnum)
            # 将列表转化为字符串
            calculatestr = ''.join(self.lists)
            # 使用eval执行字符串中的运算即可
            endnum = eval(calculatestr)
            # 将运算结果显示在界面中
            self.result.set(str(endnum)[:10])
            if self.lists != 0:
                self.ispresssign = True
            # 清空运算列表
            self.lists.clear()

        # 暂未开发说明
        def wait(self):
            tkinter.messagebox.showinfo('', '功能在努力的实现，请期待2.0版本的更新')

        # ←按键功能
        def dele_one(self):
            if self.result.get() == '' or self.result.get() == '0':
                self.result.set('0')
                return
            else:
                num = len(self.result.get())
                if num > 1:
                    strnum = self.result.get()
                    strnum = strnum[0:num - 1]
                    self.result.set(strnum)
                else:
                    self.result.set('0')

        # ±按键功能
        def zf(self):
            strnum = self.result.get()
            if strnum[0] == '-':
                self.result.set(strnum[1:])
            elif strnum[0] != '-' and strnum != '0':
                self.result.set('-' + strnum)

        # 1/x按键功能
        def ds(self):
            dsnum = 1 / int(self.result.get())
            self.result.set(str(dsnum)[:10])
            if self.lists != 0:
                self.ispresssign = True
            # 清空运算列表
            self.lists.clear()

        # C按键功能
        def sweeppress(self):
            self.lists.clear()
            self.result.set(0)

        # √按键功能
        def kpf(self):
            strnum = float(self.result.get())
            endnum = math.sqrt(strnum)
            if str(endnum)[-1] == '0':
                self.result.set(str(endnum)[:-2])
            else:
                self.result.set(str(endnum)[:10])
            if self.lists != 0:
                self.ispresssign = True
            # 清空运算列表
            self.lists.clear()

    # 实例化对象
    mycalculator = calculator()


def win():  # 主界面
    window.destroy()
    win = tk.Tk()
    win.geometry('600x400')
    win.title('健身房-燃烧你的卡路里！')

    photo = tk.PhotoImage(file="2.gif")
    theLabel = tk.Label(win, image=photo, compound=tk.CENTER)
    theLabel.place(x=0, y=0)

    btn = tk.Button(win, text='会员功能', bg='yellow', font=('黑体', 10, 'bold'), command=windows2)
    btn.place(x=10, y=280)

    btn1 = tk.Button(win, text='查询功能', bg='yellow', font=('黑体', 10, 'bold'), command=windows4)
    btn1.place(x=10, y=310)

    btn = tk.Button(win, text='万年历', bg='yellow', font=('黑体', 10, 'bold'), command=windows5)
    btn.place(x=500, y=280)

    btn = tk.Button(win, text='计算器', bg='yellow', font=('黑体', 10, 'bold'), command=windowsc)
    btn.place(x=500, y=310)

    Label_1 = tk.Label(win, text='健身房卡管理系统', font=("Arial", 22))
    Label_1.place(x=180, y=0)

    win.mainloop()


db = pymysql.connect(host="localhost", user="root", password="", db="mydb", charset="utf8")
# 获取游标对象
cursor = db.cursor()

# 窗口
window = tk.Tk()
window.title('欢迎进入健身房卡管理系统')
window.geometry('450x300')
# 画布放置图片
canvas = tk.Canvas(window, height=300, width=500)

photo = tk.PhotoImage(file="1.gif")  # file：t图片路径
imgLabel = tk.Label(window, image=photo)  # 把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)  # 自动对齐

canvas.pack(side='top')
# 标签 用户名密码
tk.Label(window, text='账号:', relief='groove').place(x=100, y=150)
tk.Label(window, text='密码:', relief='groove').place(x=100, y=190)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


def usr_log_in():
    cnt = 0
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    if usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    else:
        sql = "select * from test01"
        try:
            m = cursor.execute(sql)
            # print("结果条数：", m)
            while True:
                data = cursor.fetchone()
                cnt += 1
                if cnt == m:
                    break
            # print(data[0], data[1])
            if usr_name == data[0]:
                if usr_pwd == data[1]:
                    tk.messagebox.showinfo(title='welcome',
                                           message='欢迎您：' + usr_name)
                    win()
                else:
                    tk.messagebox.showerror(message='密码错误')
            else:
                is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
                if is_signup:
                    usr_sign_up()
        except Exception as err:
            print("SQL执行错误! 原因是", err)


# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        sql = "select * from test01"
        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            cursor.execute(sql)
            exist_usr_info = cursor.fetchall()
            # print(exist_usr_info)
        except Exception as err:
            print("SQL执行错误! 原因是", err)
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            try:
                sql = "insert into test01 values ('%s','%s')" % (nn, np)
                cursor.execute(sql)
                db.commit()
            except Exception as err:
                db.rollback()
                print("SQL执行错误! 原因是", err)
            tk.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()

    # 新建注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


# 退出的函数
def usr_sign_quit():
    window.destroy()


# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in, relief='groove')
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='注册', command=usr_sign_up, relief='groove')
bt_logup.place(x=210, y=230)
bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit, relief='groove')
bt_logquit.place(x=280, y=230)
# 主循环

window.mainloop()
