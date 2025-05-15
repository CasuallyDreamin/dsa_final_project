SEPERATOR = "-"
FILE_PATH = "./files/"

class FileManager:
    def __init__(self, address:str, seperator:str = SEPERATOR):
        self.address = address
        self.seperator = seperator
                
    def read(self) -> list:
        # read a file and return data
        array = []

        try:
            f = open(self.address, "r")
        except FileNotFoundError:
            # if not found, make file
            self.write()
            f = open(self.address, "r")

        data = f.read()    
        data = data.split("\n")
        array = [line.split(self.seperator) for line in data]
        
        f.close()
        return array


    def write(self, data: str) -> bool:
        # write data to a file
        # TODO: data should be iterable 
        try:
            f = open(self.address, "w")
            f.write(data)
            f.close()
            return True
        except:
            print(f" {self.address} Write failed.")
            return False
        
    def append(self, data: str) -> bool:
        try:
            f = open(self.address, "a")
            f.write("\n" + data)
            f.close()
            return True
        except:
            print(f" {self.address} Write failed.")
            return False


DR_FILE_NAME = "doctors.txt"
DR_ADDRESS_FILE = FILE_PATH + DR_FILE_NAME

doctor_file_manager = FileManager(DR_ADDRESS_FILE)