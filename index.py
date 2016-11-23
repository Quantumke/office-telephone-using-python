import tkinter
from tkinter import ttk
from sqlalchemy import *
from sqlalchemy import schema, types, Table, column, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
metadata = schema.MetaData()
import psycopg2
LARGE_FONT= ("Nexa Light", 12)

class GuiInit(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        container= tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for F in (LoginPage, Home):
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Home)
    def show_frame(self, count):
        frame=self.frames[count]
        frame.tkraise()

class LoginPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        self.login_gui()
    def login_gui(self):
        self.grid(column=0, row=0, sticky='nsew')
        self.username = ttk.Entry(self, width=5)
        self.username.grid(column=1, row=2)
        self.password = ttk.Entry(self, width=5)
        self.password.grid(column=3, row=2)
        self.submit_button = ttk.Button(self, text='Login', command=self.login)
        self.submit_button.grid(column=0, row=3, columnspan=4)
        self.status = ttk.LabelFrame(self, text='Status', height=100)
        self.status.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.status_label = ttk.Label(self.status, text='',font=LARGE_FONT)
        self.status_label.grid(column=0, row=0)

        ttk.Label(self, text='Login',font=LARGE_FONT).grid(column=0, row=0,
										   columnspan=4)
        ttk.Label(self, text='Username',font=LARGE_FONT).grid(column=0, row=2,
											  sticky='w')
        ttk.Label(self, text='Password',font=LARGE_FONT).grid(column=2, row=2,
											  sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
													  row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def login(self):
        u = str(self.username.get())
        p = str(self.password.get())
        engine = create_engine("postgresql://root:master12!@localhost:5432/office_tel")
        connection = engine.connect()
        engine.echo = True
        metadata.bind = engine
        users = Table('users', metadata, autoload=True)
        def destroy_window(parent, self):
            parent.destroy()
            self.destroy()

        def run(stmt):
            rs = stmt.execute()
            for row in rs:
                username = row.username
                password = row.password
                list = [username, password]
                success = len(list)
                Session = sessionmaker(bind=engine)
                session = Session()
                self.status_label['text'] = "Login successful!"
                self.submit_button['command'] = destroy_window(self,self)
                break
            else:
                self.status_label['text'] = "Wrong username or password"
        result = users.select(and_(users.c.username == u, users.c.password == p))
        run(result)

        
class Home(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.dailpad()
    def dailpad(self):
        self.grid(column=0, row=0, sticky='nsew')
        self.label=ttk.Label(self, text="Dail Pad", font=LARGE_FONT)
        self.label.grid(column=1, row=2)
        self.tel_lable=ttk.Label(self, text="", font=LARGE_FONT)
        self.tel_lable.grid(column=3, row=2)
        self.one = ttk.Button(self, text="1", command=self.one, width=5)
        self.one.grid(column=1, row=3)
        self.two = ttk.Button(self, text="2", command=self.two, width=5)
        self.two.grid(column=2, row=3)
        self.three = ttk.Button(self, text="3", command=self.three, width=5)
        self.three.grid(column=3, row=3)
        self.four = ttk.Button(self, text="4",command=self.four, width=5)
        self.four.grid(column=1, row=4)
        self.five = ttk.Button(self, text="5",command=self.five, width=5)
        self.five.grid(column=2, row=4)
        self.six = ttk.Button(self, text="6",command=self.six, width=5)
        self.six.grid(column=3, row=4)
        self.seven = ttk.Button(self, text="7",command=self.seven, width=5)
        self.seven.grid(column=1, row=5)
        self.eight = ttk.Button(self, text="8",command=self.eight, width=5)
        self.eight.grid(column=2, row=5)
        self.nine = ttk.Button(self, text="9",command=self.nine, width=5)
        self.nine.grid(column=3, row=5)
        self.zero = ttk.Button(self, text="0",command=self.zero, width=5)
        self.zero.grid(column=2, row=6)
        self.call_btn = ttk.Button(self, text="call",  width=10)
        self.call_btn.grid(column=3, row=7)
        self.end_call=ttk.Button(self, text="End Call",  width=10)
        self.end_call.grid(column=1, row=7)
        self.message_btn=ttk.Button(self, text="Msg", width=5)
        self.message_btn.grid(column=2, row=7)
      

    
        


app=GuiInit()
app.mainloop()
