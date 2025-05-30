from vm import vm
from ui.main_ui import main_ui

vm = vm()
ui = main_ui()

def main():
    while True:
        task = ui.show()
        vm.do(task)

if __name__ == "__main__":
    main()