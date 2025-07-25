from viewmodel import ViewModel
from ui.main_ui import MainUI
from clear_screen import clear
from db import db

def main():
    vm = ViewModel(db)
    ui = MainUI(vm = vm)
    ui.running = True

    while ui.running:
        clear()
        ui.show()
        ui.do_task(ui.get_option())
        
    db.save()

if __name__ == "__main__":
    main()