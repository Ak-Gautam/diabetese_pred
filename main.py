import pandas as pd
import numpy as np
import pickle
from tkinter import *

#Loading the model
MODEL_PATH = "models/knn_23.sav"
loaded_model = pickle.load(open(MODEL_PATH, 'rb'))



def isDiab(res):
    if res == 1:
        return "High"
    else:
        return "Low"

def calculate_risk():
    res = loaded_model.predict([[int(preg.get()), int(glu.get()), int(pres.get()), int(skin.get()), int(ins.get()), int(bmi.get()), int(pedi.get()), int(age.get())]])
    diab_label.config(text="Risk of Diabetes: {pr}".format(pr=isDiab(res)))

#Initializing the tkinter window
master = Tk()
master.geometry("900x800")
master.configure(background='#0090F2')
master.title('Diabetes Risk Calculator')

#Label to show res
diab_label = Label(master, bg='#0090F2', fg="white", font=("Times", 30, "bold"), text="Hello There!")
diab_label.grid(row=1, column=0, columnspan=3, pady=10)

#columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
#Creating the input fields
preg_label = Label(master, text="Pregnancies: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
preg_label.grid(row=2, column=0, padx=5, pady=20)
preg = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
preg.grid(row=2, column=1, padx=5, pady=20)
pregs = Label(master, text="Range (0-n)", bg='#0090F2', fg="white", font=("Times", 20))
pregs.grid(row=2, column=2, padx=5, pady=20)

glu_label = Label(master, text="Glucose: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
glu_label.grid(row=3, column=0, padx=5, pady=20)
glu = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
glu.grid(row=3, column=1, padx=5, pady=20)
glus = Label(master, text="Range (40-250)", bg='#0090F2', fg="white", font=("Times", 20))
glus.grid(row=3, column=2, padx=5, pady=20)

pres_label = Label(master, text="BloodPressure: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
pres_label.grid(row=4, column=0, padx=5, pady=20)
pres = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
pres.grid(row=4, column=1, padx=5, pady=20)
pres_s = Label(master, text="Range (50-200)", bg='#0090F2', fg="white", font=("Times", 20))
pres_s.grid(row=4, column=2, padx=5, pady=20)

skin_label = Label(master, text="SkinThickness: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
skin_label.grid(row=5, column=0, padx=5, pady=20)
skin = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
skin.grid(row=5, column=1, padx=5, pady=20)
skin_s = Label(master, text="Range (10-100)", bg='#0090F2', fg="white", font=("Times", 20))
skin_s.grid(row=5, column=2, padx=5, pady=20)

ins_label = Label(master, text="Insulin: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
ins_label.grid(row=6, column=0, padx=5, pady=20)
ins = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
ins.grid(row=6, column=1, padx=5, pady=20)
ins_s = Label(master, text="Range (5-1500)", bg='#0090F2', fg="white", font=("Times", 20))
ins_s.grid(row=6, column=2, padx=5, pady=20)


bmi_label = Label(master, text="BMI: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
bmi_label.grid(row=7, column=0, padx=5, pady=20)
bmi = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
bmi.grid(row=7, column=1, padx=5, pady=20)
bmi_s = Label(master, text="Range (10-80)", bg='#0090F2', fg="white", font=("Times", 20))
bmi_s.grid(row=7, column=2, padx=5, pady=20)


pedi_label = Label(master, text="DiabetesPedigreeFunction: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
pedi_label.grid(row=8, column=0, padx=5, pady=20)
pedi = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
pedi.grid(row=8, column=1, padx=5, pady=20)
pedi_s = Label(master, text="Range (1-4)", bg='#0090F2', fg="white", font=("Times", 20))
pedi_s.grid(row=8, column=2, padx=5, pady=20)

age_label = Label(master, text="Age: ", bg='#0477C5', fg="white", font=("Times", 20, "bold"))
age_label.grid(row=9, column=0, padx=5, pady=20)
age = Entry(master, bg='#0090F2', fg="white", font=("Times", 20, "bold"))
age.grid(row=9, column=1, padx=5, pady=20)
age_s = Label(master, text="Range (10-100)", bg='#0090F2', fg="white", font=("Times", 20))
age_s.grid(row=9, column=2, padx=5, pady=20)


#Submit button
submit_button = Button(master, text="Submit", bg='#0477C5', fg="white", font=("Times", 20, "bold"), command=calculate_risk).grid(row=10, column=0, columnspan=3, padx=5, pady=30)

mainloop()