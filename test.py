import numpy as np
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

class BaseWindow(tk.Tk):
    def __init__(self, queryConfig, dataConfig):
        self.queryConfig = queryConfig
        self.dataConfig = dataConfig
        super().__init__()
        self.frame_top = tk.Frame(width=600, height=90)
        self.frame_center = tk.Frame(width=600, height=180)
        self.frame_bottom = tk.Frame(width=600, height=90)
        self.queryFields = []
        for i, item in enumerate(queryConfig):
            fld = Field(item[0], item[1])
            self.queryFields.append(fld)
            fld.label = tk.Label(self.frame_top, text=fld.chn)
            fld.str_var = tk.StringVar()
            fld.entry = tk.Entry(self.frame_top, textvariable=fld.str_var)
            fld.str_var.set('')
        self.btn_query = tk.Button(self.frame_top, text="查询", command=self.query)
        self.layout()

        self.btn_add = tk.Button(self.frame_bottom, text="添加", command=self.insert)
        self.btn_update = tk.Button(self.frame_bottom, text="修改", command=self.update)
        self.btn_delete = tk.Button(self.frame_bottom, text="删除", command=self.delete)
        self.btn_add.grid(row=0, column=0, padx=15, pady=30)
        self.btn_update.grid(row=0, column=1, padx=15, pady=30)
        self.btn_delete.grid(row=0, column=2, padx=15, pady=30)

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
        self.query()
        self.mainloop()

    def layout(self):
        for i, fld in enumerate(self.queryFields):
            fld.label.grid(row=i, column=0, padx=5, pady=5)
            fld.entry.grid(row=i, column=1, padx=15, pady=5)
        self.btn_query.grid(row=len(self.queryFields), column=2, padx=15, pady=5)

    def item_click(self, event):
        pass

    def query(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

class LessonWindow(BaseWindow):
    def __init__(self):
        queryConfig=[["leson_no","课程编号"],["leson_name","课程名称"]]
        dataConfig=[
            ["leson_no","课程编号", 80, "center"],
            ["leson_name","课程名称", 120, "center"],
            ["leson_room", "上课地点", 120, "center"],
            ["leson_time", "上课时间", 120, "center"]
        ]
        super(LessonWindow, self).__init__(queryConfig, dataConfig)

    def layout(self):
        super().layout()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame_top = tk.Frame(width=600, height=90)
        self.frame_center = tk.Frame(width=600, height=180)
        self.frame_bottom = tk.Frame(width=600, height=90)
        self.lb_tip = tk.Label(self.frame_top, text="考试科目")
        self.string = tk.StringVar()
        self.string.set('')
        self.ent_find_name = tk.Entry(self.frame_top, textvariable=self.string)
        self.btn_query = tk.Button(self.frame_top, text="查询", command=self.query)
        self.lb_tip.grid(row=0, column=0, padx=15, pady=30)
        self.ent_find_name.grid(row=0, column=1, padx=15, pady=30)
        self.btn_query.grid(row=0, column=2, padx=15, pady=30)

        #self.btn_add = tk.Button(self.frame_bottom, text="添加", command=self.add)
        self.btn_add = tk.Button(self.frame_bottom, text="添加")
        self.btn_add.bind("<Button-1>", self.add_event)

        self.btn_update = tk.Button(self.frame_bottom, text="修改", command=self.update)
        self.btn_delete = tk.Button(self.frame_bottom, text="删除", command=self.delete)
        self.btn_add.grid(row=0, column=0, padx=15, pady=30)
        self.btn_update.grid(row=0, column=1, padx=15, pady=30)
        self.btn_delete.grid(row=0, column=2, padx=15, pady=30)


        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=("a", "b", "c", "d"))
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)
        self.tree.column("a", width=80, anchor="center")
        self.tree.column("b", width=120, anchor="center")
        self.tree.column("c", width=120, anchor="center")
        self.tree.column("d", width=120, anchor="center")

        self.tree.heading("a", text="课程编号")
        self.tree.heading("b", text="课程名称")
        self.tree.heading("c", text="上课地点")
        self.tree.heading("d", text="上课时间")
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

        #self.writer=pd.ExcelWriter("data.xls")
        self.data_frame = None
        self.item_selection = ""
        self.query()
        self.mainloop()

    def item_click(self, event):
        try:
            selection = self.tree.selection()[0]
            data = self.tree.item(selection, "values")
            self.item_selection = data[0]
        except IndexError:
            tkinter.messagebox.showinfo("警告", "范围异常，请重新选择！")

    def query(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        query_info = self.ent_find_name.get()
        self.string.set('')
        df = self.data_frame = pd.read_excel("data.xls")
        if query_info is None or query_info == "":
            pass
        else:
            df = self.data_frame.loc[df["课程名称"].str.contains(query_info)]
        for index, row in df.iterrows():
            data = [row["课程编号"], row["课程名称"], row["上课地点"], row["上课时间"]]
            self.tree.insert("", "end", values=data)

    def add_event(self, event):
        print(event.x, event.y)
        self.add()

    def add(self):
        dlg = LessonDialog(None)
        self.wait_window(dlg) #important!
        if dlg.group_info is not None:
            size = self.data_frame.index.size
            self.data_frame.loc[size] = dlg.group_info
            df_rows = self.data_frame.shape[0]
            self.data_frame.to_excel('data.xls', index=False)
            self.query()

    def update(self):
        pass

    def delete(self):
        if self.item_selection is None or self.item_selection == "":
            return
        if tkinter.messagebox.askyesno("提示", "是否删除？"):
            temp = self.data_frame.loc[self.data_frame["课程编号"]==self.item_selection]
            self.data_frame = self.data_frame.drop(index=temp.index)
            print(self.data_frame)
            self.data_frame.to_excel('data.xls', index=False)
            self.query()

    def load_data(self, data):
        pass

class LessonDialog(tk.Toplevel):
    def __init__(self, data):
        super().__init__()
        self.center_window(600,400)
        self.wm_attributes("-topmost", 1)
        self.protocol("WM_DELETE_WINDOW", self.donothing)  # 此语句用于捕获关闭窗口事件，用一个空方法禁止其窗口关闭。
        self.resizable(False, False)
        self.lesson_no = tk.StringVar()
        self.lesson_name = tk.StringVar()
        self.lesson_place = tk.StringVar()
        self.lesson_time = tk.StringVar()
        self.lesson_no.set('')
        self.lesson_name.set('')
        self.lesson_place.set('')
        self.lesson_time.set('')
        self.setup_ui()
        self.group_info = []

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.grid(row=0, column=0, padx=160, pady=20)
        tk.Label(row1, text='课程编号：', width=8).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.lesson_no, width=20).pack(side=tk.LEFT)

        row2 = tk.Frame(self)
        row2.grid(row=1, column=0, padx=160, pady=20)
        tk.Label(row2, text='课程名称：', width=8).pack(side=tk.LEFT)
        tk.Entry(row2, textvariable=self.lesson_name, width=20).pack(side=tk.LEFT)

        row3 = tk.Frame(self)
        row3.grid(row=2, column=0, padx=160, pady=20)
        tk.Label(row3, text='上课地点：', width=10).pack(side=tk.LEFT)
        tk.Entry(row3, textvariable=self.lesson_place, width=18).pack(side=tk.LEFT)

        row4 = tk.Frame(self)
        row4.grid(row=3, column=0, padx=160, pady=20)
        tk.Label(row4, text='上课时间：', width=8).pack(side=tk.LEFT)
        tk.Entry(row4, textvariable=self.lesson_time, width=20).pack(side=tk.LEFT)

        row5 = tk.Frame(self)
        row5.grid(row=4, column=0, padx=160, pady=20)
        tk.Button(row5, text="取消", command=self.cancel).grid(row=0, column=0, padx=60)
        tk.Button(row5, text="确定", command=self.ok).grid(row=0, column=1, padx=60)

    def center_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(size)

    def ok(self):
        self.group_info = [self.lesson_no.get(), self.lesson_name.get(), self.lesson_place.get(), self.lesson_time.get()]
        self.destroy()

    def cancel(self):
        self.group_info = None
        self.destroy()

    def donothing(self):
        pass

LessonWindow()