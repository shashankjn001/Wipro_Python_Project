from tkinter import *
import mysql.connector



def save_info():
    
    kriType_info = kriType.get()
    cob_info = cob.get()
    riskIndicator_info = riskIndicator.get()
    srcSystem_info = srcSystem.get()
    feedLocation_info = feedLocation.get()


    print()
    
    print(kriType_info)
    print(cob_info)
    print(riskIndicator_info)
    print(srcSystem_info)
    print(feedLocation_info)


app = Tk()

app.geometry("500x500")

app.title("Feeds Input")

heading = Label(text="Feeds Input",bg="grey",fg="white",font="40",width="500",height="3")
heading.pack()
#-----------------------------------------------------------------------------------------------------------
#Lables

kriType_text = Label(text="KRI Type : ")
cob_text = Label(text="COB : ")
riskIndicator_text = Label(text="Risk Indicator : ")
srcSystem_text = Label(text="Source System : ")
feedLocation_text = Label(text="Feed Location : ")

kriType_text.place(x="15",y="100")
cob_text.place(x="15",y="150")
riskIndicator_text.place(x="15",y="200")
srcSystem_text.place(x="15",y="250")
feedLocation_text.place(x="15",y="300")

#------------------------------------------------------------------------------------------------------------
#FeedInput

kriType = StringVar()
cob = StringVar()
riskIndicator = StringVar()
srcSystem = StringVar()
feedLocation = StringVar()

kriType_entry = Entry(textvariable=kriType,width="30")
cob_entry = Entry(textvariable=cob,width="30")
riskIndicator_entry = Entry(textvariable=riskIndicator,width="30")
srcSystem_entry = Entry(textvariable=srcSystem,width="30")
feedLocation_entry = Entry(textvariable=feedLocation,width="30")

kriType_entry.place(x="115",y="103")
cob_entry.place(x="115",y="153")
riskIndicator_entry.place(x="115",y="203")
srcSystem_entry.place(x="115",y="253")
feedLocation_entry.place(x="115",y="303")

#----------------------------------------------------------------------------------------------------------
#Button

button = Button(app , text="Submit" , width="30" , height="2", bg="grey" , fg="white" , command=save_info)
button.place(x="35",y="370")


mainloop()
