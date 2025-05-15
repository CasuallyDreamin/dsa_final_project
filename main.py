from file_manager import doctor_file_manager

def func(input: any = None) -> any:
    db = doctor_file_manager
    db.write("hi-y")
    db.append("bye-x")
    print(db.read())

def main():
    func()

if __name__ == "__main__":
    main()