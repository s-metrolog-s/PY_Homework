import tkinter as tk
from pathlib import Path
import dbase

def click_save():
    result_str = [ent_fname_input.get(),
                ent_lname_input.get(),
                ent_phone_1_input.get(),
                ent_phone_2_input.get()]
    if result_str != ['', '', '', '']:
        dbase.add_row(file_path, file_format.get(), data = result_str)
        click_clear()

def click_find():
    result = dbase.find_string(file_path, file_format.get(), ent_find.get())
    if result != None:
        result_of_find = result.split(';')
        ent_fname_input.delete('0', tk.END)
        ent_fname_input.insert('0', result_of_find[0])
        ent_lname_input.delete('0', tk.END)
        ent_lname_input.insert('0', result_of_find[1])
        ent_phone_1_input.delete('0', tk.END)
        ent_phone_1_input.insert('0', result_of_find[2])
        ent_phone_2_input.delete('0', tk.END)
        ent_phone_2_input.insert('0', result_of_find[3])
        lbl_fresult.configure(text = 'Запись найдена')
    else:
        lbl_fresult.configure(text = 'Запись не найдена')

def click_clear():
    ent_fname_input.delete('0', tk.END)
    ent_lname_input.delete('0', tk.END)
    ent_phone_1_input.delete('0', tk.END)
    ent_phone_2_input.delete('0', tk.END)
    ent_find.delete("0", tk.END)
    lbl_fresult.configure(text = 'Результат поиска')
    ent_lname_input.focus()

def click_del():
    result_str = [ent_fname_input.get(),
                ent_lname_input.get(),
                ent_phone_1_input.get(),
                ent_phone_2_input.get()]
    if result_str != ['', '', '', '']:
        dbase.del_row(file_path, file_format.get(), data = result_str)
        click_clear()


window = tk.Tk()
window.title('Телефонный справочник 0.1')
file_path = Path.cwd()

frm_form = tk.Frame(relief = tk.SUNKEN, borderwidth = 2)
frm_form.pack()

# Внесение Фамилии
lbl_last_name = tk.Label(master = frm_form, text = 'Фамилия', font = ('Calibri', 16))
ent_lname_input = tk.Entry(master = frm_form, width = 50)
lbl_last_name.grid(row = 0, column = 0, sticky = 'e')
ent_lname_input.grid(row = 0, column = 1)

# Внесение Имени
lbl_first_name = tk.Label(master = frm_form, text = 'Имя', font = ('Calibri', 16))
ent_fname_input = tk.Entry(master = frm_form, width = 50)
lbl_first_name.grid(row = 1, column = 0, sticky = 'e')
ent_fname_input.grid(row = 1, column = 1)

# Внесение Телефона 1
lbl_phone_1 = tk.Label(master = frm_form, text = 'Телефон 1', font = ('Calibri', 16))
ent_phone_1_input = tk.Entry(master = frm_form, width = 50)
lbl_phone_1.grid(row = 2, column = 0, sticky = 'e')
ent_phone_1_input.grid(row = 2, column = 1)

# Внесение Телефона 2
lbl_phone_2 = tk.Label(master = frm_form, text = 'Телефон 2', font = ('Calibri', 16))
ent_phone_2_input = tk.Entry(master = frm_form, width = 50)
lbl_phone_2.grid(row = 3, column = 0, sticky = 'e')
ent_phone_2_input.grid(row = 3, column = 1)

# Рамка для кнопок
frm_buttons = tk.Frame()
frm_buttons.pack(fill = tk.X, ipadx = 5, ipady = 5)

btn_find = tk.Button(master = frm_buttons, text = 'Поиск', command = click_find)
btn_find.pack(side = tk.RIGHT, padx = 10, ipadx = 10)

btn_clear = tk.Button(master = frm_buttons, text = 'Очистить', command = click_clear)
btn_clear.pack(side = tk.RIGHT, padx = 10, ipadx = 10)

btn_save = tk.Button(master = frm_buttons, text = 'Сохранить данные', command = click_save)
btn_save.pack(side = tk.LEFT, padx = 10, ipadx = 10)

btn_save = tk.Button(master = frm_buttons, text = 'Удалить данные', command = click_del)
btn_save.pack(side = tk.LEFT, padx = 10, ipadx = 10)

# Рамка модуля поиска
frm_find = tk.Frame(relief = tk.GROOVE, borderwidth = 1)
frm_find.pack(fill = tk.X, ipadx = 5, ipady = 5)

lbl_text_in = tk.Label(master = frm_find, text = 'Введите Фамилию для поиска:', font = ('Calibri', 12))
lbl_text_in.grid(row = 0, column = 0, sticky = 'e')

ent_find = tk.Entry(master = frm_find, width = 30)
ent_find.grid(row = 0, column = 1)

lbl_fresult = tk.Label(master = frm_find, text = 'Результат поиска')
lbl_fresult.grid(row = 1, column = 0)

# Рамка сохранения
frm_data = tk.Frame()
frm_data.pack(fill = tk.X)

file_format = tk.IntVar()
file_format.set(1)
lbl_data_adress = tk.Label(master = frm_data, text = 'Путь к файлу: ', font = ('Colibri', 12))
ent_data = tk.Entry(master = frm_data, width = 40)
lbl_data_text = tk.Label(master = frm_data, text = 'Выберите формат файла:', font = ('Colibri', 12))
rad1 = tk.Radiobutton(master = frm_data, text = 'csv', font = ('Colibri', 12), value = 1, variable = file_format)
rad2 = tk.Radiobutton(master = frm_data, text = 'txt', font = ('Colibri', 12), value = 2, variable = file_format)

lbl_data_adress.grid(row = 0, column = 0, sticky = 'w')
ent_data.grid(row = 0, column = 1)
lbl_data_text.grid(row = 1, column = 0, sticky = 'e')
rad1.grid(row = 2, column = 0, sticky = 'w')
rad2.grid(row = 3, column = 0, sticky = 'w')

ent_data.insert('0', file_path)

window.mainloop()
