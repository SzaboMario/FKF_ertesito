import os
import requests as rq
from bs4 import BeautifulSoup as bs

conf_file = "Config.txt"
period = ""
post_code = ""
settlement = ""
house_number = ""

def Generate_conf_file(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, "w+", encoding="utf-8") as file:
            file.writelines("Period = None\n")
            file.writelines("Post code = None\n")
            file.writelines("Settlement = None\n")
            file.writelines("House number = None")

def Load_conf_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name,"r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().split(" = ")
                if line[0] == "Period":
                        period = line[1]
                elif line[0] == "Post code":
                        post_code = line[1]
                elif line[0] == "Settlement":
                        settlement = line[1]
                elif line[0] == "House number":
                        house_number = line[1]
                else:
                     print("A konfig fájl sérült vagy nem olvasható!")
#main
Generate_conf_file(conf_file)
Load_conf_file(conf_file)
