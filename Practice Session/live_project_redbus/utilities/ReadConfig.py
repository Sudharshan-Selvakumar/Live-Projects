import configparser

ini_data = configparser.RawConfigParser()
ini_data.read(r"C:\Users\ssudharv\PycharmProjects\Practice Session\live_project_redbus\configurations\config.ini")

class ReadProperty():
    @staticmethod
    def geturl1():
        return ini_data.get("travelling city 1", "url")
    @staticmethod
    def getfromcity1():
        return ini_data.get("travelling city 1", "from")

    @staticmethod
    def gettocity1():
        return ini_data.get("travelling city 1", "to")

    @staticmethod
    def geturl2():
        return ini_data.get("travelling city 2", "url")

    @staticmethod
    def getfromcity2():
        return ini_data.get("travelling city 2", "from")

    @staticmethod
    def gettocity2():
        return ini_data.get("travelling city 2", "to")

    @staticmethod
    def geturl3():
        return ini_data.get("travelling city 3", "url")

    @staticmethod
    def getfromcity3():
        return ini_data.get("travelling city 3", "from")
    @staticmethod
    def gettocity3():
        return ini_data.get("travelling city 3", "to")
