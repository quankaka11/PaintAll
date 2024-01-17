from tkinter import *
from tkinter import ttk
import turtle
from Cỏ_may_mắn import heart1
import tkinter
from PIL import Image, ImageTk
from Ironman import *
from ChonXanhLe import *

root = Tk()
root.title("Nam Moi May Man")
root.configure(bg = "black")

root.geometry('800x600')

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Thực hiện xác nhận đăng nhập tại đây (đơn giản là so sánh với giá trị cứng)
    if password == "yeube" and username == "quankaka":
        # Hiển thị thông báo đăng nhập thành công
        login_label.config(text="Đăng nhập thành công", fg="green")

        login_.pack_forget()
        # Hiển thị màn hình vẽ
        canvas.pack()
        delete_button.pack()
        
        Che.pack()
        Iron.pack()
        Co_may_man.pack()
        
    else:
        # Hiển thị thông báo đăng nhập thất bại
        password_entry.delete(0, tkinter.END)
        login_label.config(text="Sai mật khẩu hoặc tên đăng nhập", fg="red")


login_ = Frame(root, bg = "black")
login_.pack(pady = 20)

#hien thi
username_label = Label(login_, text="Tên hiển thị:", fg="white", bg="black")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = Entry(login_, bg="white")
username_entry.grid(row=0, column=1, padx=10, pady=10)

# mk
password_label = Label(login_, text="Mật khẩu:", fg="white", bg="black")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = Entry(login_, show="*", bg="white")
password_entry.grid(row=1, column=1, padx=10, pady=10)


login_button = Button(login_, text="Đăng nhập", command=login, bg="white")
login_button.grid(row=2, columnspan=2, pady=10)

login_label = Label(login_, text="", fg="white", bg="black")
login_label.grid(row=3, columnspan=2)

# Tạo một đối tượng Canvas trong cửa sổ Tkinter
canvas = Canvas(root, width=500, height=500, bg="black")

# Tạo một đối tượng Turtle sử dụng Canvas
t = turtle.RawTurtle(canvas)

# Tạo nút trong Tkinter để gọi hàm vẽ từ file
def draw_from_file(shape):
    if shape == "heart": 

        heart1("red",4,45,t)

        heart1("pink",4,-40,t)

        heart1("orange",4,-40,t)

        heart1("green",4,-40,t)
    elif shape == "iron":  
        Iron1(t)
    elif shape == "che" :
        Che1(t)
    else :
        t.clear()
        t.reset()
        
        
Iron = Button(root,text = "Iron",bg = "red",command=lambda: draw_from_file("iron"))
Che = Button(root,text = "Che",bg = "blue",command=lambda: draw_from_file("che"))
Co_may_man = Button(root,text = "Co_may_man",bg = "green",command=lambda: draw_from_file("heart"))

delete_button = Button(root, text="delete", command=lambda:draw_from_file("delete"), bg="white")


# Ẩn màn hình vẽ và nút khi chưa đăng nhập
canvas.pack_forget()

Che.pack_forget()
Iron.pack_forget()
Co_may_man.pack_forget()
delete_button.pack_forget()



root.mainloop()