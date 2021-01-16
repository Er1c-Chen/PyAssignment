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

        self.btnAdd = tk.Button(self.frame_bottom, text="添加", command=self.add)
        self.btnUpdate = tk.Button(self.frame_bottom, text="修改", command=self.update)
        self.btnDelete = tk.Button(self.frame_bottom, text="删除", command=self.delete)
        self.btnAdd.grid(row=0, column=0, padx=15, pady=30)
        self.btnUpdate.grid(row=0, column=1, padx=15, pady=30)
        self.btnDelete.grid(row=0, column=2, padx=15, pady=30)

        columns = ("name", "price", "store")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.column("name", anchor="center")
        self.tree.column("price", anchor="center")
        self.tree.column("store", anchor="center")
        self.tree.heading("name", text="菜品名称")
        self.tree.heading("price", text="价格")
        self.tree.heading("store", text="库存")
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_center.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        i = 0
        for v in dataConfig:
            tree.insert('', i, values=(v.get("name"), v.get("gender"), v.get("age")))
            i += 1

        
        
        head_indices = [chr(i + ord('a')) for i in range(len(self.dataConfig))]
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=head_indices)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.vbar.set)
        for i, item in enumerate(self.dataConfig):
            h_index = head_indices[i]
            self.tree.column(h_index, width=int(item[2]), anchor=item[3])
            self.tree.heading(h_index, text=item[1])
        self.tree["selectmode"] = "browse"
        self.tree.bind("<ButtonRelease-1>", self.item_click)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_center.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.item_selection = ""

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
            print(dish)
        super().__init__(dish)

MenuWindow()