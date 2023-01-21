from tkinter import *

def sql_login_info():
    userName_info = userName.get()
    password_info = password.get()
    hostName_info = hostName.get()
    port_info = port.get()
    serviceName_info = serviceName.get()
        
    print(userName_info)
    print(password_info)
    print(hostName_info)
    print(port_info)
    print(serviceName_info)
    
  

app = Tk()

app.geometry("500x500")

app.title("SQL Server Login")

heading = Label(text="SQL Server Login",bg="grey",fg="white",font="40",width="500",height="3")
heading.pack()
#-----------------------------------------------------------------------------------------------------------
#Labels

userName_text = Label(text="User Name : ")
password_text = Label(text="Password : ")
hostName_text = Label(text="Host Name : ")
port_text = Label(text="Port : ")
serviceName_text = Label(text="Service Name : ")

userName_text.place(x="15",y="100")
password_text.place(x="15",y="150")
hostName_text.place(x="15",y="200")
port_text.place(x="15",y="250")
serviceName_text.place(x="15",y="300")


#-----------------------------------------------------------------------------------------------------------
#SQLEntry

userName = StringVar()
password = StringVar()
hostName = StringVar()
port = IntVar()
serviceName = StringVar()

userName_entry = Entry(textvariable=userName,width="30")
password_entry = Entry(textvariable=password,width="30")
hostName_entry = Entry(textvariable=hostName,width="30")
port_entry = Entry(textvariable=port,width="30")
serviceName_entry = Entry(textvariable=serviceName,width="30")

userName_entry.place(x="115",y="103")
password_entry.place(x="115",y="153")
hostName_entry.place(x="115",y="203")
port_entry.place(x="115",y="253")
serviceName_entry.place(x="115",y="303")


#-----------------------------------------------------------------------------------------------------------
#Button

button = Button(app , text="Submit" , width="30" , height="2", bg="grey" , fg="white" , command=sql_login_info)
button.place(x="35",y="370")


mainloop()