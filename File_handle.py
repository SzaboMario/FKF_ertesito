import os


SEL_QUERY_PERIOD = "0"
SEL_DISTRICT = "0"
SEL_PUBLIC_PLACE = ""
SEL_HOUSE_NUM = "0"

def Generate_conf_file(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines("QueryPeriod(minute) = 0\n")
            file.writelines("District = 0\n")
            file.writelines("PublicPlace = None\n")
            file.writelines("HouseNumber = 0")

def Load_conf_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as file: 
            for line in file:
                line = line.strip().split(" = ")
                if line[0].find("QueryPeriod") != -1:
                    global SEL_QUERY_PERIOD
                    SEL_QUERY_PERIOD = line[1]
                elif line[0].find("District") != -1:
                    global SEL_DISTRICT
                    SEL_DISTRICT = line[1]
                elif line[0].find("PublicPlace") != -1:
                    global SEL_PUBLIC_PLACE
                    SEL_PUBLIC_PLACE = line[1]
                else:
                    global SEL_HOUSE_NUM
                    SEL_HOUSE_NUM = line[1]
    else:
        print("Nem található konfigurációs fájl!")
        Generate_conf_file(file_name)

def Write_config_file(file_name, data_list):
    with open(file_name, "w+", encoding="utf-8") as file:
        file.write(f"QueryPeriod(minute) = {data_list[0]}\n")
        file.write(f"District = {data_list[1]}\n")
        file.write(f"PublicPlace = {data_list[2]}\n")
        file.write(f"HouseNumber = {data_list[3]}")
