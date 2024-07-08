from dotenv import load_dotenv
import os 
import requests
import ctypes
import random
from tkinter import RIGHT, Tk,Button,Entry

load_dotenv()

client_key = os.getenv("access_key")
client_secret = os.getenv("client_secret")

def get_photo():
    wallpaper = entry.get()

    url = f"https://api.unsplash.com/photos/random?query={wallpaper}&orientation=landscape&client_id={client_key}"
    data = requests.get(url).json()
    if(len(data) == 1):
        if(data['errors'][0] == "No photos found."):
            print("No photos found on website, please try something else")
            exit()
    else:
         set_wallpaper(data)

def download(photo_url,destination_path, title):
    response = requests.get(photo_url)
    
    if response.status_code == 200:
        with open (destination_path + '/' + title + '.jpg', 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully")
    else:
        print(f"Failed to download iamge")
        
def set_wallpaper(data):
    photo_data = data
    photo_url = photo_data['urls']['full']
    image_title = photo_data['alt_description']
    download_path = os.getcwd() + "\\images"
    
    download(photo_url, download_path, image_title)
    
    filename = random.choice(os.listdir(os.getcwd() + "\\images"))
    
    path = os.getcwd() + f"\\images\\{filename}" 

    ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)
    exit()

window = Tk()

submit = Button(window, text='submit',command=get_photo)
submit.config(font=('Roboto',20))
submit.config(height=2)
submit.pack(side = RIGHT)


entry = Entry()
entry.config(font=('Roboto',50))
entry.config(bg='black')
entry.config(fg='white')
entry.insert(0, 'Enter Wallpaper')

entry.pack()
window.mainloop()

