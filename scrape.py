from PyLyrics import *
from random import *

#pick a random album

all_albums = PyLyrics.getAlbums(singer='Frank Ocean')
rand_num_album = (randint(0,2))
rand_album = all_albums[rand_num_album]

#Pick a random track
all_tracks =  PyLyrics.getTracks(all_albums[rand_num_album])
rand_num_track = (randint(0,len(all_tracks)-1))
rand_track = all_tracks[rand_num_track]
print(rand_track)
if rand_track == "Goldeneye" or "White": #these songs are 1 line long going to hard code ignore it
    rand_num_track = (randint(0,len(all_tracks)-1))
    rand_track = all_tracks[rand_num_track]


all_lyrics = rand_track.getLyrics()
#print((all_lyrics))
ascii_lyric = all_lyrics.encode("utf-8")
#print(ascii_lyric)
rand_num_lyric = (randint(0,len(ascii_lyric)-1))
# print(len(ascii_lyric))
# print(rand_num_lyric)

#Find the first new line
while not ascii_lyric[rand_num_lyric] == '\n' and (rand_num_lyric < len(ascii_lyric)):
    rand_num_lyric += 1
#Make sure it doesn't start at a space line or something weird
while ascii_lyric[rand_num_lyric].isspace() and (rand_num_lyric < len(all_lyrics)):
     rand_num_lyric += 1

#print(rand_num_lyric)

#Lyric string starts at first letter
final_lyric = ascii_lyric[rand_num_lyric]
rand_num_lyric += 1

#Lyric string ends at last letter before newline
while not ascii_lyric[rand_num_lyric] == '\n' and (rand_num_lyric < len(ascii_lyric)):
    final_lyric += ascii_lyric[rand_num_lyric]
    rand_num_lyric += 1

# while not all_lyrics[rand_num_lyric].isupper() and (rand_num_lyric < len(all_lyrics)):
#     final_lyric += all_lyrics[rand_num_lyric]
#     rand_num_lyric += 1
#

print final_lyric
