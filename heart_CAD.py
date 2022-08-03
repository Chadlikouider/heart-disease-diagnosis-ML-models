"""

w@author: CHADLI KOUIDER
Written : Saturday,May 28th 2022
Email: chadli_kouider@hotmail.com
       chadkouider@gmail.com
"""
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from csv import DictWriter
from HeartModel import main
import pandas as pd
import numpy as np
import os.path
# Background colors
bg_color_1 = "#F0F0F0"
bg_color_2 = "#FFFFFF"



# Create the window
root = tk.Tk()
root.columnconfigure(0 , weight = 1)
root.configure(background='red')
# Set a Title
root.title("Doctor heart")
root.iconbitmap("heart_icon.ico")
photo1 = tk.PhotoImage(file="Save_icon.png")
photo2 = tk.PhotoImage(file="sensor_icon.png")
photo_save = photo1.subsample(6,6)
photo_sensor = photo2.subsample(12,12)
# add a page (Create a notebook)
notebook = ttk.Notebook(root)
notebook.pack(pady = 10, expand = True)

# Create the Frames
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame1.grid(padx=10, sticky=(tk.E + tk.W))
frame1.pack(fill = 'both', expand = True)
frame2.pack(fill = 'both', expand = True)
# Add frame to notebook
notebook.add(frame1, text = "Data")
notebook.add(frame2, text = "Records")

# ---------------GUI Start------------------#
p_info = ttk.LabelFrame(frame1, text = "The data measured on the patient")
p_info.grid(sticky=(tk.W + tk.E))

# TextBox Age
labelText1 = tk.StringVar()
labelText1.set("Age :")
ttk.Label(p_info, width=7, textvariable=labelText1, justify='left').grid(column=0, row=0,sticky=(tk.W + tk.E))

age = tk.DoubleVar()
tk.Entry(p_info, textvariable=age, width=4, justify='left', highlightbackground=bg_color_1, background=bg_color_2).grid(
    column=1, row=0, sticky=(tk.W + tk.E))

labelUnit1 = tk.Label(p_info, text="Years", anchor='w', width=5, justify='right', background=bg_color_1)
labelUnit1.grid(column=2, row=0, sticky=(tk.W + tk.E))

ttk.Separator(p_info, orient='horizontal').grid(row=1,columnspan=3 ,sticky=(tk.W + tk.E))

# Bottons for Male/female
labelText2 = tk.StringVar()
labelText2.set("Sex :")
ttk.Label(p_info, width=16, textvariable=labelText2, justify='left').grid(column=0, row=2)

sex = tk.StringVar()
sex.set('0.0')
tk.Radiobutton(p_info, text="Female", variable=sex, value='0.0', width=12, justify='left', background=bg_color_1).grid(
    column=1, row=2, sticky='W')
tk.Radiobutton(p_info, text="Male", variable=sex, value='1.0', width=12, justify='left', background=bg_color_1).grid(
    column=2, row=2, sticky='W')

ttk.Separator(p_info, orient='horizontal').grid(row=3, columnspan=3, sticky=(tk.W + tk.E))

# botton for chest pain type
labelText3 = tk.StringVar()
labelText3.set("Chest pain type")
ttk.Label(p_info, width=16, textvariable=labelText3, justify='left').grid(column=0, row=4, rowspan=2)

chestPain = tk.StringVar()
chestPain.set('1.0')
tk.Radiobutton(p_info, text="Typical angina", variable=chestPain, value='1.0', justify='left',
               background=bg_color_1).grid(column=1, row=4, sticky=(tk.W + tk.E))
tk.Radiobutton(p_info, text="Atypical angina", variable=chestPain, value='2.0', justify='left',
               background=bg_color_1).grid(column=2, row=4, sticky=(tk.W + tk.E))
tk.Radiobutton(p_info, text="Non-anginal pain", variable=chestPain, value='3.0', justify='left',
               background=bg_color_1).grid(column=1, row=5, sticky=(tk.W + tk.E))
tk.Radiobutton(p_info, text="Asymptomatic", variable=chestPain, value='4.0', justify='left',
               background=bg_color_1).grid(column=2, row=5, sticky=(tk.W + tk.E))

ttk.Separator(p_info, orient='horizontal').grid(row=6, columnspan=3, sticky=(tk.W + tk.E))

# TextBox blood pressure
labelText4 = tk.StringVar()
labelText4.set("Resting blood pressure :")
ttk.Label(p_info, width=21, textvariable=labelText4, justify='left').grid(column=0, row=7)

blood_pressure = tk.DoubleVar()
tk.Entry(p_info, textvariable=blood_pressure, width=2, justify='left', highlightbackground=bg_color_1,
         background=bg_color_2).grid(column=1, row=7, sticky=(tk.W + tk.E))

labelUnit4 = tk.Label(p_info, text="mmHg", anchor='w', width=8, justify='right', background=bg_color_1)
labelUnit4.grid(column=2, row=7)

ttk.Separator(p_info, orient='horizontal').grid(row=8, columnspan=3, sticky=(tk.W + tk.E))

# TextBox serum cholestoral in mg/dl
labelText5 = tk.StringVar()
labelText5.set("Serum cholestoral :")
ttk.Label(p_info, textvariable=labelText5, justify='left').grid(column=0, row=9)

serum_chol = tk.DoubleVar()
tk.Entry(p_info, textvariable=serum_chol, width=8, justify='left', highlightbackground=bg_color_1,
         background=bg_color_2).grid(column=1, row=9, sticky=(tk.W + tk.E))

labelUnit5 = tk.Label(p_info, text="mg/dL", anchor='w', width=8, justify='right', background=bg_color_1)
labelUnit5.grid(column=2, row=9)

ttk.Separator(p_info, orient='horizontal').grid(row=10, columnspan=3, sticky=(tk.W + tk.E))
#TextBox fasting blood sugar
labelText6 = tk.StringVar()
labelText6.set("Fasting blood sugar :")
ttk.Label(p_info, width=18, textvariable=labelText6, justify='left').grid(column=0, row=11)

fbs = tk.DoubleVar()

tk.Radiobutton(p_info, text="> 120 mg/dL", variable=fbs, value='1.0', justify='left', background=bg_color_1).grid(
    column=1, row=11, sticky='NW')
tk.Radiobutton(p_info, text="< 120 mg/dL", variable=fbs, value='0.0', justify='left', background=bg_color_1).grid(
    column=2, row=11, sticky=(tk.W + tk.E))

ttk.Separator(p_info, orient='horizontal').grid(row=12, columnspan=3, sticky=(tk.W + tk.E))

# #Botton resting electrocardiographic results
labelText7 = tk.StringVar()
labelText7.set("Resting electro-\ncardiographic results :")
ttk.Label(p_info, width=19, textvariable=labelText7, justify='left').grid(column=0, row=13)

rec_result = tk.StringVar()
rec_result.set('0.0')
tk.Radiobutton(p_info, text="Normal", variable=rec_result, value='0.0', justify='left', background=bg_color_1).grid(
    column=1, row=13, sticky=(tk.W + tk.E))
#Having ST-T wave abnormality (T wave inversions and/or \n ST elevation or depression of > 0.05 mV)"
tk.Radiobutton(p_info, text="Having ST-T wave abnormality (T wave inversions and/or \nST elevation or depression of > 0.05 mV)", variable=rec_result, value='1.0', justify='left',
               background=bg_color_1).grid(column=1, row=14, sticky=(tk.W + tk.E))
tk.Radiobutton(p_info, text="Showing probable or definite left ventricular\n hypertrophy by Estes' criteria", variable=rec_result, value='2.0', justify='left',
               background=bg_color_1).grid(column=1, row=15, sticky=(tk.W + tk.E))

ttk.Separator(p_info, orient='horizontal').grid(row=16, columnspan=3, sticky=(tk.W + tk.E))

# TextBox maximum heart rate achieved
labelText8 = tk.StringVar()
labelText8.set("Maximum heart rate achieved ")
ttk.Label(p_info, textvariable=labelText8, justify='left').grid(column=0, row=17)

thalach = tk.DoubleVar()
tk.Entry(p_info, textvariable=thalach, width=8, justify='left', highlightbackground=bg_color_1, background=bg_color_2).grid(
    column=1, row=17, sticky=(tk.W + tk.E))

labelUnit8 = tk.Label(p_info, text="bts/min", anchor='w', width=8, justify='right', background=bg_color_1)
labelUnit8.grid(column=2, row=17)

ttk.Separator(p_info, orient='horizontal').grid(row=18, columnspan=3, sticky=(tk.W + tk.E))

#Bouton exercise induced angina
labelText9 = tk.StringVar()
labelText9.set("Exercise induced angina :")
ttk.Label(p_info, textvariable=labelText9, justify='left', background=bg_color_1).grid(column=0, row=19)

exang = tk.StringVar()
exang.set("1.0")
tk.Radiobutton(p_info, text="Yes", variable=exang, value='1.0', justify='left', background=bg_color_1).grid(
    column=1, row=19, sticky='NW')
tk.Radiobutton(p_info, text="No", variable=exang, value='0.0', justify='left', background=bg_color_1).grid(
    column=2, row=19, sticky='NW')

ttk.Separator(p_info, orient='horizontal').grid(row=20, columnspan=3, sticky="ew")

# TextBox ST depression induced by exercise relative to rest
labelText10 = tk.StringVar()
labelText10.set("ST depression induced by \nexercise relative to rest :")
ttk.Label(p_info, width=23, textvariable=labelText10, justify='left', background=bg_color_1).grid(column=0, row=21,
                                                                                                 rowspan=1)

oldpeak = tk.DoubleVar()
tk.Entry(p_info, textvariable=oldpeak, width=5, justify='left', highlightbackground=bg_color_1,
         background=bg_color_2).grid(column=1, row=21, sticky='W')

labelUnit10 = tk.Label(p_info, text="mV", anchor='w', width=3, justify='right', background=bg_color_1)
labelUnit10.grid(column=1, row=21)

ttk.Separator(p_info, orient='horizontal').grid(row=22, columnspan=3, sticky="ew")

# botton slope of the peak exercise ST segment
labelText11 = tk.StringVar()
labelText11.set("The slope of the peak \nexercise ST segment :")
ttk.Label(p_info, textvariable=labelText11, justify='left', background=bg_color_1).grid(column=0, row=23, rowspan=2)

slope = tk.StringVar()
slope.set('1.0')

tk.Radiobutton(p_info, text="Upsloping", variable=slope, value='1.0', justify='left',
               background=bg_color_1).grid(column=1, row=23, sticky='W')
tk.Radiobutton(p_info, text="Flat", variable=slope, value='2.0', justify='left', background=bg_color_1).grid(
    column=1, row=24, sticky='W')
tk.Radiobutton(p_info, text="Downsloping", variable=slope, value='3.0', justify='left',
               background=bg_color_1).grid(column=1, row=25, sticky='W')

ttk.Separator(p_info, orient='horizontal').grid(row=26, columnspan=3, sticky="ew")

# Botton number of major vessels (0-3) colored by flourosopy
labelText12 = tk.StringVar()
labelText12.set("Number of major vessels \n(0-3) colored by flourosopy :")
ttk.Label(p_info, textvariable=labelText12, justify='left').grid(column=0, row=27, rowspan =2)
nb_vessels = tk.StringVar()
nb_vessels.set("0.0")
tk.Radiobutton(p_info, text="0", variable=nb_vessels, value='0.0', justify='left', background=bg_color_1).grid(column=1,
                                                                                                              row=27,
                                                                                                              sticky='W')
tk.Radiobutton(p_info, text="1", variable=nb_vessels, value='1.0', justify='left', background=bg_color_1).grid(column=2,
                                                                                                              row=27,
                                                                                                              sticky='W')
tk.Radiobutton(p_info, text="2", variable=nb_vessels, value='2.0', justify='left', background=bg_color_1).grid(column=1,
                                                                                                              row=28,
                                                                                                              sticky='W')
tk.Radiobutton(p_info, text="3", variable=nb_vessels, value='3.0', justify='left', background=bg_color_1).grid(column=2,
                                                                                                              row=28,
                                                                                                              sticky='W')

ttk.Separator(p_info, orient='horizontal').grid(row=29, columnspan=3, sticky="ew")

# Botton Thallium heart examination
labelText13 = tk.StringVar()
labelText13.set("Thallium heart examination :")
ttk.Label(p_info, textvariable=labelText13, justify='left').grid(column=0, row=30)
tha_heartscan = tk.StringVar()
tha_heartscan.set('3.0')
tk.Radiobutton(p_info, text="Normal", variable=tha_heartscan, value='3.0', justify='left', background=bg_color_1).grid(
    column=1, row=30, sticky='W')
tk.Radiobutton(p_info, text="reversable defect", variable=tha_heartscan, value='7.0', justify='left',
               background=bg_color_1).grid(column=1, row=31, sticky='W')
tk.Radiobutton(p_info, text="fixed defect", variable=tha_heartscan, value='6.0', justify='left',
               background=bg_color_1).grid(column=1, row=32, sticky='W')

ttk.Separator(p_info, orient='vertical').grid(column=3, rowspan=33, sticky="ns")

labelName = tk.StringVar()
labelName.set("FULL NAME :")
ttk.Label(p_info, textvariable=labelName, justify='left').grid(column=6, row=0)
Name =tk.StringVar()
tk.Entry(p_info, textvariable=Name, width=6, justify='left', highlightbackground=bg_color_1, background=bg_color_2).grid(
    column=7, row=0, sticky=(tk.W + tk.E))
ttk.Separator(p_info, orient='horizontal').grid(row=1, columnspan=3, sticky="ew")
labelText14 = tk.StringVar()
labelText14.set("Select a model :")
ttk.Label(p_info, textvariable=labelText14, justify='left').grid(column=6, row=3)
sel_mod = tk.StringVar()
ttk.Combobox(p_info,width=20,textvariable=sel_mod,values=["Logistic Regression","Decision Tree","K Nearest neighbor (KNN)"],justify='left').grid(
    column = 7,row = 3)
sel_mod.set("Logistic Regression")
ttk.Separator(p_info, orient='horizontal').grid(columnspan = 3,row = 4)
###Casting functions
# getter for the variables that are inserted using the keyboard
def Nameprocessor(Name):
    name_p =str(Name.get())
    return name_p
def ageProcessor(age):
    age_p = str(age.get())
    return age_p


def blood_pressureProcessor(blood_pressure):
    blood_pressure_p = str(blood_pressure.get())
    return blood_pressure_p


def serum_cholProcessor(serum_chol):
    serum_chol_p = str(serum_chol.get())
    return serum_chol_p

def fbsProcessor(fbs):
    fbs_p = str(fbs.get())
    return fbs_p


def thalachProcessor(thalach):
    thalach_p = str(thalach.get())
    return thalach_p


def oldpeakProcessor(oldpeak):
    oldpeak_p = str(oldpeak.get())
    return oldpeak_p

def sel_modProcessor(sel_mod): # Process the data from words to integers
    sel_mod_p = {"Logistic Regression" : 0,  
                 "Decision Tree": 1,
                 "K Nearest neighbor (KNN)": 2}
    sel_mod_p = str(sel_mod_p.get(sel_mod.get()))
    return sel_mod_p
    
# set the data collected in one list
def dataPreprocessor(age, sex, chestPain, blood_pressure, serum_chol, fbs, rec_result, thalach, exang,
                     oldpeak, slope, nb_vessels, tha_heartscan):
    # Casts all data and shapes it for the prediction model
    processed_vars = []
    processed_vars.append(ageProcessor(age))
    processed_vars.append(sex.get())
    processed_vars.append(chestPain.get())
    processed_vars.append(blood_pressureProcessor(blood_pressure))
    processed_vars.append(serum_cholProcessor(serum_chol))
    processed_vars.append(fbsProcessor(fbs))
    processed_vars.append(rec_result.get())
    processed_vars.append(thalachProcessor(thalach))
    processed_vars.append(exang.get())
    processed_vars.append(oldpeakProcessor(oldpeak))
    processed_vars.append(slope.get())
    processed_vars.append(nb_vessels.get())
    processed_vars.append(tha_heartscan.get())
    processed_vars.append(sel_modProcessor(sel_mod)) # the last element is to select the model

    data_string = ''
    c = 1
    for var in processed_vars:
        if c == 14:
            data_string += var

        else:
            data_string += var + ' '
            c += 1
            #on mets les données d'entrée sous forme d'array et on transtype
    inputData = data_string.split(' ')
    print(inputData)
    return data_string
def DocAIModel(data_string):
    # send the inserted data to the model for prediction
    output = main(data_string)
    return output
def predict():
    # Verify the no value is empty
    # set them in an array form
    data_string = dataPreprocessor(age, sex, chestPain, blood_pressure, serum_chol, fbs, rec_result, thalach,
                                   exang, oldpeak, slope, nb_vessels, tha_heartscan)
    output = DocAIModel(data_string)
    return output  #[float : Prediction (0-4), string:name of the model, float:the accuracy of the model]

#===========================================================================================================#
#============================= Dispaly results after Prediction ============================================#
#===========================================================================================================#

def display_result(out_res_txt,lvl,pred_txt,p):

    if p[0] == 0:
        out_res_txt.set("No Heart disease")
        out_res_txt = ttk.Label(p_info, width = 20,textvariable=out_res_txt, font=("Arial", 15), background=bg_color_1, foreground='green')
        out_res_txt.grid(column=7, row=13, sticky="EW", columnspan=4)
    elif p[0] >= 1:
        out_res_txt.set("Has Heart disease")
        out_res_txt = ttk.Label(p_info, width = 20,textvariable=out_res_txt, font=("Arial", 15), background=bg_color_1, foreground='red')
        out_res_txt.grid(column=7, row=13, sticky="EW", columnspan=3)
    else:
        out_res_txt.set("________________")
        out_res_txt = ttk.Label(p_info, width = 20,textvariable=out_res_txt, font=("Arial", 15), background=bg_color_1)
        out_res_txt.grid(column=7, row=13, sticky="EW", columnspan=4)
    if p[0] == 0:
        lvl.set("Level 0")
        lvl = ttk.Label(p_info, width = 3,textvariable=lvl, font=("Arial", 15), background=bg_color_1,justify='left')
        lvl.grid(column=7, row=15, sticky="EW", columnspan=2)
    elif p[0] == 1:
        lvl.set("Level 1")
        lvl = ttk.Label(p_info, width = 3,textvariable=lvl, font=("Arial", 15), background=bg_color_1,justify='left')
        lvl.grid(column=7, row=15, sticky="EW", columnspan=2)
    elif p[0] == 2:
        lvl.set("Level 2")
        lvl = ttk.Label(p_info, width = 3,textvariable=lvl, font=("Arial", 15), background=bg_color_1)
        lvl.grid(column=7, row=15, sticky="EW", columnspan=1)
    elif p[0] == 3:
        lvl.set("Level 3")
        lvl = ttk.Label(p_info, width = 10,textvariable=lvl, font=("Arial", 15), background=bg_color_1)
        lvl.grid(column=7, row=15, sticky="EW", columnspan=2)
    elif p[0] == 4:
        lvl.set("Level 4")
        lvl = ttk.Label(p_info, width = 10,textvariable=lvl, font=("Arial", 15), background=bg_color_1)
        lvl.grid(column=7, row=15, sticky="EW", columnspan=2)
    else:
        lvl.set("________________")
        lvl = ttk.Label(p_info, width = 10,textvariable=lvl, font=("Arial", 15), background=bg_color_1)
        lvl.grid(column=7, row=15, sticky="EW", columnspan=2)
    pred_txt.set(str(float(format(p[2], ".4f"))*100)+" %")
    pred_txt = ttk.Label(p_info, width = 5,textvariable=pred_txt, font=("Verdana", 15), background=bg_color_1)
    pred_txt.grid(column=7, row=19, sticky="EW", columnspan=2)
#===========================================================================================================#
#===========================================================================================================#
#===================================================================================================================#
#================================= OUT of the scope of this project =================================================================#
def Coming_soon():
    showinfo(title='Notice', 
             message="The implementation of this functionality is out of the scope of this project") 
#=======================================================================================================================#
#=========================================================================================================================#
#======================================= Save the result of the prediction ===============================================#
def save_record():
    p=predict()
    if p[0] == 0:
        Result = "No Heart disease"
    elif p[0] >= 1:
        Result="Has Heart disease"
    with open('Records.csv', 'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=["Name", "Result","Risk level" ,"Accuracy","Prediction model"])
        if os.stat('Records.csv').st_size == 0:        #if file is not empty than header write else not
            dict_writer.writeheader()
       
        dict_writer.writerow({
            'Name' : Nameprocessor(Name),
            'Result' : Result,
            'Risk level': "Level " + str(p[0]),
            'Accuracy' : p[2],
            'Prediction model' : p[1],

        })
    
labelText15 = tk.StringVar()
labelText15.set("Angiography Result Prediction :")
text15 = ttk.Label(p_info, width=25, textvariable=labelText15, background=bg_color_1, anchor='center')
text15.grid(column=6, row=6, sticky="EW", columnspan=4)
#Out_result = tk.StringVar()
s = ttk.Style().configure("cta.TButton", foreground='Black',background = 'Green' ,font=('Helvetica', '14', 'bold'))
action = ttk.Button(p_info, text="Predict", width=40, command=lambda:[predict(),display_result(Out_result,Out_lev,pr_text,predict())], style="cta.TButton")
action.grid(column=6, row=7, rowspan=1, columnspan=4, sticky="EW")

ttk.Separator(p_info, orient='horizontal').grid(columnspan = 3,row = 5)

#=======================================================================================================#
#===================================  Display After OUTPUT is generated ================================#
#=======================================================================================================#

labelText16 = tk.StringVar()
labelText16.set("Result : ")
text16 = ttk.Label(p_info, width = 20,textvariable=labelText16, font=("Segoe Script", 22), background=bg_color_1)
text16.grid(column=6, row=13, sticky="EW", columnspan=4)
Out_result = tk.StringVar()



labelText17 = tk.StringVar()
Out_lev = tk.StringVar()
labelText17.set("Risk level (0-4) : ")
text17 = ttk.Label(p_info, width = 10,textvariable=labelText17, font=("Segoe Script", 14), background=bg_color_1)
text17.grid(column=6, row=15, sticky="EW", columnspan=2)

ttk.Separator(p_info, orient='horizontal').grid(columnspan = 3,row = 16)
labelText18 = tk.StringVar()
pr_text = tk.StringVar()
labelText18.set("Prediction Accuracy : ")
text18 = ttk.Label(p_info, width = 10,textvariable=labelText18, font=("Verdana", 13), background=bg_color_1)
text18.grid(column=6, row=19, sticky="EW", columnspan=2)

#=======================================================================================================#
#=============================== Save result and receive input buttons==================================#
#=======================================================================================================#

action2 = ttk.Button(p_info, image=photo_save ,text="Save Result" ,command =lambda : save_record() ,width=20,compound = "left")
action2.grid(column=6, row=23, rowspan=1, columnspan=1, sticky="EW")

action3 = ttk.Button(p_info, image=photo_sensor ,text="Receive Sensors' data",command=Coming_soon, width=20,compound = "left")
action3.grid(column=7, row=23, rowspan=1, columnspan=1, sticky="EW")
#========================================================================================================================#
#------------------------------------------------------------------------------------------------------------------------#
#----------------------------Doctor's record ----------------------------------------------------------------------------#
d_info = ttk.LabelFrame(frame2, text = "Medical Records")
#d_info.grid(sticky=(tk.W + tk.E))
d_info.place(height=650,width=850)
#TreeView widget (Table)
tv = ttk.Treeview(d_info)
tv.place(width=800,height=600)
treescrolly = tk.Scrollbar(d_info,orient= 'vertical',command=tv.yview)
treescrollx = tk.Scrollbar(d_info,orient= 'horizontal',command=tv.xview)
tv.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
treescrollx.pack(side='bottom',fill = 'x')
treescrolly.pack(side='right',fill = 'y')
# define number of columns and draw heading elemnts on the table
tv["columns"] = ("Name", "Result","Risk level" ,"Accuracy","Prediction model")
tv["show"]="headings"
for c in tv["columns"]:
    tv.heading(c, text=c)
    tv.column(c, width=100)
#===============================================================================#
#========================== Check if the Record file already exist ==============
# if os.path.isfile('/'.join((os.path.dirname(os.path.realpath("__file__")),"Records.csv"))):
#     Rec =pd.read_csv("Records.csv",names=tv["columns"])
#     tv.insert('', "end",iid=1,values=np.array(Rec))
root.mainloop()