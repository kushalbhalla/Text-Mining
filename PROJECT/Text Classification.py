#######    MAIN GUI FILE . HERE IS DISGIN FOR USER BATTER UNDERSTANDABLE   ##################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from ttkthemes import themed_tk
import os
import Mainc
from PIL import ImageTk,Image
Model = Mainc.Classy()


fileName = ''
topicNo = 0
wordNo = 0
url = ''
title = ''
getTopic = 101

def StartWIn():

    root = themed_tk.ThemedTk()
    root.get_themes()
    root.set_theme('plastik')
    root.configure(bg='snow')
    root.title('Text Classifier')
    root.geometry('700x520')

    fn = Frame(root, bg='black')
    fn.place(x=270, y=10, width=150, height=150)

    img = ImageTk.PhotoImage(Image.open(r'web.jpg'))
    panel = Label(fn, image=img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    heading = Label(root, text='TEXT CLASSIFIER',bg='white', fg='black', font=("Helvetica", 22, "bold"))
    heading.place(x=220, y=160)

    fn = Frame(root, bg='black')
    fn.place(x=25, y=200, width=650, height=10)

    def sub():
        global fileName
        global topicNo
        global wordNo
        global Model


        if len(var1.get()) == 0 or len(c1.get()) == 0 or len(c2.get()) == 0:
            messagebox.showinfo('Error', 'Enter all values')

        else:
            fileName = var1.get()
            topicNo = var2.get()
            wordNo = var3.get()

            Model.Getdata(fileName,topicNo,wordNo)
            Model.MachineLearningModel()
            Model.save()
            root.destroy()
            SecondWin(fileName, topicNo, wordNo)




    def open_file():
        global url
        global title

        url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        fileName = os.path.basename(url)
        e1.insert(0, fileName)


    f1 = Frame(root, bd=7, relief='ridge', bg='OrangeRed2')
    f1.place(x=120, y=230, width=445, height=250)

    l1 = ttk.Label(f1, text='SELECT DATA FILE      : ', font=("Helvetica", 15, 'bold'), background='OrangeRed2')
    l1.place(x=10, y=25)

    var1 = StringVar()
    e1 = ttk.Entry(f1, textvariable=var1, font=("times new roman", 13))
    e1.place(x=250, y=25, height=25, width=170)

    btn2 = ttk.Button(f1, text='Open', command=open_file)
    btn2.place(x=340, y=60, height=25, width=80)

    l2 = ttk.Label(f1, text='ENTER AMOUNT OF TOPIC : ', font=("Helvetica", 15, 'bold'), background='OrangeRed2')
    l2.place(x=10, y=100)

    var2 = IntVar()
    c1 = ttk.Combobox(f1, values=tuple(range(1, 101)), textvariable=var2, state='readonly')
    c1.place(x=250, y=100, height=25, width=170)

    l3 = ttk.Label(f1, text='ENTER AMOUNT OF TAG   :', font=("Helvetica", 15, 'bold'), background='OrangeRed2')
    l3.place(x=10, y=140)

    var3 = IntVar()
    c2 = ttk.Combobox(f1, values=tuple(range(1, 101)), textvariable=var3, state='readonly')
    c2.place(x=250, y=140, height=25, width=170)

    btn1 = ttk.Button(f1, text='SUBMIT', command=sub)
    btn1.place(x=140, y=190, height=25, width=150)

    root.mainloop()




def SecondWin(fileName,topicNo,wordNo):

    root = themed_tk.ThemedTk()
    root.configure(bg='snow')
    root.get_themes()
    root.set_theme('plastik')
    root.geometry('830x640')

   
    def help():
        pass

    helpB = ttk.Button(root, text='HELP', command=help)
    helpB.place(x=690, y=30, height=25, width=100)

    fn = Frame(root, bg='black')
    fn.place(x=40, y=20, width=70, height=70)

    img = ImageTk.PhotoImage(Image.open(r'logo3.jpg'))
    panel = Label(fn, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    heading = Label(root, text='TEXT CLASSIFIER', bg='snow', fg='black', font=("Sans Bold", 40, "bold"))
    heading.place(x=140, y=20)

    fn = Frame(root, bg='black')
    fn.place(x=20, y=100, width=790, height=10)

    def sho():
        global Model
        selectedTopicToClassify = var4.get()
        Model.classification(selectedTopicToClassify)

    def chek():
        sentance = textValue.get("1.0","end-1c")
        print(sentance)
        getTopic = Model.SearchT(sentance)
        print(getTopic)

        text.set(str(getTopic))
    #
    def show():
        import os
        os.system("gedit " + 'cat.text')

    def See():
        Model.See()

    def Plot():
        print(word_amount.get())
        Model.pyTopicPlot(search_word.get(),word_amount.get())


    f2 = Frame(root, bd=7, relief='ridge', bg='#03befc')
    f2.place(x=25, y=125, width=370, height=240)

    f3 = Frame(root, bd=7, relief='ridge', bg='#CCCCFF')
    f3.place(x=25, y=375, width=370, height=240)

    f4 = Frame(root, bd=7, relief='ridge', bg='hot pink')
    f4.place(x=415, y=125, width=390, height=485)

    f5 = Frame(f4, bd=7, relief='ridge', bg='yellow green')
    f5.place(x=15, y=220, width=350, height=240)

    lf1 = ttk.Label(f2, text='ATTRIBUTES ', foreground='snow', background='#03befc',font=("Sans Bold", 18, 'bold'))
    lf1.place(x=100, y=5)

    lf1 = ttk.Label(f2, text='SELECTED FILE  :', foreground='snow', background='#03befc', font=("Helvetica", 17, 'bold'))
    lf1.place(x=20, y=50, width=200, height=25)

    ef1 = ttk.Label(f2, text=fileName, foreground='snow', background='#03befc', state='readonly',
                    font=("Helvetica", 17, 'bold'))
    ef1.place(x=220, y=50, width=100, height=25)

    lf2 = ttk.Label(f2, text='TOPIC NUMBER   :', foreground='snow', background='#03befc', font=("Helvetica", 17, 'bold'))
    lf2.place(x=20, y=100, width=200, height=25)

    ef2 = ttk.Label(f2, text=topicNo, foreground='snow', background='#03befc', state='readonly',
                    font=("Helvetica", 17, 'bold'))
    ef2.place(x=220, y=100, width=100, height=25)

    lf3 = ttk.Label(f2, text='TAGS IN TOPIC  :', foreground='snow', background='#03befc', font=("Helvetica", 17, 'bold'))
    lf3.place(x=20, y=150, width=200, height=25)

    ef3 = ttk.Label(f2, text=wordNo, foreground='snow', background='#03befc', state='readonly',
                    font=("Helvetica", 17, 'bold'))
    ef3.place(x=220, y=150, width=100, height=25)

    btnf3 = ttk.Button(f2, text='SHOW', command=show)
    btnf3.place(x=110, y=190, width=140, height=30)

    l1f3 = ttk.Label(f3, text='CLASSIFICATION OF DATA ', foreground='snow', background='#CCCCFF',
                     font=("Sans Bold", 18, 'bold'))
    l1f3.place(x=10, y=10, width=330, height=30)

    l2f3 = ttk.Label(f3, text='CHOOSE TOPIC NUMBER  : ', foreground='snow', background='#CCCCFF',
                     font=("Helvetica", 17, 'bold'))
    l2f3.place(x=20, y=80, width=250, height=25)

    var4 = IntVar()
    select = ttk.Combobox(f3, textvariable=var4, values=tuple(range(0, topicNo )))
    select.place(x=20, y=130, width=180, height=25)

    btnf3 = ttk.Button(f3, text='SAVE', command=sho)
    btnf3.place(x=120, y=180, width=140, height=30)

    l1f4 = ttk.Label(f4, text='PLOTS FOR TOPIC AND TAG \nRELATION VISUALIZATION ', foreground='snow',
                     background='hot pink', font=("Sans Bold", 18, 'bold'))
    l1f4.place(x=10, y=5)

    l1f4 = ttk.Label(f4, text='DOMINANT TOPIC :-', foreground='snow',background='hot pink', font=("Helvetica", 17, 'bold'))
    l1f4.place(x=10, y=80)

    l1f4 = ttk.Label(f4, text='TAG DENSITY    :-', foreground='snow',
                     background='hot pink', font=("Helvetica", 17, 'bold'))
    l1f4.place(x=10, y=130)

    btn2f4 = ttk.Button(f4, text='SHOW', command=See)
    btn2f4.place(x=220, y=80, height=25, width=135)

    search_word = StringVar()
    btn3f4 = ttk.Entry(f4, textvariable=search_word, font=("Sans Bold", 15))
    btn3f4.place(x=220, y=130, height=25, width=100)

    word_amount = IntVar()
    select = ttk.Combobox(f4, textvariable=word_amount, values=tuple(range(1, 26)))
    select.place(x=325, y=130, height=25, width=35)

    btn1f4 = ttk.Button(f4, text='PLOT', command=Plot)
    btn1f4.place(x=140, y=170, height=30, width=120)

    l1f5 = ttk.Label(f5, text='SEARCH SENTANCE', foreground='snow', background='yellow green',
                     font=("Snas Bold", 17, 'bold'))
    l1f5.place(x=50, y=5)

    l1f5 = ttk.Label(f5, text='ENTER SENTANSE', foreground='snow', background='yellow green',
                     font=("Helvetica", 17, 'bold'))
    l1f5.place(x=10, y=40)

    textValue = Text(f5, font=("Helvetica", 12, 'bold'))
    textValue.place(x=10, y=80, height=50, width=320)

    btn1f5 = ttk.Button(f5, text='CHECK', command=chek)
    btn1f5.place(x=10, y=140, height=30, width=120)

    l2f5 = ttk.Label(f5, text='CONNECTED TOPIC ', foreground='snow', background='yellow green',
                     font=("Helvetica", 17, 'bold'))
    l2f5.place(x=10, y=180, height=30, width=180)

    text = StringVar()
    text.set('')
    getTopicL = ttk.Label(f5, textvariable = text, foreground='black', background = 'snow')
    getTopicL.place(x=190, y=180, height=30, width=120)



    root.mainloop()


StartWIn()


