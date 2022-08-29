from tkinter import *
from tkinter import ttk

class SMVC():
    def __init__(self,event):
        if n.get() == 'Phase 1':
            self.phase1()

    def phase1(self):
        windows2 = Toplevel()
        windows2.title('Compiler SMV (Phase 1)')
        windows2.geometry('%sx%s+%s+%s'%(450,350,int((screen_width/2)-(300/2)),int((screen_height/2)-(130/2))))
        wrapper2 = LabelFrame(windows2)

        canvas = Canvas(wrapper2)
        canvas.pack(side=LEFT,fill='both',)

        scrollbar_vertical = Scrollbar(wrapper2, orient='vertical', command=canvas.yview)
        scrollbar_vertical.pack(side=RIGHT, fill='both')

        canvas.configure(yscrollcommand=scrollbar_vertical.set)

        canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        frame=Frame(canvas)
        canvas.create_window((0,0), window=frame,anchor='nw')

        wrapper2.pack(fill='both',expand=Y,padx=10,pady=10)

        varTXRX = StringVar()
        label_TXRX = Label(frame,textvariable=varTXRX,bg='Light Blue')
        varTXRX.set('TX/RX')
        label_TXRX.pack(anchor='nw')

        str1 = self.str1 = StringVar(value=0)
        str2 = self.str2 = StringVar(value=0)
        str3 = self.str3 = StringVar(value=0)
        str4 = self.str4 = StringVar(value=0)
        str5 = self.str5 = StringVar(value=0)
        str6 = self.str6 = StringVar(value=0)
        str7 = self.str7 = StringVar(value=0)
        str8 = self.str8 = StringVar(value=0)
        str9 = self.str9 = StringVar(value=0)

        Button1 = Checkbutton(frame, text = "RX-DFE", 
                            variable = str1,
                            onvalue = 'AVK_SMV_1D_Disc-RXUDFE-Unmatch_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button2 = Checkbutton(frame, text = "RX-DQSCTLE", 
                            variable = str2,
                            onvalue = 'AVK_SMV_1D_Disc-RXDQSCTLE-Match_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button3 = Checkbutton(frame, text = "RX-BIAS", 
                            variable = str3,
                            onvalue = 'AVK_SMV_1D_Disc-RXBIAS_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button4 = Checkbutton(frame, text = "RX-BIASRLOAD", 
                            variable = str4,
                            onvalue = 'AVK_SMV_1D_Disc-RxBiasRload_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button5 = Checkbutton(frame, text = "TX-EQ", 
                            variable = str5,
                            onvalue = 'AVK_SMV_1D_Disc-TXEQ_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button6 = Checkbutton(frame, text = "RX-ODT", 
                            variable = str6,
                            onvalue = 'AVK_SMV_1D_Disc-RX-ODT_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button7 = Checkbutton(frame, text = "TX-RON", 
                            variable = str7,
                            onvalue = 'AVK_SMV_1D_Disc-TX-RON_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button8 = Checkbutton(frame, text = "TX-DQ-TCO", 
                            variable = str8,
                            onvalue = 'AVK_SMV_1D_Disc_TX-DQ-TCO_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button9 = Checkbutton(frame, text = "TX-DQS-TCO", 
                            variable = str9,
                            onvalue = 'AVK_SMV_1D_Disc_TX-DQS-TCO_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button1.pack()
        Button2.pack()
        Button3.pack()
        Button4.pack()
        Button5.pack()
        Button6.pack()
        Button7.pack()
        Button8.pack()
        Button9.pack()


        str10 = self.str10 = StringVar(value=0)
        str11 = self.str11 = StringVar(value=0)
        str12 = self.str12 = StringVar(value=0)
        str13 = self.str13 = StringVar(value=0)
        str14 = self.str14 = StringVar(value=0)
        str15 = self.str15 = StringVar(value=0)
        str16 = self.str16 = StringVar(value=0)
        str17 = self.str17 = StringVar(value=0)
        str18 = self.str18 = StringVar(value=0)
        str19 = self.str19 = StringVar(value=0)

        Button10 = Checkbutton(frame, text = "TX-EQ-CMD", 
                            variable = str10,
                            onvalue = 'AVK_SMV_1D_Disc-CMD_EQ_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button11 = Checkbutton(frame, text = "TXRX-WCK-TCO", 
                            variable = str11,
                            onvalue = 'AVK_SMV_1D_Disc_TXRXWCK_TCO_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button12 = Checkbutton(frame, text = "CLK-TCO", 
                            variable = str12,
                            onvalue = 'AVK_SMV_1D_Disc-CLK_TCO_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button13 = Checkbutton(frame, text = "CMD-TCO", 
                            variable = str13,
                            onvalue = 'AVK_SMV_1D_Disc-CMD_TCO_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button14 = Checkbutton(frame, text = "CMD-SlewRate", 
                            variable = str14,
                            onvalue = 'AVK_SMV_1D_Disc-CMD_SlewRate_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button15 = Checkbutton(frame, text = "CMD-RON", 
                            variable = str15,
                            onvalue = 'AVK_SMV_1D_Disc-CMD-RON_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button16 = Checkbutton(frame, text = "DRAM-CA-ODT", 
                            variable = str16,
                            onvalue = 'AVK_SMV_1D_Disc-DRAM-CA-ODT_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button17 = Checkbutton(frame, text = "DRAM-RON", 
                            variable = str17,
                            onvalue = 'AVK_SMV_1D_Disc-DRAM-RON_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button18 = Checkbutton(frame, text = "DRAM-DQ-ODT", 
                            variable = str18,
                            onvalue = 'AVK_SMV_1D_Disc-DRAM-DQ-ODT_LPR5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button19 = Checkbutton(frame, text = "DRAM-WCK-ODT", 
                            variable = str19,
                            onvalue = 'AVK_SMV_1D_Disc-DRAM-WCK-ODT_LP5.xlsx',
                            offvalue = '0',
                            height = 2,
                            width = 14,
                            anchor='w',
                            command=self.checkbox_input)

        Button19.pack(side=BOTTOM,anchor='w')
        Button18.pack(side=BOTTOM,anchor='w')
        Button17.pack(side=BOTTOM,anchor='w')
        Button16.pack(side=BOTTOM,anchor='w')
        Button15.pack(side=BOTTOM,anchor='w')
        Button14.pack(side=BOTTOM,anchor='w')
        Button13.pack(side=BOTTOM,anchor='w')
        Button12.pack(side=BOTTOM,anchor='w')
        Button11.pack(side=BOTTOM,anchor='w')
        Button10.pack(side=BOTTOM,anchor='w')
        
        varCCC = StringVar()
        label_CCC = Label(frame,textvariable=varCCC,bg='Light Blue')
        varCCC.set('CCC')
        label_CCC.pack(side=BOTTOM, anchor='w')

        run = Button(windows2,text='Continue',command=self.call_P1Plot)
        run.pack(side=BOTTOM, anchor='e', padx=10, pady=10)


    def checkbox_input(self):
        self.test_list = [self.str1.get(),self.str2.get(),self.str3.get(),self.str4.get(),self.str5.get(),self.str6.get(),self.str7.get(),self.str8.get(),self.str9.get(),
                            self.str10.get(),self.str11.get(),self.str12.get(),self.str13.get(),self.str14.get(),self.str15.get(),self.str16.get(),self.str17.get(),
                            self.str18.get(),self.str19.get()]
        print(self.test_list)

    def call_P1Plot(self):
        from main import main
        print('main function loaded')
        main(condition_list=self.test_list)

windows = Tk()
windows.title('Compiler SMV')
windows.config(background='white')

phase=Label(windows, text = "Phase: ", background='white',
          font = ("Times New Roman", 12))

n = StringVar()
phasechoosen = ttk.Combobox(windows, width = 30, textvariable = n)
phasechoosen['values'] = ('Phase 1',
                                    )
phase.grid(column=0,row=0,padx=20,sticky='w',pady=10)
phasechoosen.grid(column=0,row=0,sticky='w', padx=90,pady=10)
phasechoosen.bind("<<ComboboxSelected>>",SMVC)

screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()
windows.geometry('%sx%s+%s+%s'%(330,50,int((screen_width/2)-(300/2)),int((screen_height/2)-(300/2))))

windows.mainloop()