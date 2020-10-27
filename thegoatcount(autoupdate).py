## Heat Sealer Counter ##

import tkinter as tk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime
import json
#import RPi.GPIO as GPIO
import time
import threading
import schedule
#from datetime import datetime, timedelta
#from threading import Timer

################################ Google Sheets and Drive API ###############################

# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
#sheet = client.open("Daily Count - Heat Sealer").sheet1
spreadsheetName = "Daily Count - Heat Sealer"
sheetName = "Test"
spreadsheet = client.open(spreadsheetName)
sheet = spreadsheet.worksheet(sheetName)




# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#pprint(list_of_hashes)

################################ Global Var ###############################

#GPIO.setmode(GPIO.BCM)
PIR_PIN = 23
#GPIO.setup(PIR_PIN, GPIO.IN)
number = 0
date = 2
count = 2
mainLabel = "Heat Sealer Counter"
updatelabel = "Count updated successfully :D"


## Window creation + Geometry ##
root = tk.Tk()
root.geometry("800x480")
root.config(bg="white")
root.wm_title("Sealing Station A")

## reacurrring time ###
#x = datetime.today()
#y = x.replace(day=x.day, hour=00, minute=00, second=0, microsecond=0) + timedelta(days=1)
#delta_t = y - x

#secs = delta_t.seconds+1
################################ Functions ###############################




def counupdateWindow():
    popup = tk.Tk()
    popup.geometry("300x150")
    popup.config(bg="white")
    popup.wm_title("Count Updater")
    countupdateLabel = tk.Label(popup, text=updatelabel, font=("Helvetica", 15), bg="white")
    countupdateLabel.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="OK", font=("Helvetica", 15, 'bold'), bg='green2', height=3, width=8, command=popup.destroy)
    B1.pack(side='bottom', pady=30)
    popup.eval('tk::PlaceWindow %s center' % popup.winfo_pathname(popup.winfo_id()))
    popup.mainloop()
    




def updateDate():
    global date
    date += 1
    return str(date)

def updateCount():
    global count
    count += 1
    return str(count)
    

def plusOne():
    global number
    number += 1
    count.config(text=number)

def minusOne():
    global number
    number -= 1
    count.config(text=number)

def resetCount():
    global number
    number = 0
    count.config(text=number)
    
def numberToString():
    global number
    return str(number)    

def changemainLabel():
    mainLabel = "Update Successfull!"
    label.config(text=mainLabel, fg='green2')
    #root.after(1000)

def changemainlabelBack():
    #time.sleep(1)
    mainLabel = "Heat Sealer Counter"
    label.config(text=mainLabel, fg='black')


def updateSheet():
    sheet.insert_row([])
    sheet.update("A1", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sheet.update("B1", number)
    sheet.update('C1', 'Sealing Station 2')


def startCounter():
    
    while True:
    
        #i=GPIO.input(PIR_PIN)
        
    
        if i==0:
            root.after(750)
            #break
            i==1
            plusOne()
            count.config(text=number)
        #print(count)
            #print("motion detected")
            root.update()

    #GPIO.cleanup()



schedule.every().day.at("00:00").do(updateSheet)


def scheduler():
    
    while True:
        schedule.run_pending()
        time.sleep(1)

   

################################ GUI #####################################

label = tk.Label(root, text=mainLabel, bg="white") # Creates a text label
label.pack() # Pack label into the window
label.config(font=("Helvetica", 15)) # Sets font of label

count = tk.Label(root, text=number, bg="white") # Creates a text label
count.pack() # Pack label into the window
count.config(font=("Helvetica", 50)) # Sets font of label

uploadButton = tk.Button(root, text ="Upload Daily Count", height=2, width=16, command=lambda:[updateSheet(), counupdateWindow()])
uploadButton.pack(pady=10) #creates start counting button !!!Remeber to add command!!!
uploadButton.config(font=("Helvetica", 10, 'bold'))

plusButton = tk.Button(root, bg='green2', text ="+", height=3, width=20, command=plusOne)
plusButton.pack(pady=10) #creates +1 counting button !!!Remeber to add command!!!
plusButton.config(font=("Helvetica", 10, 'bold'))

minusButton = tk.Button(root, bg='IndianRed1', text ="-", height=3, width=20, command=minusOne)
minusButton.pack(pady=10) #creates +1 counting button !!!Remeber to add command!!!
minusButton.config(font=("Helvetica", 10, 'bold'))

resetButton = tk.Button(root, text ="Reset Counter", height=2, width=15, command=lambda:[resetCount(), changemainlabelBack()])
resetButton.pack(pady=10) 
resetButton.config(font=("Helvetica", 10, 'bold'))

################################ GUI #####################################




thread = threading.Thread(target=startCounter)
thread.daemon = True
thread.start()

thread2 = threading.Thread(target=scheduler)
thread2.start()

root.mainloop()

#while True:
    #schedule.run_pending()
    #time.sleep(1)