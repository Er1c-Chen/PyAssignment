import csv, os
from matplotlib import pyplot as plt


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
        writer.writerows(dish)
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
        chart(dish)
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
        if cart[order].amount > 1:
            cart[order].amount -= orderAmo
            for item in dish:
                if item.name == cart[order].name:
                    item.sold -= orderAmo
            print("删除成功！")
            break
        elif cart[order].amount == 1:
            cart.pop(order)
            for item in dish:
                if item.name == cart[order].name:
                    item.sold -= orderAmo
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


def chart(dish):
    x = [i for i in range(len(dish))]
    y = []
    xticks = []
    for item in dish:
        y.append(item.sold)
        xticks.append(item.name)
    plt.xticks(x, xticks, fontproperties="SimSun", fontsize=8, wrap=True)
    plt.bar(x, y, align='center')
    plt.title('销量一览表', fontproperties="SimSun", fontsize=15)
    plt.ylabel('销量', fontproperties="SimSun", fontsize=15)
    plt.xlabel('菜品', fontproperties="SimSun", fontsize=15)
    plt.show()


MAXSIZE = 20
oriPasswd = 666666
dish = []
cart = []
loadDish()
ch = coreMenu()
if ch == '1':
    buyMenu(dish, cart)
if ch == '2':
    checkPass(oriPasswd)
    sellMenu(dish, cart)
