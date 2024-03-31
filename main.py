from tkinter import ttk, messagebox
import tkinter as tk
import sv_ttk
import subprocess
import webbrowser


class WindowLoader(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.Mainwindow()

    def Mainwindow(self):
        MainFrame = ttk.Frame(self, height=200, width=400)
        MainFrame.pack(side="top", anchor="n", padx=10, pady=10)
        #主容器
        Title = ttk.Label(MainFrame, text="CN Code-自研IDE",font=("微软雅黑", 20))
        Title.pack(anchor="n", padx=10, pady=10)
        #标题
        Text = ttk.Label(MainFrame, text="兼容VSCode",font=("微软雅黑", 15))
        Text.pack(anchor="n", padx=10, pady=20)
        #说明
        Start = ttk.Button(MainFrame, text="启动窗口", width=100, style="Accent.TButton")
        Start["command"] = self.Start
        Start.pack(anchor="n", padx=10, pady=15)
        #开始按钮
        MoreFrame = ttk.Frame(self, height=300, width=400)
        MoreFrame.pack(side="bottom", anchor="s", padx=10, pady=10)
        #底部按钮容器
        Option = ttk.Button(MoreFrame, text="设置", width=18)
        Option.pack(side="right", anchor="w", padx=10, pady=15)
        #设置
        Open = ttk.Button(MoreFrame, text="打开项目", width=18)
        Open.pack(side="left", anchor="e", padx=10, pady=15)
        #开启文件
        Option["command"] = self.Unknow
        Open["command"] = self.Unknow

    def Start(self):
        subprocess.run("CnIDE\\code.exe")

    def Unknow(self):
        No = messagebox.askyesno("您不是VIP", "您不是白金VIP,无法使用白金程序员尊享功能,请点击“YES”充值!")
        if No:
            webbrowser.open(url="https://space.bilibili.com/1858500718?spm_id_from=333.1007.0.0", new=2)
        else:
            messagebox.showerror("VIP", "服务器错误,即将跳转充值页面!")
            webbrowser.open(url="https://space.bilibili.com/1858500718?spm_id_from=333.1007.0.0", new=2)

    def Closing(self):
        for i  in range(2):
            Exit = messagebox.askyesno("QAQ","你真的要残忍关闭我吗?呜呜呜 QAQ")
            if Exit:
                Exit2 = messagebox.askyesno("不~","我不想离开你~")
                if Exit2:
                    Exit3 = messagebox.askyesno("提示","我们不希望你走,点击“YES”就可以免费获得VIP了!")
                    if Exit3:
                        Exit4 = messagebox.askyesno("404","啊哦!内容自己逃走了哦!但是你可以点击“YES”以获取更多福利")
                        if Exit4:
                            webbrowser.open(url="https://www.bilibili.com/video/BV1hq4y1s7VH/?spm_id_from=333.337.search-card.all.click",new=2)
                        else:
                            messagebox.showerror("笑了","你不能跑!")
                    else:
                        messagebox.showinfo("OK","好吧,你赢了!")
                        Window.destroy()
                        webbrowser.open(url="https://www.bilibili.com/video/BV1hq4y1s7VH/?spm_id_from=333.337.search-card.all.click",new=2)
                        break
            else:
                break
        Window.destroy()

Window = tk.Tk()
app = WindowLoader(master=Window)
Window.geometry("400x500")
Window.title("IDE")
Window.resizable(False, False)
Window.protocol("WM_DELETE_WINDOW", app.Closing)

sv_ttk.set_theme("light")
app.mainloop()