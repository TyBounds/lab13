#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
enemy = drawpad.create_rectangle(300,290,410,300, fill="Black")
enemy2 = drawpad.create_rectangle(0,100,110,110, fill="Black")
enemy3 = drawpad.create_rectangle(800,400,690,410, fill="Black")
# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="Right", background= "red")
       	    self.right.grid(row=0,column=3)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="Left", background= "blue")
       	    self.left.grid(row=0,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "Purple")
       	    self.down.grid(row=0,column=2)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    # Bind an event to the first button
       	 
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    
	    
	    
	    
	    
	    
	    global drawpad
	    global player
	    global enemy
	    global enemy2
	    global enemy3
	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
		
		
app = MyApp(root)
root.mainloop()