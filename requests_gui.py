from tkinter import *
from tkinter import ttk, filedialog
from ttkbootstrap import Style

import requests_db
import tess_requests

# create main window
root = Tk()

actions = ['action', 'none']
[actions.append(i) for i in tess_requests.Request.ACTIONS.keys()]
export_action_drop = StringVar()
taxes_action_drop = StringVar()
manage_action_drop = StringVar()

statuses = ['status', 'none', 'pending', 'done']
statuses_curr = ['current status', 'none', 'pending', 'done']
statuses_new = ['new status', 'none', 'pending', 'done']
export_status_drop = StringVar()
taxes_status_drop = StringVar()
manage_status_curr_drop = StringVar()
manage_status_new_drop = StringVar()

browse_folder = StringVar()


def browse():
    folder = filedialog.askdirectory()
    browse_folder.set(folder)


# root
root.title('Requests management')
# root.geometry('510x300+100+400')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(0, 0)

style = Style(theme='superhero')
style.configure('.', font=12)
style.configure('TButton', font=12)
style.configure('TFrame', font=12)
style.configure('TLabel', font=12)

# main frame
main_frame = Frame(root, background='black')
main_frame.grid(column=0, row=0, sticky='ewn')
main_frame.columnconfigure(0, weight=1, minsize=170)
main_frame.columnconfigure(1, weight=1, minsize=170)
main_frame.columnconfigure(2, weight=1, minsize=170)
main_frame.rowconfigure(0, weight=0)
main_frame.rowconfigure(1, weight=0)
main_frame.rowconfigure(2, weight=0)
main_frame.rowconfigure(3, weight=0)

# add request
add_req = ttk.Labelframe(main_frame, text='add requests')
add_req.grid(column=0, row=0, columnspan=3, sticky='ew')
add_req.columnconfigure(0, weight=1)
add_req.columnconfigure(1, weight=1)
add_req.rowconfigure(0, weight=1)

browse = ttk.Button(add_req, text='browse', command=browse)
browse.grid(row=0, column=0, columnspan=1, sticky='ew', padx=(0, 1))

submit = ttk.Button(add_req, text='submit', command=lambda: requests_db.add_requests(browse_folder.get()))
submit.grid(row=0, column=1, columnspan=1, sticky='ew')

# export request
export_request = ttk.Labelframe(main_frame, text='export request')
export_request.grid(row=1, column=0, columnspan=3, sticky='ew')
export_request.columnconfigure(0, weight=1, minsize=170)
export_request.columnconfigure(1, weight=1, minsize=170)
export_request.columnconfigure(2, weight=1, minsize=170)
export_request.rowconfigure(0, weight=1)

export_action = ttk.OptionMenu(export_request, export_action_drop, *actions)
export_action.grid(row=0, column=0, columnspan=1, sticky='ew', padx=(0, 1))

export_status = ttk.OptionMenu(export_request, export_status_drop, *statuses)
export_status.grid(row=0, column=1, columnspan=1, sticky='ew')

export_export = ttk.Button(export_request, text='export', command=lambda: requests_db.export_csv_act_status(export_action_drop.get(), export_status_drop.get()))
export_export.grid(row=0, column=2, columnspan=1, sticky='ew', padx=(1, 0))

# taxes
taxes = ttk.Labelframe(main_frame, text='taxes')
taxes.grid(row=2, column=0, columnspan=3, sticky='ew')
taxes.columnconfigure(0, weight=1, minsize=170)
taxes.columnconfigure(1, weight=1, minsize=170)
taxes.columnconfigure(2, weight=1, minsize=170)
taxes.rowconfigure(0, weight=1)

taxes_action = ttk.OptionMenu(taxes, taxes_action_drop, *actions)
taxes_action.grid(row=0, column=0, columnspan=1, sticky='ew', padx=(0, 1))

taxes_status = ttk.OptionMenu(taxes, taxes_status_drop, *statuses)
taxes_status.grid(row=0, column=1, columnspan=1, sticky='ew')

taxes_export = ttk.Button(taxes, text='export', command=lambda: requests_db.export_taxes(taxes_action_drop.get(), taxes_status_drop.get()))
taxes_export.grid(row=0, column=2, columnspan=1, sticky='ewn', padx=(1, 0))

# manage status
manage_status = ttk.Labelframe(main_frame, text='manage status')
manage_status.grid(row=3, column=0, columnspan=3, sticky='ew')
manage_status.columnconfigure(0, weight=1, minsize=170)
manage_status.columnconfigure(1, weight=1, minsize=170)
manage_status.columnconfigure(2, weight=1, minsize=170)
manage_status.rowconfigure(0, weight=1)
manage_status.rowconfigure(1, weight=1)

manage_action = ttk.OptionMenu(manage_status, manage_action_drop, *actions)
manage_action.grid(row=0, column=0, columnspan=1, sticky='ew', padx=(0, 1))

manage_curr_status = ttk.OptionMenu(manage_status, manage_status_curr_drop, *statuses_curr)
manage_curr_status.grid(row=0, column=1, columnspan=1, sticky='ew')

manage_new_status = ttk.OptionMenu(manage_status, manage_status_new_drop, *statuses_new)
manage_new_status.grid(row=0, column=2, columnspan=1, sticky='ew', padx=(1, 0))

manage_submit = ttk.Button(manage_status, text='submit', command=lambda: requests_db.set_status(manage_action_drop.get(), manage_status_curr_drop.get(), manage_status_new_drop.get()))
manage_submit.grid(row=1, column=0, columnspan=3, sticky='ew', pady=(1, 0))

root.mainloop()
