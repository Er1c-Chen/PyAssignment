import csv, os


class cuisine:
    def __init__(self, name, price, store, sold):
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


class cart:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def modAmount(self):
        self.amount = input("请输入所需的数量：")

    def show(self, data):
        print("****************************************\n"
              "序号  菜品名称            价格      数量\n")
        for t, item in enumerate(data)
MAXSIZE = 20
dish = []
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
            dish[i].name = data[i][0]
            dish[i].price = data[i][1]
            dish[i].store = data[i][2]
            dish[i].sold = data[i][3]


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
def buyMenu(dish, )
