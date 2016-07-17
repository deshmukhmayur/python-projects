#! python
'''A simple Calculator'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculator')

label1 = ttk.Label(root, text='Enter first number:')
label1.grid(row='0', column='0')

num1 = DoubleVar()
ttk.Entry(root, textvariable=num1).grid(row='0', column='1')

label2 = ttk.Label(root, text='Enter second number:')
label2.grid(row='1', column='0')

num2 = DoubleVar()
ttk.Entry(root, textvariable=num2).grid(row='1', column='1')

operation = StringVar()
ttk.Radiobutton(root, text='Add', variable=operation, value='add').grid(row='2', column='0')
ttk.Radiobutton(root, text='Subtract', variable=operation, value='sub').grid(row='2', column='1')
ttk.Radiobutton(root, text='Multiply', variable=operation, value='mul').grid(row='3', column='0')
ttk.Radiobutton(root, text='Divide', variable=operation, value='div').grid(row='3', column='1')

ans = StringVar()
ttk.Label(root, textvariable=ans).grid(row='4', column='0', columnspan='2')

def calc():
	if operation.get() == 'add':
		ans.set(str(float(num1.get()) + float(num2.get())))
	elif operation.get() == 'sub':
		ans.set(str(float(num1.get()) - float(num2.get())))
	elif operation.get() == 'mul':
		ans.set(str(float(num1.get()) * float(num2.get())))
	elif operation.get() == 'div':
		ans.set(str(float(num1.get()) / float(num2.get())))
	else:
		ans.set('Please select and operation!')

ttk.Button(root, text='Calculate', command=calc).grid(row='5', column='0')
ttk.Button(root, text='Exit', command= lambda: root.destroy()).grid(row='5', column='1')
