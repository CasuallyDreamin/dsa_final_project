SEPERATOR = "-"
FILE_PATH = "./Files"

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

# NOTE: USAGE
# X_FILE_NAME = "/X.txt"
# X_FILE_ADDRESS = FILE_PATH + DR_FILE_NAME
# X_file_manager = FileManager(X_FILE_ADDRESS)

# file names

CARS_FILE_NAME              = "/cars.txt"
USERS_FILE_NAME             = "/users.txt"
CITYCODE_FILE_NAME          = "/citycode.txt"
DRIVERS_FILE_NAME           = "/drivers.txt"
OWNERSHIP_HISTORY_FILE_NAME = "/ownership_history.txt"
PENALTIES_FILE_NAME         = "/penalties.txt"
PHASE4_FILE_NAME            = "/phase4.txt"

# file addresses

CARS_FILE_ADDRESS               = FILE_PATH + CARS_FILE_NAME
USERS_FILE_ADDRESS              = FILE_PATH + USERS_FILE_NAME
CITYCODE_FILE_ADDRESS           = FILE_PATH + CITYCODE_FILE_NAME
DRIVERS_FILE_ADDRESS            = FILE_PATH + DRIVERS_FILE_NAME
OWNERSHIP_HISTORY_FILE_ADDRESS  = FILE_PATH + OWNERSHIP_HISTORY_FILE_NAME
PENALTIES_FILE_ADDRESS          = FILE_PATH + PENALTIES_FILE_NAME
PHASE4_FILE_ADDRESS             = FILE_PATH + PHASE4_FILE_NAME

# file managers

cars_file_manager     = FileManager(CARS_FILE_ADDRESS)
users_file_manager    = FileManager(USERS_FILE_ADDRESS)
citycode_file_manager = FileManager(CITYCODE_FILE_ADDRESS)
drivers_file_manager  = FileManager(DRIVERS_FILE_ADDRESS)