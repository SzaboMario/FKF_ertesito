import File_handle as fh
import time
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from plyer import notification



conf_file = "Config.txt"
URL = "https://www.fkf.hu/hulladeknaptar"
Chrome_options = Options()
Chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=Chrome_options)


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None, 
        timeout=15,  
    )

def Set_list_data(element, data):
    Select(driver.find_element(By.ID, element)).select_by_value(data)
    time.sleep(4)

def ClickButton(text):
    driver.find_element(By.XPATH, f"//button[text()='{text}']").click()
    time.sleep(4)

def Collect_data_from_result_table(class_name):
    tables = driver.find_elements(By.TAG_NAME, class_name)
    scrap_type = {"Szelektív"}
    ret_list = list()
    for t in tables:
        if len(tables)>1:
            tr_list = t.find_elements(By.TAG_NAME, "tbody")
            for row in tr_list:
                td_list = row.find_elements(By.TAG_NAME, "tr")
                for td in td_list:
                    td = td.text.split(" ")
                    if len(td)>2 and td[2] in scrap_type:
                        ret_list.append(td)
    return ret_list

def Get_districts():
    ret = list()
    data = driver.find_elements(By.ID, "districts")
    data = data[0].text.split("\n")
    for distr in data:
        distr = distr.split(" ")
        if len(distr) > 2:
            ret.append(distr[2])
    return ret

def Get_public_places():
    ret = list()
    select_element = Select(driver.find_element(By.ID, "publicPlaces"))
    all_options = select_element.options
    for option in all_options:
        tmp = option.get_attribute('value')
        if tmp != "false":
            ret.append(tmp)
    return ret

def Get_house_numbers():
    ret = list()
    select_element = Select(driver.find_element(By.ID, "houseNumber"))
    all_options = select_element.options
    for option in all_options:
        tmp = option.get_attribute('value')
        if tmp != "false":
            ret.append(tmp)
    return ret

def Read_user_choice(param, list, msg):
    while not param in list:
        param = input(msg)
        found = param in list
        if not found:
            print("Hibás adat!")
        else:
            return param
            
#main
driver.get(URL)
time.sleep(4)
fh.Generate_conf_file(conf_file)
fh.Load_conf_file(conf_file)

if fh.SEL_DISTRICT == "0":
    districts = Get_districts()
    print(f"Elérhető irányítószámok:\n{districts}")
    fh.SEL_DISTRICT = Read_user_choice(fh.SEL_DISTRICT, districts, "Kérem adja meg az irányítószámot: ")
Set_list_data("districts", fh.SEL_DISTRICT)

if fh.SEL_PUBLIC_PLACE == "None":
    public_places = Get_public_places()
    print(f"Elérhető utcák:\n{public_places}")
    fh.SEL_PUBLIC_PLACE = Read_user_choice(fh.SEL_PUBLIC_PLACE, public_places, "Kérem adja meg az utcanevet: ")
Set_list_data("publicPlaces", fh.SEL_PUBLIC_PLACE)

if fh.SEL_HOUSE_NUM == "0":
    house_numbers = Get_house_numbers()
    print(f"Elérhető házszámok:\n{house_numbers}")
    fh.SEL_HOUSE_NUM = Read_user_choice(fh.SEL_HOUSE_NUM, house_numbers, "Kérem adja meg a házszámot: ")
Set_list_data("houseNumber", fh.SEL_HOUSE_NUM)


ClickButton("Keresés")
ret_data = Collect_data_from_result_table("table")
if len(ret_data) == 0:
    ret_data  = "Nincs adat!"
else:
    s = "Szelektív szemétszállítás időpontjai:\n"
    for sor in ret_data:
        s+=f"{sor[1]} - {sor[0]}\n" 
    ret_data = s
    fh.Write_config_file(conf_file, [fh.SEL_QUERY_PERIOD, fh.SEL_DISTRICT, fh.SEL_PUBLIC_PLACE, fh.SEL_HOUSE_NUM])
driver.close()
#messagebox.showinfo("Értesítő", ret_data)
send_notification("Értesítő", ret_data)