import tkinter as tk
import webbrowser
import threading
import pyautogui
import keyboard
import time
import pyperclip
import subprocess
import sys



# File paths
pathm = r'C:\Users\Sarah_\VSCODE\macro.txt'
pathh = r'C:\Users\Sarah_\VSCODE\height.txt'

# Function to open a URL in the web browser
def callback(url):
    webbrowser.open_new(url)

# Macro Application Class
class MacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BTE Macro")
        self.root.geometry("250x250")

        # Load settings
        with open(pathm, 'r') as opened_file:
            self.macro = opened_file.readline().strip()
        with open(pathh, 'r') as opened_file:
            self.height = opened_file.readline().strip()

        self.macr = tk.StringVar(value=self.macro)
        self.yz = tk.StringVar(value=self.height)

        # Setup GUI
        logo = """
              ..+*#####***#%%%%%####-.          
          ...*%%##*******%##%%%%%%%%@@%-..      
         .:=%##********#%%%%%%%%%%%%%%%%+-..    
       .:*##********##%%%%%%%%%%%%%%%%%%%%*-... 
     ..+%#*********#%%%%%%%%%%%%%%%%%%%%##%%%...
     :###*******++*#%%%%%%%%%%%%%%%%%%%%%%###%= 
    :=##********+*#####%%%%%%%%%%%%%%%%%%#####+:
    =@#*****#####*+#####%%%%%%%%%%%%%%%%######%*
    =@%#**##%###########%%%%%%%%%%%%%%%%%%####%*
    @%%#**+*%%%#%#######%%%%%%%%%%%%%%%%%%######
    @%%%##**###*#*+*####%%%%%%%%%%%%%%%%%%%####%
    @%%%%%###***###*####%*#%%%%%%%%%%%%%%%%%%%%@
    @%%%%%%%%%%%%#+*##*#%#*#%%%%%%%%%%%%%%%%%%%@
    @%%%%%%%%%%###****#*******##%%%%%%%%%%%%%%%@
    @%%%%%%%%%%#****************#%%%%%%%%%%%%%%@
    =@%%%%%%%%%%%#************#####%%%%%%%%%%@@#
    =@%%%%%%%%%%%#*********########%%%%%%%%%%@@#
    -#%%%%%%%%%%%%%%#**############%%%%%%%%%%@%+
     :%%%%%%%%%%%%%%%%%##########%%%%%%%%%%%@@=.
     ..*@%%%%%%%%%%%%%%#######%%%%%%%%%%%%%@%...
       .:#%%%%%%%%%%%%%######%%%%%%%%%%%%@%=... 
        ..=*@%%%%%%%%%%######%%%%%%%%%%@#+...   
          ..:#@@%%%%%%%####%%%%%%%%%%##-....    
           .....*%%%%%%%##%@@@%@%##*-...        


        """
        label = tk.Label(self.root, text=logo, font=("Courier", 5))
        label.pack()

        # Drop Down Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Settings', command=self.open_settings)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.quit_ch)
        helpmenu = tk.Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='Contact Me', command=self.contact)

        # Start the macro detection thread
        self.set_macro()

    def set_macro(self):
        # Start the key detection in a separate thread
        threading.Thread(target=self.detect_macro, daemon=True).start()

    def detect_macro(self):
        def on_macro_key_press():
            text = pyperclip.paste()
            
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.5)
            pyautogui.press('esc')
            time.sleep(0.5)
            pyautogui.press('/')
            time.sleep(0.5)
            pyautogui.write('tpll ')
            pyautogui.typewrite(text)
            time.sleep(0.5)
            pyautogui.press('space')
            time.sleep(0.5)
            pyautogui.write(self.height)
            time.sleep(0.5)
            pyautogui.press('enter')

        # Set up the key detection
        keyboard.add_hotkey(self.macro, on_macro_key_press)
        
        # Keep the thread alive and wait for the macro key press
        keyboard.wait()

    def restart_(self):
        # Destroy the main window
        self.root.destroy()
        # Restart the application
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    # Open the settings window
    def open_settings(self):
        settings = tk.Toplevel(self.root)
        settings.title("Settings")
        settings.geometry("300x250")

        tk.Label(settings, text="Macro Key").grid(row=0)
        mac = tk.Entry(settings, textvariable=self.macr, width=10)
        mac.grid(row=0, column=1)

        tk.Label(settings, text="Tp Height").grid(row=1)
        y = tk.Entry(settings, textvariable=self.yz, width=10)
        y.grid(row=1, column=1)

        def save_settings():
            self.macro = self.macr.get()
            self.height = self.yz.get()
            with open(pathm, 'w') as opened_file:
                opened_file.write(self.macro)
            with open(pathh, 'w') as opened_file:
                opened_file.write(self.height)
            settings.destroy()

        tk.Button(settings, text="Save", width=7, command=lambda:[save_settings(), self.restart_()]).place(x=225, y=50)

    
    
        
    # Show a contact window with a link to Discord
    def contact(self):
        c = tk.Tk()
        c.title("Contact Me")
        c.geometry("150x75")
        label = tk.Label(c, text="Contact Me On Discord")
        label.pack()
        link1 = tk.Label(c, text="Discord", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://discord.gg/muq2zVTZ"))

    # Confirm quitting the application
    def quit_ch(self):
        qui = tk.Toplevel(self.root)
        qui.title("Warning")
        qui.geometry("250x150")
        lbl = tk.Label(qui, text="Are You Sure You Want To Quit?")
        lbl.place(x=45, y=20)
        yes = tk.Button(qui, text="Yes", width=10, command=self.root.quit)
        yes.place(x=20, y=75)
        no = tk.Button(qui, text="No", width=10, command=qui.destroy)
        no.place(x=155, y=75)

# Initialize and run the application
root = tk.Tk()
app = MacroApp(root)
root.mainloop()