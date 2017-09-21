class Song (object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

Take_me_to_the_ball_game = Song(["take me out to the ball game", "buy me some salad and tofu", "Im Vegan"])

Secrets_song = Song(["Tell me what you want to hear", "im not insencere", "oh actuall i am"])

Take_me_to_the_ball_game.sing_me_a_song()

Secrets_song.sing_me_a_song()
