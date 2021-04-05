#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def come_over_here(user_text):
    options_for_run = webdriver.ChromeOptions()
    options_for_run.add_argument('headless')
    # ATTENTION TO THE PATH
    brows_driver = webdriver.Chrome(
    '/home/nikita/project/Multiple_internet_requests_pp/chromedriver', options=options_for_run)
    # ATTENTION TO THE ADDRESS
    # brows_driver.get(
    # f'http://docs.cntd.ru/search/intellectual?q={user_text}&itemtype=')
    brows_driver.get(f'https://docs.cntd.ru/search?q={user_text}')
    html_element_2 = brows_driver.find_element_by_class_name('document-list_i')
    result = html_element_2.get_attribute('title')
    print(result)
    return result


def pool_in_line_brows(user_text):
    # options_for_run = webdriver.ChromeOptions()
    brows_driver = webdriver.Chrome('/home/nikita/project/Multiple_internet_requests_pp_p2/chromedriver')
    brows_driver.get(f'https://yandex.ru/search/?text={user_text}')
        


"""def run_search():
    # checking the status of the checkbox and run search
    text = text_area.get('1.0', 'end - 1 chars').split(save_separator())
    out_window = tk.Toplevel()
    out_text = tk.Text(out_window, width=50, height=10)
    if check_rel() == 1:
        out_window.title('Результаты поиска')
        count = len(text)
        for i in reversed(text):
            out_text.insert(
                '1.0', f'{count}) {i} -> {pars.come_over_here(i)}\n\n')
            out_text.pack(expand=True, fill=tk.BOTH)
            count -= 1
    else:
        out_window.title('Warning')
        tk.Label(
            out_window, text='Перед закрытием окна\nубедитесь, что все данные изучены', font='bold').pack()
        for i in text:
            pars.fetch_in_line_brows(i) """

