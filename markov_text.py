import markovify

with open("text_data/zep.txt") as f:
    zep = f.read()

with open("text_data/whitman.txt") as f:
    whitman = f.read()

with open("text_data/songs.txt") as f:
    songs = f.read()

with open("text_data/trumpy.txt") as f:
    trumpy = f.read()

zep_model = markovify.Text(zep)
whitman_model = markovify.Text(whitman)
songs_model = markovify.Text(songs)

txt = markovify.combine([zep_model, songs_model], (2, 1))


print(txt.make_sentence())
