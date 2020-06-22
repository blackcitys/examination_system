from typing import Any, Union, Tuple

import pymysql
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

global userId_input


# 录入成绩
def entry_mark_windows():
    def entry_mark():
        courseId = int(entry_courseId.get().strip())
        studentId = int(entry_studentId.get().strip())
        mark = int(entry_student_mark.get().strip())
        sql = 'insert into selectedcourse value(%d,%d,%d)' % (courseId, studentId, mark)
        cursor.execute(sql)
        tkinter.messagebox.showinfo("成功", "成绩录入成功")
        database.commit()

    window_entry_mark = Tk()
    window_entry_mark.title('录入成绩')
    window_entry_mark.geometry('300x400')

    # 课程ID
    Label(window_entry_mark, text="课程ID", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.2)
    entry_courseId = Entry(window_entry_mark)
    entry_courseId.place(relx=0.4, rely=0.2)
    # 学生ID
    Label(window_entry_mark, text="学生ID", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.4)
    entry_studentId = Entry(window_entry_mark)
    entry_studentId.place(relx=0.4, rely=0.4)
    # 学生成绩
    Label(window_entry_mark, text="学生成绩", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.6)
    entry_student_mark = Entry(window_entry_mark)
    entry_student_mark.place(relx=0.4, rely=0.6)
    # 确认按钮
    button_entry_mark = Button(window_entry_mark, text='录入成绩', relief='raised', command=lambda: entry_mark())
    button_entry_mark.place(relx=0.4, rely=0.8)

    window_entry_mark.mainloop()


# 查询教授课程
def inquire_teach_course():
    window_inquire_teach = Tk()
    window_inquire_teach.title('查询教授课程')
    window_inquire_teach.geometry('900x400')

    columns = ("课程ID", "课程名", "教师ID", "上课时间", "上课地点", "上课周期", "课程类型", "课程学分")
    treeview = ttk.Treeview(window_inquire_teach, height=18, show="headings", columns=columns)
    treeview.pack(side=TOP, fill=BOTH)

    # 设置每列宽度和对齐方式
    # 设置每列表头标题文本
    treeview.column("课程ID", width=100, anchor='center')
    treeview.heading("课程ID", text="课程ID")
    treeview.column("课程名", width=100, anchor='center')
    treeview.heading("课程名", text="课程名")
    treeview.column("教师ID", width=100, anchor='center')
    treeview.heading("教师ID", text="教师ID")
    treeview.column("上课时间", width=100, anchor='center')
    treeview.heading("上课时间", text="上课时间")
    treeview.column("上课地点", width=100, anchor='center')
    treeview.heading("上课地点", text="上课地点")
    treeview.column("上课周期", width=100, anchor='center')
    treeview.heading("上课周期", text="上课周期")
    treeview.column("课程类型", width=100, anchor='center')
    treeview.heading("课程类型", text="课程类型")
    treeview.column("课程学分", width=100, anchor='center')
    treeview.heading("课程学分", text="课程学分")

    cursor.execute('select * from course where teacherID = %d' % int(userId_input))
    all_teach_course = cursor.fetchall()

    for i in range(len(all_teach_course)):
        treeview.insert('', i, values=all_teach_course[i])

    window_inquire_teach.mainloop()


# 教师界面
def run_teacher_windows():
    window_teacher = Tk()
    window_teacher.title('教师')
    window_teacher.geometry('200x400')

    button_entry_mark = Button(text='录入成绩', relief='raised', command=lambda: entry_mark_windows())
    button_entry_mark.place(relx='0.4', rely='0.4')
    button_inquire_course = Button(text='查询教授课程', relief='raised', command=lambda: inquire_teach_course())
    button_inquire_course.place(relx='0.32', rely='0.6')

    window_teacher.mainloop()


# 查询成绩
def inquire_course_window():
    window_inquire_course = Tk()
    window_inquire_course.title('查询成绩')
    window_inquire_course.geometry('900x400')

    columns = ("课程ID", "课程名", "教师ID", "上课时间", "上课地点", "上课周期", "课程类型", "课程学分", "课程成绩")
    treeview = ttk.Treeview(window_inquire_course, height=18, show="headings", columns=columns)
    treeview.pack(side=LEFT, fill=BOTH)

    # 设置每列宽度和对齐方式
    # 设置每列表头标题文本
    treeview.column("课程ID", width=100, anchor='center')
    treeview.heading("课程ID", text="课程ID")
    treeview.column("课程名", width=100, anchor='center')
    treeview.heading("课程名", text="课程名")
    treeview.column("教师ID", width=100, anchor='center')
    treeview.heading("教师ID", text="教师ID")
    treeview.column("上课时间", width=100, anchor='center')
    treeview.heading("上课时间", text="上课时间")
    treeview.column("上课地点", width=100, anchor='center')
    treeview.heading("上课地点", text="上课地点")
    treeview.column("上课周期", width=100, anchor='center')
    treeview.heading("上课周期", text="上课周期")
    treeview.column("课程类型", width=100, anchor='center')
    treeview.heading("课程类型", text="课程类型")
    treeview.column("课程学分", width=100, anchor='center')
    treeview.heading("课程学分", text="课程学分")
    treeview.column("课程成绩", width=100, anchor='center')
    treeview.heading("课程成绩", text="课程成绩")

    cursor.execute('select * from selectedcourse where studentID = %d' % int(userId_input))
    data = cursor.fetchall()

    for i in range(len(data)):
        cursor.execute('select * from course where courseID = %d' % data[i][0])
        temp = (data[i][2],)
        info = cursor.fetchone() + temp
        # treeview.insert('', i, values=(info, data[i][2]))
        treeview.insert('', i, values=info)

    window_inquire_course.mainloop()


# 学生选课
def choose_course_window():
    def selectTree(event):
        for item in treeview.selection():
            item_text = treeview.item(item, "values")

    def choose_course():
        selected_item = treeview.item(treeview.selection(), "values")
        cursor.execute('select * from selectedcourse where studentID = %d' % int(userId_input))
        all_selected_course = cursor.fetchall()
        for course in all_selected_course:
            if selected_item[0] == course[0]:
                tkinter.messagebox.showerror("错误", "已选过该课程")
                return
            else:
                courseId = int(selected_item[0])
                studentId = int(userId_input)
                sql = 'insert into selectedcourse (courseID,studentID) value(%d,%d)' % (courseId, studentId)
                cursor.execute(sql)
                database.commit()
                tkinter.messagebox.showinfo("成功", "选课成功")

    window_choose_course = Tk()
    window_choose_course.title('学生选课')
    window_choose_course.geometry('900x500')
    columns = ("课程ID", "课程名", "教师ID", "上课时间", "上课地点", "上课周期", "课程类型", "课程学分")
    treeview = ttk.Treeview(window_choose_course, height=18, show="headings", columns=columns)
    treeview.pack(side=TOP, fill=BOTH)

    # 设置每列宽度和对齐方式
    # 设置每列表头标题文本
    treeview.column("课程ID", width=100, anchor='center')
    treeview.heading("课程ID", text="课程ID")
    treeview.column("课程名", width=100, anchor='center')
    treeview.heading("课程名", text="课程名")
    treeview.column("教师ID", width=100, anchor='center')
    treeview.heading("教师ID", text="教师ID")
    treeview.column("上课时间", width=100, anchor='center')
    treeview.heading("上课时间", text="上课时间")
    treeview.column("上课地点", width=100, anchor='center')
    treeview.heading("上课地点", text="上课地点")
    treeview.column("上课周期", width=100, anchor='center')
    treeview.heading("上课周期", text="上课周期")
    treeview.column("课程类型", width=100, anchor='center')
    treeview.heading("课程类型", text="课程类型")
    treeview.column("课程学分", width=100, anchor='center')
    treeview.heading("课程学分", text="课程学分")
    # 确认按钮
    button_choose_course = Button(window_choose_course, text="选择课程", command=lambda: choose_course())
    button_choose_course.pack(side=BOTTOM)

    cursor.execute('select * from course')
    all_courses = cursor.fetchall()

    for i in range(len(all_courses)):
        cursor.execute('select * from course where courseID = %d' % all_courses[i][0])
        temp = (all_courses[i][2],)
        info = cursor.fetchone() + temp
        treeview.insert('', i, values=info)


# 学生界面
def run_student_windows():
    window_student = Tk()
    window_student.title('学生')
    window_student.geometry('200x400')

    inquire_button = Button(text='查询成绩', relief='raised', command=inquire_course_window)
    inquire_button.place(relx='0.4', rely='0.4')
    choose_button = Button(text='学生选课', relief='raised', command=choose_course_window)
    choose_button.place(relx='0.4', rely='0.6')

    window_student.mainloop()


# 添加用户
def add_user_windows():
    def add_user():
        input_role = combobox_choose_user.current()
        input_userId = int(entry_userId.get().strip())
        input_username = entry_username.get().strip()
        input_sex = entry_sex.get().strip()
        input_password = entry_password.get().strip()
        # 如果是教师
        if input_role == 0:
            cursor.execute('insert into teacher value(%d,"%s","%s")' % (
                input_userId, input_username, input_sex))
            cursor.execute('insert into userlogin(userName,password,role) value("%s","%s",%d)' % (
                input_userId, input_password, input_role + 1))
        # 如果是学生
        elif input_role == 1:
            cursor.execute('insert into student value(%d,"%s","%s")' % (
                input_userId, input_username, input_sex))
            cursor.execute('insert into userlogin(userName,password,role) value("%s","%s",%d)' % (
                input_userId, input_password, input_role + 1))
        tkinter.messagebox.showinfo("添加成功", "添加成功")
        database.commit()

    window_add_user = Tk()
    window_add_user.title('增加用户')
    window_add_user.geometry('400x400')

    # 选择角色
    Label(window_add_user, text="角色:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.2)
    combobox_choose_user = ttk.Combobox(window_add_user, values=['教师', '学生'], width=17)
    combobox_choose_user.place(relx=0.4, rely=0.2)
    # 用户ID
    Label(window_add_user, text="用户ID:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.3)
    entry_userId = Entry(window_add_user)
    entry_userId.place(relx=0.4, rely=0.3)
    # 用户名
    Label(window_add_user, text="用户名:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.4)
    entry_username = Entry(window_add_user)
    entry_username.place(relx=0.4, rely=0.4)
    # 性别
    Label(window_add_user, text="性别:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.5)
    entry_sex = Entry(window_add_user)
    entry_sex.place(relx=0.4, rely=0.5)
    # 登录密码
    Label(window_add_user, text="登录密码:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.6)
    entry_password = Entry(window_add_user)
    entry_password.place(relx=0.4, rely=0.6)
    # 确认按钮
    button_add_user = Button(window_add_user, text='添加用户', relief='raised',
                             command=lambda: add_user()).place(relx=0.4, rely=0.7)

    window_add_user.mainloop()


# 删除用户
def delete_user_window():
    def delete_user():
        selected_item = treeview.item(treeview.selection(), "values")
        if selected_item[3] == "学生":
            delete_sql = 'delete from student where userID=%d' % int(selected_item[0])
            cursor.execute(delete_sql)
            delete_sql = 'delete from student where userName="%s"' % selected_item[0]
            cursor.execute(delete_sql)
            delete_sql = 'delete from userlogin where userID=%d' % int(selected_item[0])
            cursor.execute(delete_sql)
            delete_sql = 'delete from userlogin where userName="%s"' % selected_item[0]
            cursor.execute(delete_sql)
            database.commit()
            treeview.delete(treeview.selection())
        elif selected_item[3] == "教师":
            delete_sql = 'delete from teacher where userID=%d' % int(selected_item[0])
            cursor.execute(delete_sql)
            delete_sql = 'delete from student where userName="%s"' % selected_item[0]
            cursor.execute(delete_sql)
            delete_sql = 'delete from userlogin where userID=%d' % int(selected_item[0])
            cursor.execute(delete_sql)
            delete_sql = 'delete from userlogin where userName="%s"' % selected_item[0]
            cursor.execute(delete_sql)
            database.commit()
            treeview.delete(treeview.selection())

    window_delete_user = Tk()
    window_delete_user.title('删除用户')
    window_delete_user.geometry('500x450')

    columns = ("用户ID", "用户名", "性别", "用户类型")
    treeview = ttk.Treeview(window_delete_user, height=18, show="headings", columns=columns)
    treeview.pack(side=TOP, fill=BOTH)

    # 设置每列宽度和对齐方式
    # 设置每列表头标题文本
    treeview.column("用户ID", width=100, anchor='center')
    treeview.heading("用户ID", text="用户ID")
    treeview.column("用户名", width=100, anchor='center')
    treeview.heading("用户名", text="用户名")
    treeview.column("性别", width=100, anchor='center')
    treeview.heading("性别", text="性别")
    treeview.column("用户类型", width=100, anchor='center')
    treeview.heading("用户类型", text="用户类型")

    user_num = 0
    # 从学生表获取数据
    sql = 'select * from student'
    cursor.execute(sql)
    all_student = cursor.fetchall()
    for i in range(len(all_student)):
        role = ('学生',)
        info = all_student[i] + role
        treeview.insert('', user_num, values=info)
        user_num = user_num + 1

    # 从教师表获取数据
    sql = 'select * from teacher'
    cursor.execute(sql)
    all_teacher = cursor.fetchall()
    for i in range(len(all_teacher)):
        role = ('教师',)
        info = all_teacher[i] + role
        treeview.insert('', user_num, values=info)
        user_num = user_num + 1

    # 确认按钮
    button_choose_course = Button(window_delete_user, text="删除用户", command=lambda: delete_user())
    button_choose_course.pack(side=BOTTOM)


# 添加课程
def add_course_window():
    def add_course():
        courseId = int(entry_courseId.get().strip())
        course_name = entry_course_name.get().strip()
        teacherId = int(entry_teacherId.get().strip())
        course_time = entry_course_time.get().strip()
        course_room = entry_course_room.get().strip()
        course_week = int(entry_course_week.get().strip())
        course_type = entry_course_type.get().strip()
        course_score = int(entry_course_score.get().strip())

        sql = 'insert into course value (%d,"%s",%d,"%s","%s",%d,"%s",%d)' % \
              (courseId, course_name, teacherId, course_time, course_room, course_week, course_type, course_score)
        cursor.execute(sql)
        database.commit()
        tkinter.messagebox.showinfo("添加成功", (
            courseId, course_name, teacherId, course_time, course_room, course_week, course_type, course_score))

    # columns = ("课程ID", "课程名", "教师ID", "上课时间", "上课地点", "上课周期", "课程类型", "课程学分")
    window_delete_user = Tk()
    window_delete_user.title('添加课程')
    window_delete_user.geometry('400x450')

    # 课程ID
    Label(window_delete_user, text="课程ID:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.1)
    entry_courseId = Entry(window_delete_user)
    entry_courseId.place(relx=0.4, rely=0.1)
    # 课程名
    Label(window_delete_user, text="课程名:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.2)
    entry_course_name = Entry(window_delete_user)
    entry_course_name.place(relx=0.4, rely=0.2)
    # 教师ID
    Label(window_delete_user, text="教师ID:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.3)
    entry_teacherId = Entry(window_delete_user)
    entry_teacherId.place(relx=0.4, rely=0.3)
    # 上课时间
    Label(window_delete_user, text="上课时间:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.4)
    entry_course_time = Entry(window_delete_user)
    entry_course_time.place(relx=0.4, rely=0.4)
    # 上课地点
    Label(window_delete_user, text="上课地点:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.5)
    entry_course_room = Entry(window_delete_user)
    entry_course_room.place(relx=0.4, rely=0.5)
    # 上课周期
    Label(window_delete_user, text="上课周期:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.6)
    entry_course_week = Entry(window_delete_user)
    entry_course_week.place(relx=0.4, rely=0.6)
    # 课程类型
    Label(window_delete_user, text="课程类型:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.7)
    entry_course_type = Entry(window_delete_user)
    entry_course_type.place(relx=0.4, rely=0.7)
    # 课程学分
    Label(window_delete_user, text="课程学分:", font='Arial 12 bold', width=10, height=1).place(relx=0.1, rely=0.8)
    entry_course_score = Entry(window_delete_user)
    entry_course_score.place(relx=0.4, rely=0.8)

    # 确认按钮
    button_add_user = Button(window_delete_user, text='添加课程', relief='raised',
                             command=lambda: add_course()).place(relx=0.45, rely=0.9)

    window_delete_user.mainloop()


# 删除课程
def delete_course_window():
    def delete_course():
        selected_item = treeview.item(treeview.selection(), "values")
        delete_sql = 'delete from selectedcourse where courseID=%d' % int(selected_item[0])
        cursor.execute(delete_sql)
        delete_sql = 'delete from course where courseID=%d' % int(selected_item[0])
        cursor.execute(delete_sql)
        database.commit()
        treeview.delete(treeview.selection())
        tkinter.messagebox.showinfo("删除成功", "删除成功")

    # columns = ("课程ID", "课程名", "教师ID", "上课时间", "上课地点", "上课周期", "课程类型", "课程学分")
    window_delete_course = Tk()
    window_delete_course.title('删除课程')
    window_delete_course.geometry('900x500')

    columns = ("课程ID", "课程名", "教师ID", "上课时间", "上课地点", "上课周期", "课程类型", "课程学分")
    treeview = ttk.Treeview(window_delete_course, height=18, show="headings", columns=columns)
    treeview.pack(side=TOP, fill=BOTH)

    # 设置每列宽度和对齐方式
    # 设置每列表头标题文本
    treeview.column("课程ID", width=100, anchor='center')
    treeview.heading("课程ID", text="课程ID")
    treeview.column("课程名", width=100, anchor='center')
    treeview.heading("课程名", text="课程名")
    treeview.column("教师ID", width=100, anchor='center')
    treeview.heading("教师ID", text="教师ID")
    treeview.column("上课时间", width=100, anchor='center')
    treeview.heading("上课时间", text="上课时间")
    treeview.column("上课地点", width=100, anchor='center')
    treeview.heading("上课地点", text="上课地点")
    treeview.column("上课周期", width=100, anchor='center')
    treeview.heading("上课周期", text="上课周期")
    treeview.column("课程类型", width=100, anchor='center')
    treeview.heading("课程类型", text="课程类型")
    treeview.column("课程学分", width=100, anchor='center')
    treeview.heading("课程学分", text="课程学分")

    # 确认按钮
    button_delete_course = Button(window_delete_course, text="删除课程", command=lambda: delete_course())
    button_delete_course.pack(side=BOTTOM)

    cursor.execute('select * from course')
    all_courses = cursor.fetchall()

    for i in range(len(all_courses)):
        treeview.insert('', i, values=all_courses[i])

    window_delete_course.mainloop()


# 管理员界面
def run_admin_window():
    window_admin = Tk()
    window_admin.title('管理员')
    window_admin.geometry('200x400')

    add_button = Button(text='增加用户', relief='raised', command=lambda: add_user_windows())
    add_button.place(relx='0.4', rely='0.1')
    delete_button = Button(text='删除用户', relief='raised', command=lambda: delete_user_window())
    delete_button.place(relx='0.4', rely='0.3')
    alter_button = Button(text='添加课程', relief='raised', command=lambda: add_course_window())
    alter_button.place(relx='0.4', rely='0.5')
    search_button = Button(text='删除课程', relief='raised', command=lambda: delete_course_window())
    search_button.place(relx='0.4', rely='0.7')

    window_admin.mainloop()


# 登录
def login():
    global userId_input
    userId_input = entry_userId_input.get().strip()
    password_input = entry_password_input.get().strip()
    # 根据输入的用户名和密码查询数据库
    cursor.execute('select * from userlogin where userName = "%s" and password = "%s"'
                   % (userId_input, password_input))
    login_data = cursor.fetchone()
    # 如果获没有获取到数据
    if login_data is None:
        tkinter.messagebox.showerror("Error", "用户名或密码错误")
    # login_data[3]为role role==0 为管理员
    elif login_data[3] == 0:
        print("管理员登录" + str(login_data))
        window_login.destroy()
        # 转到管理员界面
        run_admin_window()
    # login_data[3]为role role==1 为教师
    elif login_data[3] == 1:
        print("教师登录" + str(login_data))
        window_login.destroy()
        # 转到教师界面
        run_teacher_windows()
    # login_data[3]为role role==2 为学生
    elif login_data[3] == 2:
        print("学生登录" + str(login_data))
        window_login.destroy()
        # 转到学生界面
        run_student_windows()


if __name__ == "__main__":
    # 连接数据库
    database = pymysql.connect(host='localhost', port=3306, user='newroot', passwd='root', db='examination_system',
                               charset='utf8')
    cursor = database.cursor()
    if not database.open:
        raise Exception("数据库连接失败")

    # 初始化Tk()
    window_login = Tk()
    # 设置标题
    window_login.title('教务管理系统登陆')
    window_login.geometry('300x200')
    # 创建一个标签，显示文本
    Label(window_login, text="用户名:", font='Arial 12 bold', width=10, height=1).place(relx=0.10, rely=0.3)
    Label(window_login, text="密码:", font='Arial 12 bold', width=10, height=1).place(relx=0.10, rely=0.5)

    entry_userId_input = Entry(window_login)  # 用户名
    entry_password_input = Entry(window_login)  # 密码
    entry_userId_input.place(relx=0.45, rely=0.3)
    entry_password_input.place(relx=0.45, rely=0.5)

    button_login = Button(text='登陆', relief='raised', command=login)
    button_login.place(relx=0.5, rely=0.7)
    # 进入消息循环
    window_login.mainloop()
