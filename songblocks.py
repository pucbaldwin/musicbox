  
#!/usr/bin/env python
# from __future__ import print_function
from soco import SoCo
from time import sleep
import time
import nfc
import math

# import the library to control the LCD
import Adafruit_CharLCD as LCD

# import the My_Consumer_Key, My_Consumer_Secret, My_Access_Token & My_Token_Secret variables from the Secrets.py file
from Secrets import *

# import the twitter library
import tweetpony

# Set which pins on the PI are being used to control the LCD
lcd_rs        = 27  
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# this function gets called when a NFC tag is detected
def touched(tag):
    currentHour = time.localtime()[3]
    isNight = 0
    if currentHour < daytimeRange[0] or currentHour > daytimeRange[1]: # is it nighttime?
        isNight = 1

    if tag.ndef:
        message = tag.ndef.message
        for record in message:
            tag_text = nfc.ndef.TextRecord(record).text
            print ""
           
            if tag_text == "peter1":
                print "Playing Song 1"
                
                play_song(1)
            elif tag_text == "peter2":
                print "Playing Song 2"
                play_song(2)
            print ""


    else:
        print "Tag Misread - Sorry"

    return True   

def play_song(song_number):
    if song_number == 1:
        sonos.play_uri("x-sonos-spotify:spotify%3atrack%3a0mWTKA9sDTZjzRua0pzDHx?sid=9&flags=32&sn=1")
        print "Playing Nina Simone: Ain't Got No, I Got Life - Remix - Radio Edit"
        lcd.message("Nina Simone\nAin't Got No, I Got Life - Remix")
    elif song_number == 2:
        sonos.play_uri("x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1")
        sonos.seek('00:00:04')
        print "Playing Carly Rae Jepsen: Call Me Maybe"
        lcd.clear()
        lcd.message("Carly Rae Jepsen\nCall Me Maybe")
        tweet_text = "Maya is listening to Call Me Maybe by Carly Rae Jepsen"
        try:
            api.update_status(status = tweet_text)
        except tweetpony.APIError as err:
            print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
        else:
            print "Tweet sent successfully"

#TO DO - Refactor song names into Artist and Song Title



    
##    tag_uid = str(tag.uid).encode("hex")  # get the UID of the touched tag

    #Look up the song to play and set the right volume depending on whether it's day or night
##    if tag_uid in songs:
##        print("Tag touched: #" + songs[tag_uid][0] + ", UID: " + tag_uid)
##        print ("  Song: " + songs[tag_uid][1])
##        if isNight:
##            vol = int(round(nightVol * songs[tag_uid][2],0))
##            sonos.volume = vol
##            print ("  Nighttime song volume is " + str(vol))
##        else:
##            vol = int(round(dayVol * songs[tag_uid][2],0))
##            sonos.volume = vol
##            print ("  Daytime song volume is " + str(vol))
##        
##        sonos.play_uri(songs[tag_uid][4])  # play the song
##        print ("  Playing...")
##
##        # if the song has a time offset, skip to it.
##        if songs[tag_uid][3]:   
##                sonos.seek(songs[tag_uid][3])
##                print ("  Skipped to " + songs[tag_uid][3])                  
##    else:
##        print ("  No record for tag UID: " + tag_uid)

    # Tweet the song
##    tweet = songs[tag_uid][1] + time.strftime("\n%b %d %Y %H:%M:%S", time.localtime()) 
##    try:
##        status = twitter_api.update_status(status = tweet)
##    except tweetpony.APIError as err:
##        print ("  Tweet failed: ", err.description)
##    else:
##        print ("  Tweet sent")
##
##    return True


# Constants
dayVol = 50  # default daytime volume
nightVol = 25 # default nighttime volume
daytimeRange = [7,17] # daytime is 7:00a to 5:59p
sonos_ip = '192.168.1.31'
##url = 'x-sonos-http:_t%3a%3a17790141.mp3?sid=11&flags=32'  #default url
time_offset = ''  #time offset (to skip song intros)

songs = {
# block_number, title, vol % (for normalization), time_offset (to skip intros, 'HH:MM:SS'), url
'04436522c52980' : ['1','Paul Simon: Diamonds on the Soles of Her Shoes',1,time_offset,'x-sonos-http:_t%3a%3a17790141.mp3?sid=11&flags=32'],
'04926422c52980' : ['2','Nina Simone: To Love Somebody',1,time_offset,'x-sonos-http:_t%3a%3a2995780.mp3?sid=11&flags=32'],
'04dd3a22c52980' : ['3','Bob Marley: One Cup of Coffee',0.8,time_offset,'x-sonos-http:_t%3a%3a39299573.mp3?sid=11&flags=32'],
'04b56322c52980' : ['4','Adele: Best for Last',0.8,'00:00:36','x-sonos-http:_t%3a%3a2893061.mp3?sid=11&flags=32'],
'04e46422c52980' : ['5','Jack Johnson: We are Going to Be Friends',0.8,time_offset,'x-sonos-http:_t%3a%3a2807102%3a%3aa%3a%3a231444.mp3?sid=11&flags=32'],
'048b6322c52980' : ['6','The Hollies: The Mighty Quinn',0.8,time_offset,'x-sonos-http:_t%3a%3a2568562.mp3?sid=11&flags=32'],
'04216522c52980' : ['7','Raffi: Baa Baa Black Sheep',1.15,time_offset,'x-sonos-http:_t%3a%3a5425710%3a%3aa%3a%3a441322.mp3?sid=11&flags=32'],
'04df3a22c52980' : ['8','K\'naan: In the Beginning',0.75,'00:00:13','x-sonos-http:_t%3a%3a5407313.mp3?sid=11&flags=32'],
'04cb6422c52980' : ['9','Tuck & Patti: Honey Pie',1.3,'00:00:41','x-sonos-http:_t%3a%3a3053744.mp3?sid=11&flags=32'],
'04436422c52980' : ['10','Miriam Makeba: Pata Pata',0.9,'00:00:09','x-sonos-http:_t%3a%3a1163595.mp3?sid=11&flags=32'],
'049e6422c52980' : ['11','Yo-Yo Ma & Bobby McFerrin: Flight of the Bumblebee',1.2,time_offset,'x-sonos-http:_t%3a%3a8805968.mp3?sid=11&flags=32'],
'04536422c52980' : ['12','Desmond De Silva: Babi Achchee',0.8,time_offset,'x-sonos-http:_t%3a%3a43013728.mp3?sid=11&flags=32'],
}

# Twitter setup
print("Connecting to Twitter...")
api = tweetpony.API(consumer_key = My_Consumer_Key, consumer_secret = My_Consumer_Secret, access_token = My_Access_Token, access_token_secret = My_Token_Secret)
user = api.user
print "Connected to Twitter as @%s!" % user.screen_name
lcd.clear()
lcd.message('Connected to\nTwitter')
##else:
  ##  print ("Twitter connection error")
##print ("")


# Sonos setup
print("Connecting to Sonos...")
sonos = SoCo(sonos_ip)
print ("Connected to Sonos: " + sonos.player_name)
lcd.clear()
lcd.message('Connected to\nSonos & Twitter')
# Use this section to get the URIs of new songs we want to add
info = sonos.get_current_track_info()
print("Currently Playing: " + info['title'])
print("URI: " + info['uri'])
print("---")
print("") 


print("Setting up reader...")
reader = nfc.ContactlessFrontend('tty:AMA0:pn53x')
print(reader)
print("Ready!")
print("")
#lcd.clear()
#lcd.message('Do you want to\nhear a tune?')
lcd.blink(True)

while True:
    reader.connect(rdwr={'on-connect': touched})
    print("Tag released")
    sonos.stop()
    lcd.clear()
    print ("Sonos stopped")
    print ("---")
    print ("")
    sleep(0.1);
