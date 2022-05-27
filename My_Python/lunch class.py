class Lunch(object):
    def __init__(self,menu):
        self.menu=menu
        
    def menu_price(self):
        if self.menu=="menu1":
            print("Your choice:",self.menu,"Price:12.00")
        elif self.menu=="menu2":
            print("Your choice:",self.menu,"Price 13.40")
        else:
            print("Error in menu")
        
Paul=Lunch("menu1")
Paul.menu_price()
