"""
Chapter 9 example (Page 228)
Program: checkbuttondemo.py
3/10/2025

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run properly!

GUI-based app demonstrating the use of the check button (checkbox) graphic component to create a food order.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here 

# Class Header (class name will change from project to project)
class CheckbuttonDemo(EasyFrame):

	# Defintion of our classes' constructor method
	def __init__(self):
		# Call to the EasyFrame class constructor
		EasyFrame.__init__(self, title = "Check Button Demo", width = 320, height = 200, resizable = False, background = "#75DDDD")
		# Other components are added here 
		 
		# Add four check buttons 
		self.chickCB = self.addCheckbutton (text = "Chicken", row =1, column = 0)
		self.taterCB = self.addCheckbutton(text = "French Fries", row = 1, column = 1)
		self.beanCB = self.addCheckbutton(text = "Green Beans", row = 2, column = 0)
		self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 2, column = 1)

		#Change some color properties of the check buttons
		self.chickCB["background"] = "#75DDDD"
		self.taterCB["background"] = "#75DDDD"
		self.beanCB["background"] = "#75DDDD"
		self.sauceCB["background"] = "#75DDDD"

		# Add the command button
		self.button = self.addButton(text = "Place Order", row = 3, column = 0, columnspan = 2, command = self.placeOrder)

		self.button["background"] = "#689689"
		self.button["foreground"] = "white"
		self.button["width"] = 24
		self.button["height"] = 2
		#self.button["font"] = Font(size = 14)

    # Definition of the placeOrder() method which is the event handler
    def placeOrder(self):
    	""" Display a message pop-up box with the order summary. """
    	message = ""

    	# Analyze each Check Button to see if they have been checked 
    	if self.chickCB.isChecked():
    		message += "Chicken\n\n"

    	if self.taterCB.isChecked():
    		message += "French Fries\n\n"

    	if self.beanCB.isChecked():
    		message += "Green Beans\n\n"

    	if self.sauceCB.isChecked():
    	    message += "Applesauce\n\n"	

    	if message == "":
    		message = "Sorry, no food ordered! Try again!"

    	# Now that we have looked at every check button, let's push the message string to a pop up
    	self.messageBox(title = "Customer Order", message = message)
# End of class block

# Global definition of the main() function
def main():
	# Instantiate an object from the class into mainloop()
	CheckbuttonDemo().mainloop()

# Global call to main() for program entry.
if __name__ == '__main__':
	main()