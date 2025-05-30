class ui:
    def __init__(self, options: list, menu: str):
        self.options = options
        self.menu = menu

    def show(self):
        print(self.menu)
