class UI:
    def __init__(self, options: int, menu: str, vm):
        self.options = options
        self.menu = menu
        self.running = False
        self.vm = vm

    def show(self):
        curr_user = self.vm.curr_user
        sys_date = self.vm.sys_date

        if curr_user or sys_date:
            print(f"user: {curr_user} \ntime: {sys_date}")
        
        print(self.menu)

    def get_option(self):
        try:
            option = int(input("$ "))
        except ValueError:
            input("option must be a number.")
            return
        if not (0 <= option < self.options):
            input("invalid option.")
            return 

        return str(option)
    
    def do_task(self, task_id: str):
        # override this func for all functionality
        return

