from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x400')
GUI.title('โปรแกรมคำนวณสินค้า + Vat ')

#FONT All
FONT1 = ('Angsana New',20)


############# ช่องกรอก ชื่อสินค้า ###################
L = ttk.Label(GUI,text='ชื่อสินค้า',font=FONT1).pack()

v_nameitem = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_nameitem,)
E1.pack(pady=10)



############# ช่องกรอกข้อมูล ราคาสินค้า #################
L = ttk.Label(GUI,text='ราคาสินค้า',font=FONT1).pack() #ข้อความแสดง

v_price = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_price)
E2.pack(pady=10)

############ ช่องกรอก จำนวนสินค้า ######################
L = ttk.Label(GUI,text='จำนวนสินค้า',font=FONT1).pack()

v_quantity = StringVar()
E3 = ttk.Entry(GUI,textvariable=v_quantity)
E3.pack(pady=10)



############ ปุ่มกด คำนวณ Calculate #########
def Calc(event=None):
	# int() คำสั่งแปลงความเป็นตัวเลข '2' ---> 2
	#print( type( int( v_price.get() ) ) )
	nameitem = v_nameitem.get()
	price = int(v_price.get())
	quantity = int(v_quantity.get())
	total = price * quantity
	
	Vat7 = total * (7/107)
	nettotal = total * (100/107)

	print('ราคาก่อน vat: {:.2f} (vat 7%: {:.2f})'.format(nettotal,Vat7))

	v_result.set('สินค้า: {} {} ชิ้นทั้งหมด {} บาท ({} บาท/ชิ้น)\nราคาสินค้า: {:.2f}.-VAT7%: {:.2f}.-'.format(nameitem,
																							quantity,
																							total,
																							price,
																							nettotal,
																							Vat7))

B1 = ttk.Button(GUI,text='Calculate',command=Calc)
B1.pack(pady=10)


E3.bind('<Return>',Calc)

################ แสดงผล ##############
v_result = StringVar()
v_result.set('<<<<<ผลลัพธ์โชว์จุดนี้>>>>>>') ### โชว์ข้อมูลเริ่มต้น

R1 = ttk.Label(GUI,textvariable=v_result, font=FONT1)
R1.pack()


GUI.mainloop()