import logging
import datetime

def customlog():
    path = r"C:\Users\ssudharv\PycharmProjects\Project Lists\REDBUS\logs"
    date = datetime.datetime.now().strftime("%d.%m.%y.%H%M%S")
    logging.basicConfig(handlers=[logging.StreamHandler(), logging.FileHandler(filename=path + "//" + f"log{date}.txt", mode="w")], format="%(asctime)s::%(message)s::%(levelname)s", level=logging.INFO, force=True)
    return logging