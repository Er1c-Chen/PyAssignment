import csv, os
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mes
import pandas as pd


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("餐厅订餐与计费管理系统")
        self.label_1 = tk.Label(self, text="欢迎使用餐厅订餐与计费管理系统\n\nDesigned:电智1902 陈虹冰", font=('FangSong', 12), width=30, height=10)

        self.btnBuy = tk.Button(self, text="面向顾客功能", font=('FangSong', 12), command=self.buy)
        self.btnSell = tk.Button(self, text="面向商家功能", font=('FangSong', 12), command=self.sell)

        self.label_1.grid(row=0, column=0, columnspan=2)
        self.btnBuy.grid(row=1, column=0, padx=40, pady=15)
        self.btnSell.grid(row=1, column=1, padx=40, pady=15)
        self.mainloop()

    def buy(self):
        BuyWindow()

    def sell(self):
        PassCheckWinw()


class BuyWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        global dish
        self.dataConfig = dish
        self.datalist = []
        self.frame_top = tk.Frame(self, width=400, height=90)
        self.frame_middle = tk.Frame(self, width=400, height=180)
        self.frame_bottom = tk.Frame(self, width=400, height=90)
        self.label = tk.Label(self.frame_top, text="000", font=('FangSong', 12), width=0, height=0).grid(row=0, column=0)
        self.btn = tk.Button(self.frame_bottom, text='完成选购', font=('FangSong', 12), command=self.finish)
        self.btn.grid(padx=160, pady=20)
        self.columns = ("order", "name", "price", "store")
        self.tree = ttk.Treeview(self.frame_middle, show="headings", height=8, columns=self.columns)
        self.rollbar = ttk.Scrollbar(self.frame_middle, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.column("order", width=40, anchor="center")
        self.tree.column("name", width=180, anchor="center")
        self.tree.column("price", width=80, anchor="center")
        self.tree.column("store", width=80, anchor="center")
        self.tree.heading("order", text="序号")
        self.tree.heading("name", text="菜品名称")
        self.tree.heading("price", text="价格")
        self.tree.heading("store", text="库存")
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        self.rollbar.grid(row=0, column=1, sticky=tk.NS)
        self.tree.configure(yscrollcommand=self.rollbar.set)

        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_middle.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_middle.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.tree["selectmode"] = "browse"
        self.tree.bind("<ButtonRelease-1>", self.item_click)
        self.loadin(dish)
        self.mainloop()

    def item_click(self, event):
        for item in self.tree.selection():
            data = list(self.tree.item(item, "values"))
            self.datalist.append([data[1], data[2], 1])

    def finish(self):
        global cart
        cart = pd.DataFrame(self.datalist, columns=['name', 'price', 'amount'])
        ShopCart()

    def loadin(self, dataConfig):
        i = 0
        for i, item in dataConfig.iterrows():
            self.tree.insert('', i, values=(i+1, item['name'], item.price, item.store - item.sold))
            i += 1


class SellWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.frame_top = tk.Frame(self, width=400, height=90)
        self.frame_middle = tk.Frame(self, width=400, height=180)
        self.frame_bottom = tk.Frame(self, width=400, height=90)

        self.lb_1 = tk.Label(self.frame_top, text='选择条目后即可进行删改操作')
        self.btnAdd = tk.Button(self.frame_bottom, text="添加", command=self.add)
        self.btnUpdate = tk.Button(self.frame_bottom, text="修改", command=self.update)
        self.btnDelete = tk.Button(self.frame_bottom, text="删除", command=self.delete)
        self.lb_1.grid(padx=130, pady=30)
        self.btnAdd.grid(row=0, column=0, padx=40, pady=30)
        self.btnUpdate.grid(row=0, column=1, padx=40, pady=30)
        self.btnDelete.grid(row=0, column=2, padx=40, pady=30)

        self.columns = ("order", "name", "price", "store")
        self.tree = ttk.Treeview(self.frame_middle, show="headings", height=8, columns=self.columns)
        self.rollbar = ttk.Scrollbar(self.frame_middle, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.column("order", width=40, anchor="center")
        self.tree.column("name", width=180, anchor="center")
        self.tree.column("price", width=80, anchor="center")
        self.tree.column("store", width=80, anchor="center")
        self.tree.heading("order", text="序号")
        self.tree.heading("name", text="菜品名称")
        self.tree.heading("price", text="价格")
        self.tree.heading("store", text="库存")
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        self.rollbar.grid(row=0, column=1, sticky=tk.NS)
        self.tree.configure(yscrollcommand=self.rollbar.set)

        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_middle.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_middle.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.tree["selectmode"] = "browse"
        self.tree.bind("<ButtonRelease-1>", self.item_click)
        self.loadin(dish)
        self.mainloop()

    def add(self):
        self.destroy()
        addWinw()

    def delete(self):
        global dish
        ind = dish.loc[dish['name'] == updateName].index
        dish.drop(index=ind, inplace=True)
        dish = dish.reset_index(drop=True)
        self.destroy()
        SellWindow()

    def update(self):
        self.destroy()
        updateWinw()

    def loadin(self, dataConfig):
        i = 0
        for i, item in dataConfig.iterrows():
            self.tree.insert('', i, values=(i+1, item['name'], item.price, int(item.store) - int(item.sold)))
            i += 1

    def item_click(self, event):
        global updateName
        for item in self.tree.selection():
            data = list(self.tree.item(item, "values"))
            updateName = data[1]


class PassCheckWinw(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('欢迎登陆')
        self.lb_1 = tk.Label(self, text='请输入登录密码：\n初始密码为：666666').grid(row=0, column=0, columnspan=2, padx=100, pady=20)
        self.en_1 = tk.Entry(self, show='*')
        self.en_1.grid(row=1, column=0, columnspan=2, pady=10)
        self.btn_1 = tk.Button(self, text='登录', command=self.sellwinw).grid(row=2, column=1, pady=20)
        self.btn_2 = tk.Button(self, text='退出', command=self.destroy).grid(row=2, column=0)
        self.mainloop()

    def sellwinw(self):
        if self.en_1.get() == '6':
            self.destroy()
            mes.showinfo('', '登录成功！')
            SellWindow()
        else:
            mes.showerror('警告', '密码错误，请重新输入！')


class ShopCart(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("购物车")
        self.frame_top = tk.Frame(self, width=400, height=90)
        self.frame_middle = tk.Frame(self, width=400, height=180)
        self.frame_bottom = tk.Frame(self, width=400, height=90)

        self.lb_1 = tk.Label(self.frame_top, font=('FangSong', 12), text='点击菜品条目来修改份数\n选0份即为删除')
        self.lb_1.grid(padx=100, pady=40)
        self.btn_1 = tk.Button(self.frame_bottom, text='支付', font=('FangSong', 12), command=self.pay)
        self.btn_2 = tk.Button(self.frame_bottom, text='取消', font=('FangSong', 12), command=self.destroy)
        self.btn_1.grid(row=0, column=0, padx=60, pady=20)
        self.btn_2.grid(row=0, column=1, padx=140, pady=20)
        self.columns = ("order", "name", "price", "amount")
        self.tree = ttk.Treeview(self.frame_middle, show="headings", height=8, columns=self.columns)
        self.rollbar = ttk.Scrollbar(self.frame_middle, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.column("order", width=40, anchor="center")
        self.tree.column("name", width=180, anchor="center")
        self.tree.column("price", width=80, anchor="center")
        self.tree.column("amount", width=80, anchor="center")
        self.tree.heading("order", text="序号")
        self.tree.heading("name", text="菜品名称")
        self.tree.heading("price", text="价格")
        self.tree.heading("amount", text="份数")
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        self.rollbar.grid(row=0, column=1, sticky=tk.NS)
        self.tree.configure(yscrollcommand=self.rollbar.set)

        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_middle.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_middle.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.loadin()
        self.tree.bind("<ButtonRelease-1>", self.item_click)
        self.mainloop()

    def loadin(self):
        global cart
        i = 0
        for i, item in cart.iterrows():
            self.tree.insert('', i, values=(i + 1, item['name'], item.price, item.amount))
            i += 1

    def item_click(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.destroy()
            amountConf(item_text)

    def pay(self):
        self.destroy()
        global cart
        sum = 0
        for item in cart:
            sum += item.price*item.amount
        mesg = '预计等待时间为{time}分钟\n是否付款{sum}元'
        jud = mes.askyesno('提示', mesg.format(time=len(cart)*10, sum=sum))
        if jud:
            mes.showinfo('', '谢谢您的惠顾，欢迎下次光临！')
            del cart[:]
        else:
            pass


class amountConf(tk.Toplevel):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.lbl = tk.Label(self, text='请选择订购的数量')
        self.lbl.grid(row=0)
        self.com = ttk.Combobox(self, value=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        self.com.bind("<<ComboboxSelected>>", self.getAmount)
        self.com.grid(row=1, pady=10)
        self.mainloop()

    def getAmount(self, event):
        amo = int(self.com.get())
        global cart, dish
        name = self.text[1]
        if amo:
            cart.loc[cart['name'] == name, 'amount'] = amo
        else:
            cart = cart.drop()
        self.destroy()
        ShopCart()


class addWinw(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('请填写相关信息')
        self.frame_1 = tk.Frame(self, width=400, height=200)
        self.frame_1.grid()

        self.lb_1 = tk.Label(self.frame_1, text='菜品名称')
        self.lb_2 = tk.Label(self.frame_1, text='价格')
        self.lb_3 = tk.Label(self.frame_1, text='库存')
        self.lb_4 = tk.Label(self.frame_1, text='销量')
        self.en_1 = tk.Entry(self.frame_1)
        self.en_2 = tk.Entry(self.frame_1)
        self.en_3 = tk.Entry(self.frame_1)
        self.en_4 = tk.Entry(self.frame_1)
        self.btn = tk.Button(self.frame_1, text='确定', command=self.conf)
        self.btn.grid(row=4, column=0, columnspan=2, padx=100, pady=20)

        self.lb_1.grid(row=0, column=0, padx=40, pady=10)
        self.lb_2.grid(row=1, column=0, padx=40, pady=10)
        self.lb_3.grid(row=2, column=0, padx=40, pady=10)
        self.lb_4.grid(row=3, column=0, padx=40, pady=10)
        self.en_1.grid(row=0, column=1, padx=40, pady=10)
        self.en_2.grid(row=1, column=1, padx=40, pady=10)
        self.en_3.grid(row=2, column=1, padx=40, pady=10)
        self.en_4.grid(row=3, column=1, padx=40, pady=10)
        self.mainloop()

    def conf(self):
        newitem = [[self.en_1.get(), self.en_2.get(), self.en_3.get(), self.en_4.get()]]
        df = pd.DataFrame(newitem, columns=['name', 'price', 'store', 'sold'])
        global dish
        dish = pd.concat([dish, df], ignore_index=True)
        self.destroy()
        SellWindow()


class updateWinw(addWinw):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(width=400, height=200)
        self.mainloop()

    def conf(self):
        global dish, updateName
        newitem = [self.en_1.get(), self.en_2.get(), self.en_3.get(), self.en_4.get()]
        ind = dish.loc[dish['name'] == updateName].index
        dish.loc[ind, 'name'] = newitem[0]
        dish.loc[ind, 'price'] = newitem[1]
        dish.loc[ind, 'store'] = newitem[2]
        dish.loc[ind, 'sold'] = newitem[3]
        self.destroy()
        SellWindow()


def showChart():
    global dish, cart
    x = [i for i in range(len(dish))]
    y = []
    xticks = []
    for item in dish.iterrows():
        y.append(item.sold * item.price)
        xticks.append(item.name)
    plt.xticks(x, xticks, fontproperties="SimHei", fontsize=9, wrap=True)
    plt.bar(x, y, align='center')
    plt.title('销量一览表', fontproperties="SimHei", fontsize=15)
    plt.ylabel('销售额/￥', fontproperties="SimHei", fontsize=15)
    plt.xlabel('菜品', fontproperties="SimHei", fontsize=15)
    plt.show()


def loadDish():
    global dish
    dish = pd.read_csv('menu.csv')


def saveDish():
    global dish
    dish.to_csv('menu.csv')


updateName = ''
dish = pd.DataFrame()
cart = pd.DataFrame()
loadDish()
LoginWindow()