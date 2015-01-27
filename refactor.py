  
#!/usr/bin/env python


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

mayasongs = {
    #tagtext, title, vol%, time_offset, url
'peter2' : ['1','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
'peter3' : ['2','Nina Simone: Aint Got No, I Got Life - Remix - Radio Edit',1,'00:00:00', 'x-sonos-spotify:spotify%3atrack%3a0mWTKA9sDTZjzRua0pzDHx?sid=9&flags=32&sn=1'],
'peter4' : ['3','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
'peter5' : ['4','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
'peter6' : ['5','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
'peter7' : ['6','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
'peter8' : ['7','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
'peter9' : ['8','Carly Rae Jepson: Call me maybe',1,'00:00:09', 'x-sonos-spotify:spotify%3atrack%3a5unfeZUhKhICP73CDYBW4N?sid=9&flags=32&sn=1'],
}
for song, details in mayasongs.iteritems():
    print song
    print details


#print mayasongs['peter2'][4]