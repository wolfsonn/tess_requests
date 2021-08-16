from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style

# create main window
root = Tk()

# root
root.title('Requests management')
root.geometry('350x350+100+400')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

style = Style(theme='superhero')
style.configure('.', font=12)
style.configure('TButton', font=12)
style.configure('TFrame', font=12)
style.configure('TLabel', font=12)

# main frame
main_frame = Frame(root, background='black')
main_frame.grid(column=0, row=0, sticky='ewns')
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.rowconfigure(0, weight=0)
main_frame.rowconfigure(1, weight=0)
main_frame.rowconfigure(2, weight=0)
main_frame.rowconfigure(3, weight=0)

# add request
add_request = ttk.Labelframe(main_frame, text='add requests')
add_request.grid(column=0, row=0, columnspan=3, sticky='ewns')
add_request.columnconfigure(0, weight=1)
add_request.columnconfigure(1, weight=1)
add_request.rowconfigure(0, weight=1)

choose_folder = ttk.Button(add_request, text='browse')
choose_folder.grid(row=0, column=0, columnspan=1, sticky='ewn')

submit = ttk.Button(add_request, text='submit')
submit.grid(row=0, column=1, columnspan=1, sticky='ewn')

# export request
export_request = ttk.Labelframe(main_frame, text='export request')
export_request.grid(row=1, column=0, columnspan=3, sticky='ewns')
export_request.columnconfigure(0, weight=1)
export_request.columnconfigure(1, weight=1)
export_request.columnconfigure(2, weight=1)
export_request.rowconfigure(0, weight=1)

export_action = ttk.Button(export_request, text='action')
export_action.grid(row=0, column=0, columnspan=1, sticky='ewn')

export_status = ttk.Button(export_request, text='status')
export_status.grid(row=0, column=1, columnspan=1, sticky='ewn')

export_export = ttk.Button(export_request, text='export')
export_export.grid(row=0, column=2, columnspan=1, sticky='ewn')

# taxes
taxes = ttk.Labelframe(main_frame, text='taxes')
taxes.grid(row=2, column=0, columnspan=3, sticky='ewns')
taxes.columnconfigure(0, weight=1)
taxes.columnconfigure(1, weight=1)
taxes.columnconfigure(2, weight=1)
taxes.rowconfigure(0, weight=1)

taxes_action = ttk.Button(taxes, text='action')
taxes_action.grid(row=0, column=0, columnspan=1, sticky='ewn')

taxes_status = ttk.Button(taxes, text='status')
taxes_status.grid(row=0, column=1, columnspan=1, sticky='ewn')

taxes_export = ttk.Button(taxes, text='export')
taxes_export.grid(row=0, column=2, columnspan=1, sticky='ewn')

# manage status
manage_status = ttk.Labelframe(main_frame, text='manage status')
manage_status.grid(row=3, column=0, columnspan=3, sticky='ewns')
manage_status.columnconfigure(0, weight=1)
manage_status.columnconfigure(1, weight=1)
manage_status.columnconfigure(2, weight=1)
manage_status.rowconfigure(0, weight=1)
manage_status.rowconfigure(1, weight=1)

manage_action = ttk.Button(manage_status, text='action')
manage_action.grid(row=0, column=0, columnspan=1, sticky='ewn')

manage_curr_status = ttk.Button(manage_status, text='status')
manage_curr_status.grid(row=0, column=1, columnspan=1, sticky='ewn')

manage_new_status = ttk.Button(manage_status, text='export')
manage_new_status.grid(row=0, column=2, columnspan=1, sticky='ewn')

manage_submit = ttk.Button(manage_status, text='submit')
manage_submit.grid(row=1, column=0, columnspan=3, sticky='ewn')

root.mainloop()
