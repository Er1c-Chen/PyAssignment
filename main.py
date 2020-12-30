import csv, os
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pandas as pd


class Field:
    def __init__(self, key, chn):
        self.key = key
        self.chn = chn
        self.label = None
        self.entry = None
        self.str_var = None


class BasicSettings(tk.Tk):
    def __init__(self, dataConfig):
        super().__init__()

        self.dataConfig = dataConfig
        self.frame_top = tk.Frame(width=600, height=90)
        self.frame_center = tk.Frame(width=600, height=180)
        self.frame_bottom = tk.Frame(width=600, height=90)
        self.label = tk.Label(self.frame_top, text="000", width=50, height=10).pack()
        self.btnAdd = tk.Button(self.frame_bottom, text="添加", command=self.add)
        self.btnUpdate = tk.Button(self.frame_bottom, text="修改", command=self.update)
        self.btnDelete = tk.Button(self.frame_bottom, text="删除", command=self.delete)
        self.btnAdd.grid(row=0, column=0, padx=50, pady=30)
        self.btnUpdate.grid(row=0, column=1, padx=50, pady=30)
        self.btnDelete.grid(row=0, column=2, padx=50, pady=30)

        columns = ("order", "name", "price", "store")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=columns)
        self.rollbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
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
        self.frame_center.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        i = 0
        for v in dataConfig:
            self.tree.insert('', i, values=(v.order, v.name, v.price, v.store-v.sold))
            i += 1

        self.tree["selectmode"] = "browse"
        self.tree.bind("<ButtonRelease-1>", self.item_click)
        self.mainloop()

    def item_click(self, event):
        pass

    def query(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class MenuWindow(BasicSettings):
    def __init__(self):
        dish = []
        with open('menu.csv', 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            data = list(reader)
            for i, item in enumerate(data):
                dish.append(cuisine(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
        super().__init__(dish)

class cuisine:
    def __init__(self, order, name, price, store, sold):
        self.order = int(order)
        self.name = name
        self.price = float(price)
        self.store = int(store)
        self.sold = int(sold)

    def show(self):
        print("%-6s" % self.order, end='')
        print("{0:{1}<9s}".format(self.name, chr(12288)), end='')
        print("%8.2f" % self.price, end='')
        print("%8d\n" % (self.store - self.sold), end='')

    def modName(self):
        self.name = input()

    def modPrice(self):
        self.price = float(input())

    def modStore(self):
        self.store = int(input())


class cartItem:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = float(price)
        self.amount = int(amount)

    def modAmount(self):
        self.amount = input("请输入所需的数量：")

    def show(self):
        print("{0:{1}<9s}".format(self.name, chr(12288)), end='')
        print("%8.2f" % self.price, end='')
        print("%8d\n" % self.amount, end='')


def checkPass(oriPasswd):
    os.system("cls")
    print("****************************************\n"
          "   欢迎使用餐厅订餐与计费管理系统\n"
          "               请登录")
    while True:
        inputPasswd = int(input("****************************************\n"
                                "请输入密码："))
        if inputPasswd == oriPasswd:
            os.system("cls")
            break
        else:
            print("密码错误，请重新输入!")


def loadDish():
    with open('menu.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        for i, item in enumerate(data):
            dish.append(cuisine(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))


def saveDish(dish):
    with open('menu.csv', 'w') as f:
        writer = csv.writer(f)
        for item in dish:
            writer.writerows(item)
        print("保存成功！", end='')


def coreMenu():
    cho = input("****************************************\n"
                "   欢迎使用餐厅订餐与计费管理系统\n"
                "         1.面向顾客功能\n         2.面向商家功能\n"
                "         3.退出程序\n"
                "****************************************\n"
                "请选择：")
    if cho == 3:
        exit(0)
    else:
        return cho


def buyMenu(dish, cart):
    os.system("cls")
    print("****************************************\n"
          "        欢迎使用本系统订餐！\n"
          "           1.开始订餐\n"
          "         2.返回上级菜单\n"
          "****************************************\n"
          "请选择：", end='')
    if input() == '1':
        os.system("cls")
        print("****************************************\n"
              "序号   菜品名称            价格      数量")
        for item in dish:
            item.show()
        orderMenu(dish, cart)
    else:
        ch = coreMenu()
        if ch == '1':
            buyMenu(dish, cart)
        elif ch == '2':
            os.system("cls")
            sellMenu(dish, cart)


def orderMenu(dish, cart):
    while True:
        order = input("****************************************\n"
                      "请输入所选菜品的序号：")
        amo = int(input("请输入你想要的数量："))
        if (dish[int(order) - 1].store - dish[int(order) - 1].sold - amo) > 0:
            cart.append(cartItem(dish[int(order) - 1].name, dish[int(order) - 1].price, amo))
            print("添加成功！")
            dish[int(order) - 1].sold += amo
        else:
            print("所选菜品库存不足！请重新选择！")
        ch = input("是否继续添加？y/n")
        if ch == 'n' or ch == 'N':
            break
        else:
            while True:
                if ch == 'y' or ch == 'Y':
                    break
                else:
                    ch = input("错误！请输入y/n！")
    settleCart(dish, cart)


def sellMenu(dish, cart):
    os.system("cls")
    cho = input("****************************************\n"
                "    欢迎使用商家管理功能！\n"
                "        1.显示菜单\n"
                "        2.保存菜单\n"
                "        3.添加菜品\n"
                "        4.修改菜品\n"
                "        5.删除菜品\n"
                "      6.重新加载菜单\n"
                "     7.制作销量一览表\n"
                "      8.返回上级菜单\n"
                "****************************************\n"
                "请选择：")
    os.system("cls")
    if cho == '1':
        print("****************************************\n"
              "      菜品名称            价格      数量")
        for item in dish:
            item.show()
        sellMenu(dish, cart)
    elif cho == '2':
        saveDish(dish)
        sellMenu(dish, cart)
    elif cho == '3':
        addDish(dish, cart)
        sellMenu(dish, cart)
    elif cho == '4':
        modDish(dish, cart)
        sellMenu(dish, cart)
    elif cho == '5':
        delDish(dish, cart)
        sellMenu(dish, cart)
    elif cho == '6':
        loadDish()
        sellMenu(dish, cart)
    elif cho == '7':
        showChart(dish)
        sellMenu(dish, cart)
    elif cho == '8':
        if coreMenu() == '1':
            buyMenu(dish, cart)
        else:
            os.system("cls")
            sellMenu(dish, cart)


def addCart(dish, cart):
    os.system("cls")
    flag = 0
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    print("****************************************\n"
          "请选择需要添加的菜品序号与数量：", end='')
    while True:
        inp = input().split()
        order = int(inp[0]) - 1
        orderAmo = int(inp[1])
        if (dish[order].store - dish[order].sold) >= 1:
            for item in cart:
                if item.name == dish[order].name:
                    item.amount += orderAmo
                    flag = 1
            if not flag:
                cart.append(cartItem(dish[order].name, dish[order].price, orderAmo))
            print("添加成功！")
            dish[order].sold += orderAmo
            settleCart(dish, cart)
            break
        else:
            print("所选菜品库存不足！")
            os.system("pause")
            addCart(dish, cart)
            break


def settleCart(dish, cart):
    sum = 0
    print("****************************************\n"
          "菜品名称            价格      数量")
    for item in cart:
        item.show()
        sum += item.price * item.amount
    print("总金额：{:.2f}".format(sum))
    ch = input("****************************************\n"
               "            1.确认订单\n"
               "            2.添加菜品\n"
               "            3.删除菜品\n"
               "请选择：")
    if ch == '1':
        confCart(cart)
    if ch == '2':
        addCart(dish, cart)
    if ch == '3':
        delCart(dish, cart)
    else:
        print("输入错误！")


def confCart(cart):
    del cart[:]
    print("****************************************")
    print("订单提交成功！\n欢迎下次光临！")
    os.system("pause")
    buyMenu(dish, cart)


def delCart(dish, cart):
    print("****************************************\n"
          "提示：请输入目前菜品的编号\n"
          "请选择删除的菜品与数量：", end='')
    while True:
        inp = input().split()
        order = int(inp[0]) - 1
        orderAmo = int(inp[1])
        if cart[order].amount - orderAmo >= 1:
            cart[order].amount -= orderAmo
            for item in dish:
                if item.name == cart[order].name:
                    item.sold -= orderAmo
            print("删除成功！")
            break
        elif cart[order].amount - orderAmo <= 0:
            cart.pop(order)
            for item in dish:
                if item.name == cart[order].name:
                    item.sold -= cart[order].amount
            print("删除成功！")
            break
        else:
            print("未找到您删除的菜品！\n请重新输入：", end='')
    settleCart(dish, cart)


def addDish(dish, cart):
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    print("****************************************")
    b = input("请输入菜品名称：")
    c = float(input("价格："))
    d = int(input("库存量："))
    dish.append(cuisine(dish[-1].order + 1, b, c, d, 0))
    print("添加成功！")
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    os.system("pause")
    sellMenu(dish, cart)


def modDish(dish, cart):
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    os.system('pause')
    order = input("****************************************\n"
                  "请输入要修改菜品序号：")
    order = int(order)
    cho = input("1.菜品名称 2.价格 3.库存"
                "\n 请输入要修改的参数：")
    if cho == '1':
        dish[order - 1].modName()
    if cho == '2':
        dish[order - 1].modPrice()
    if cho == '3':
        dish[order - 1].modStore()
    print("修改成功！")
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    os.system("pause")
    sellMenu(dish, cart)


def delDish(dish, cart):
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    order = int(input("请输入要删除的菜品序号：")) - 1
    dish.pop(order)
    print("删除成功！")
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    os.system("pause")
    sellMenu(dish, cart)


def showChart(dish):
    x = [i for i in range(len(dish))]
    y = []
    xticks = []
    for item in dish:
        y.append(item.sold * item.price)
        xticks.append(item.name)
    plt.xticks(x, xticks, fontproperties="SimHei", fontsize=9, wrap=True)
    plt.bar(x, y, align='center')
    plt.title('销量一览表', fontproperties="SimHei", fontsize=15)
    plt.ylabel('销售额/￥', fontproperties="SimHei", fontsize=15)
    plt.xlabel('菜品', fontproperties="SimHei", fontsize=15)
    plt.show()


MenuWindow()
oriPasswd = 666666
dish, cart = [], []
loadDish()
ch = coreMenu()
if ch == '1':
    buyMenu(dish, cart)
elif ch == '2':
    checkPass(oriPasswd)
    sellMenu(dish, cart)
