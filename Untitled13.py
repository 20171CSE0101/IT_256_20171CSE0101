#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Address enrty form frame
import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

frame1 = tk.Frame(master=window)
frame1["relief"] = tk.SUNKEN
frame1["borderwidth"] = 3
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.X)

list = {
    0: "First Name",
    1: "Last Name",
    2: "Address Line 1",
    3: "Address Line 2",
    4: "City",
    5: "State/Province",
    6: "Postal Code",
    7: "Country",
}

for i in list:
    label = tk.Label(master=frame1)
    label["text"] = list[i], ":"
    label.grid(row=i, column=0, sticky=tk.E)

    entry = tk.Entry(master=frame1)
    entry["width"] = 50
    entry.grid(row=i, column=1)

button1 = tk.Button(master=frame2)
button1["text"] = "Submit"
button1["width"] = 7
button1["height"] = 1
button1.pack(padx=5, pady=5, side=tk.RIGHT)

button2 = tk.Button(master=frame2)
button2["text"] = "Clear"
button2["width"] = 5
button2["height"] = 1
button2.pack(padx=5, pady=5, side=tk.RIGHT)

window.mainloop()


# In[1]:


#temperature converter frame
import tkinter as tk
from functools import partial

# global variable
tempVal = "Celsius"


# getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp


# the main conversion
def call_convert(rlabel1, rlabe12, inputn):
    tem = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        rlabel1.config(text="%f Fahrenheit" % f)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Fahrenheit" % f)
    return


# app window configuration and UI
root = tk.Tk()
root.geometry('400x150+100+200')
root.title('Temperature Converter')
root.configure(background='#09A3BA')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

numberInput = tk.StringVar()
var = tk.StringVar()

# label and entry field
input_label = tk.Label(root, text="Enter temperature", background='#09A3BA', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

# result label's for showing the other two temperatures
result_label1 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)

# drop down initalization and setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)
dropdown.config(background='#09A3BA', foreground="#FFFFFF")
dropdown["menu"].config(background='#09A3BA', foreground="#FFFFFF")

# button click
call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)

root.mainloop()


# In[2]:


#convert tuple to string
tup=('a','b','c')
str=''.join(tup)
print(str)


# In[3]:


#check whether an element exists within a tuple
t=(1,2,3,4,5)
n=2
if n in t:
    print("present in tuple")
else:
    print("not present in tuple")
    


# In[5]:


#find index of an item of a list
name=['a','b','c']
index=name.index('a')
print("the index of a is",index)


# In[6]:


#convert a list of tuples into dictionary
z=((1,'a'),(2,'b'))
dict(z)
print(dict(z))


# In[ ]:




