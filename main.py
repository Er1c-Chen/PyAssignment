import csv, os


class cuisine:
    def __init__(self, order, name, price, store, sold):
        self.order = int(order)
        self.name = name
        self.price = float(price)
        self.store = int(store)
        self.sold = int(sold)

    def modName(self):
        self.name = input("请输入要修改的名字:")

    def modPrice(self):
        self.price = input("请输入要修改的价格:")

    def modStore(self):
        self.store = input("请输入要修改的库存:")

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
        inputPasswd = input("****************************************\n"
                            "请输入密码：")
        if inputPasswd == oriPasswd:
            os.system("cls")
            break
        else:
            print("密码错误，请重新输入!")


def loadDish():
    with open('menu.csv', 'r') as f:
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
    elif input() == '2':
        if coreMenu() == '1':
            buyMenu(dish, cart)
        else:
            os.system("cls")
            sellMenu(dish, cart)


def orderMenu(dish, cart):
    #i = 0
    while True:
        order = input("****************************************\n"
                      "请输入所选菜品的序号：")
        #cart[i].name = dish[int(order) - 1].name
        #cart[i].price = dish[int(order) - 1].price
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
        '''
        if (dish[int(order) - 1].store - dish[int(order) - 1].sold - amo) < 0:
            print("所选菜品库存不足！请重新选择！")
            i -= 1 if i >= 0 else 0
        else:
            print("添加成功！")
            cart[i].amount += amo
            dish[int(order) - 1].sold += amo
        ch = input("是否继续添加？y/n")
        if ch == 'n' or ch == 'N':
            break
        else:
            while True:
                if ch == 'y' or ch == 'Y':
                    i += 1
                    break
                else:
                    ch = input("错误！请输入y/n！")
        '''


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
                "      7.返回上级菜单\n"
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
        if coreMenu() == '1':
            buyMenu(dish, cart)
        else:
            os.system("cls")
            sellMenu(dish, cart)


def addCart(dish, cart):
    os.system("cls")
    order = 0
    global s
    print("****************************************\n"
          "序号   菜品名称            价格      数量")
    for item in dish:
        item.show()
    print("****************************************\n"
          "请选择需要添加的菜品（仅一份）：", end='')
    while True:
        flag = 0
        order = int(input()) - 1
        for item in dish:
            for t in enumerate(cart):
                if item.name == cart[t].name:
                    flag = 1
        if not flag:
            cart.append(cartItem(dish[order].name, dish[order].price, 1))
            dish[order].sold += 1
            break
        else:
            if flag:
                cart[order].amount += 1
                dish[order].sold += 1
                break
            else:
                print("序号输入错误！\n请重新输入：", end='')
    for item in dish:
        if item.store - item.sold < 0:
            s = 0
            print("所选菜品库存不足！")
            os.system("pause")
            addCart(dish, cart)
            break
    if s:
        print("添加成功！")
        settleCart(dish, cart)


def settleCart(dish, cart):
    print("****************************************\n"
          "菜品名称            价格      数量")
    for item in cart:
        item.show()
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
    for item in cart:
        del item
    cart = [cartItem(0, 0, 0)]
    print("****************************************")
    print("订单提交成功！\n欢迎下次光临！")
    os.system("pause")
    buyMenu(dish, cart)


def delCart(dish, cart):
    print("****************************************\n"
          "提示：请输入目前菜品的编号\n"
          "请选择删除的菜品（仅一份）：", end='')
    order = int(input()) - 1
    while True:
        if cart[order].amount > 1:
            cart[order].amount -= 1
            print("删除成功！")
            break
        if cart[order].amount == 1:
            cart.pop(order)
            print("删除成功！")
        else:
            print("未找到您删除的菜品！\n请重新输入：", end='')
    settleCart(dish, cart)


def addDish(dish, cart):
    print("****************************************\n"
          "序号   菜品名称            价格      数量", end='')
    for item in dish:
        item.show()
    print("****************************************\n"
          "请输入：序号 菜品名称 价格 库存量(逗号隔开)")
    a, b, c, d = eval(input())
    dish.append(cuisine(a, b, c, d, 0))
    print("添加成功！")
    print("****************************************\n"
          "序号   菜品名称            价格      数量", end='')
    for item in dish:
        item.show()
    os.system("pause")
    sellMenu(dish, cart)


def modDish(dish, cart):
    print("****************************************\n"
          "序号   菜品名称            价格      数量", end='')
    for item in dish:
        item.show()
    os.system('pause')
    order = input("****************************************\n"
                  "请输入要修改菜品序号：")
    order = int(order)
    cho = input("1.菜品名称 2.价格 3.库存"
                "\n 请输入要修改的参数：")
    if cho == '1':
        dish[order - 1].name = input("\n请输入新的菜品名称：")
    if cho == '2':
        dish[order - 1].price = input("\n请输入新的菜品价格：")
    if cho == '3':
        dish[order - 1].store = input("\n请输入新的菜品库存：")
    print("修改成功！")
    print("****************************************\n"
          "序号   菜品名称            价格      数量", end='')
    for item in dish:
        item.show()
    os.system("pause")
    sellMenu(dish, cart)


def delDish(dish, cart):
    print("****************************************\n"
          "序号   菜品名称            价格      数量", end='')
    for item in dish:
        item.show()
    order = int(input("请输入要删除的菜品序号：")) - 1
    dish.pop(order)
    print("删除成功！")
    print("****************************************\n"
          "序号   菜品名称            价格      数量", end='')
    for item in dish:
        item.show()
    os.system("pause")
    sellMenu(dish, cart)


MAXSIZE = 20
dish = []
cart = []
oriPasswd = 666666
loadDish()
ch = coreMenu()
if ch == '1':
    buyMenu(dish, cart)
if ch == '2':
    checkPass(oriPasswd)
    sellMenu(dish, cart)
