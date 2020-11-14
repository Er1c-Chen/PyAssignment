import csv, os


class cuisine:
    def __init__(self, order, name, price, store, sold):
        self.order = order
        self.name = name
        self.price = price
        self.store = store
        self.sold = sold

    def modName(self):
        self.name = input("请输入要修改的名字:")

    def modPrice(self):
        self.price = input("请输入要修改的价格:")

    def modStore(self):
        self.store = input("请输入要修改的库存:")

    def show(self):
        print("&-6s" % self.order)
        print("%-18s" % self.name)
        print("%6.2f" % self.price)
        print("%10d\n" % (self.store - self.sold))


class cart:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def modAmount(self):
        self.amount = input("请输入所需的数量：")

    def show(self):
        print("%-24s" % self.name)
        print("%6.2f" % self.price)
        print("%10d\n" % self.amount)


MAXSIZE = 20
dish = []
cart = []

for num in range(MAXSIZE):
    dish[num] = cuisine()


def checkPass(oriPasswd):
    os.system("cls")
    print("****************************************\n"
          "   欢迎使用餐厅订餐与计费管理系统\n"
          "               请登录\n")
    while True:
        inputPasswd = input("****************************************\n"
                            "请输入密码：")
        if inputPasswd == oriPasswd:
            os.system("cls")
            break
        else:
            print("密码错误，请重新输入\n")


def loadDish():
    with open('menu.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        for i, item in enumerate(data):
            data[i].order = data[i][0]
            dish[i].name = data[i][1]
            dish[i].price = data[i][2]
            dish[i].store = data[i][3]
            dish[i].sold = data[i][4]


def saveDish(dish):
    with open('menu.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(dish)
        print("保存成功！")


def coreMenu():
    cho = input("****************************************\n"
                "   欢迎使用餐厅订餐与计费管理系统\n"
                "         1.面向顾客功能\n         2.面向商家功能\n"
                "         3.退出程序\n"
                "****************************************\n"
                "请选择：")
    if cho == 3:
        exit(0)
    return cho


def buyMenu(dish, cart):
    os.system("cls")
    print("****************************************\n"
          "        欢迎使用本系统订餐！\n"
          "           1.开始订餐\n"
          "         2.返回上级菜单\n"
          "****************************************\n"
          "请选择：")
    if input() == 1:
        os.system("cls")
        print("****************************************\n"
              "序号   菜品名称            价格      数量\n")
        for item in dish:
            item.show()
        orderMenu(dish, cart)
    elif input() == 2:
        if coreMenu() == 1:
            buyMenu(dish, cart)
        else:
            os.system("cls")
            sellMenu()


def orderMenu(dish, cart):
    i = 0
    while True:
        order = input("****************************************\n"
                      "请输入所选菜品的序号：")
        cart[i].name = dish[int(order) - 1].name
        cart[i].price = dish[int(order) - 1].price
        amo = input("请输入你想要的数量：")
        if (dish[int(order) - 1].store - dish[int(order) - 1].sold - amo) < 0:
            print("所选菜品库存不足！请重新选择！\n")
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
    if cho == 1:
        print("****************************************\n"
              "      菜品名称            价格      数量\n")
        for item in dish:
            item.show()
        sellMenu(dish, cart)
    elif cho == 2:
        saveDish(dish)
        sellMenu(dish, cart)
    elif cho == 3:
        addDish(dish, cart)
        sellMenu()
    elif cho == 4:
        modDish(dish, cart)
        sellMenu()
    elif cho == 5:
        delDish(dish, cart)
        sellMenu()
    elif cho == 6:
        loadDish()
        sellMenu()
    elif cho == 7:
        if coreMenu() == 1:
            buyMenu(dish, cart)
        else:
            os.system("cls")
            sellMenu(dish, cart)


def addCart (dish, cart):
    os.system("cls")
    order = 0
    print("****************************************\n"
          "序号   菜品名称            价格      数量\n")
    for item in dish:
        item.show()
    print("****************************************\n"
           "请选择需要添加的菜品（仅一份）：\n")
    while (True):
            order -= input()
            for i in enumerate(dish):
            if (strcmp(dish[order].name, cart[i].name) == 0)
            j=1;
            if ((!j) & & (0 <= order & & order < * n))
        for (i=0;i < strlen(cart[* line].name);i++)
        cart[* line].name[i]=0;
        strcpy(cart[* line].name, dish[order].name);
        cart[* line].price=dish[* line].price;
        cart[* line].amount=1;
        ( * line)++;
        dish[order].sold++;
    break;
    }
    else
    {
    if (j & & (0 <= order & & order <* n))
        {
            cart[order].amount += 1;
        dish[order].sold + +;
    break;
    }
    else printf("序号输入错误！\n请重新输入：");
    }
    }
    for (i=0;i < * n;i++)
    if (dish[i].store - dish[i].sold < 0)
    {
        s=0;
    printf("所选菜品库存不足！\n");
    system("pause");
    addCart(cart, dish, line, n);
    break;

}
if (s)
{
printf("添加成功！");
settleCart(dish, cart, line, n);
}