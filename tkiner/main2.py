from tkinter import *
def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("miles to km converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equals to ")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

cal_button = Button(text="calculate", command=mile_to_km)
cal_button.grid(column=1, row=2)














window.mainloop()
