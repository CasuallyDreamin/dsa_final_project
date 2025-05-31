from viewmodel import ViewModel
from ui.main_ui import MainUI
from clear_screen import clear
from db import DataBase

def main():
    db = DataBase()
    vm = ViewModel(db)
    ui = MainUI(vm = vm)
    ui.running = True

    while ui.running:
        clear()
        ui.show()
        ui.do_task(ui.get_option())
        
    # tell view model to save data into files

if __name__ == "__main__":
    main()