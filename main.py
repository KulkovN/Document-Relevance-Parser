#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import selenium_modul as pars_sl
import parser_bs as pars_bs


# Тестовые данные:
# ГОСТ 34028-2016,ГОСТ 5781-82,ГОСТ 8509-93,ГОСТ-7657849,О внесении изменений в статью 4 Федерального закона "Об упразднении Лотошинского и Шаховского районных судов Московской области и образовании постоянных судебных присутствий в составе Волоколамского городского суда Московской области" и статью 3 Федерального закона "Об упразднении Климовского городского суда Московской области"


def run_search():
    """ checking the status of the checkbox and run search """
    text = text_area.get('1.0', 'end - 1 chars').split(save_separator())
    if check_rel() == 0:
        for i in text:
            pars_sl.pool_in_line_brows(i)
    else:
        out_window = tk.Toplevel()
        out_window.title('Статус релевантности')
        out_window.geometry('430x310')
        out_window.resizable(False, False)
        # виджет текста для нового окна
        text_wi_toplvl = tk.Frame(out_window)
        text_wi_toplvl.pack(side=tk.LEFT)
        text_area_toplvl = tk.Text(text_wi_toplvl)
        text_area_toplvl.pack(expand=True, fill=tk.BOTH)
        count = len(text)
        for i in reversed(text):
            text_area_toplvl.insert(
                '1.0', f'{count}) {i[:50]}\n{pars_bs.parser(i)}\n{"_"*53}\n\n')
            count -= 1


def check_rel():
    """ featch checkbox """
    value_checkBox = CheckVar_1.get()
    return value_checkBox


def save_separator():
    """ saving separator """
    separator_for_browser = input_pool_sep.get()
    if separator_for_browser:
        tk.Label(
            sep_frame, text=f'" {separator_for_browser} " записан',
            foreground='#008000', font='bold').grid(
            row=2, column=0, columnspan=2)
    return separator_for_browser


if __name__ == '__main__':
    """ Main window """
    main_win = tk.Tk()
    main_win.title('Выбор параметров')
    main_win.geometry('570x230')
    main_win.resizable(False, False)
    main_font_for_widgets = ('Roboto', 10)

    """ Separator Widgets """
    sep_frame = tk.LabelFrame(text='Внесите разд-ль')
    sep_frame.grid(row=0, column=0, padx=10)
    # комбобокс выбора разделителя
    input_pool_sep = ttk.Combobox(
        sep_frame, justify='center', width=3, font=main_font_for_widgets, values=[
            '.', ',', ':', ';'])
    input_pool_sep.grid(row=0, column=0)
    # кнопка отправления разделителя
    separ_get_btn = tk.Button(
        sep_frame, text='Сохранить', command=save_separator)
    separ_get_btn.grid(row=1, column=0, pady=10, padx=10)

    """ CheckBox Widgets"""
    chbox_frame = tk.LabelFrame(text="КОДЕКС")
    chbox_frame.grid(row=1, column=0)
    # чекБокс для поиска по СПС Кодеks
    CheckVar_1 = tk.IntVar()  # нужна "своя" переменная в tk
    CheckBtn = tk.Checkbutton(
        chbox_frame, text='поиск',
        variable=CheckVar_1,
        offvalue=0, onvalue=1)
    CheckBtn.grid(row=0, column=0)

    """ Text Widgets """
    text_frame = tk.LabelFrame(text='Внесите текст')
    text_frame.grid(row=0, column=1, rowspan=2)
    # виджет текста
    text_area = tk.Text(text_frame, width=50, height=10,
                        font=main_font_for_widgets)
    text_area.grid(column=0, row=0)
    # кнопка отправления текста
    text_get_btn = tk.Button(
        text_frame, text='Найти', command=run_search)
    text_get_btn.grid(row=1, column=0)

    main_win.mainloop()
