from .base_ui import UI
from .user_panel_ui import UserPanelUI
from .admin_panel_ui import AdminPanelUI
from clear_screen import clear

class MainUI(UI):
    def __init__(self, vm):
        menu = """
1. User Panel
2. Admin Panel
0. exit
"""     
        options = 3
        super().__init__(options, menu, vm)
        self.user_panel = UserPanelUI(vm = self.vm)
        self.admin_panel = AdminPanelUI(vm = self.vm)
    
    def do_task(self, task_id):
        if task_id == "1": self.run_user_panel()
        elif task_id == "2": self.run_admin_panel()
        elif task_id == "0":
            clear()
            self.running = False

    def run_user_panel(self):
        user_panel = self.user_panel
        user_panel.running = True

        while user_panel.running:
            clear()
            user_panel.show()
            user_panel.do_task(user_panel.get_option())


    def run_admin_panel(self):
        admin_panel = self.admin_panel
        admin_panel.running = True

        while admin_panel.running:
            clear()
            admin_panel.show()
            admin_panel.do_task(admin_panel.get_option())
            
    