import pandas as pd


def load_play_history(file, orient):
    spotify = pd.read_json(file, orient=orient)

    print(spotify)


load_play_history('spotifyfiles/Userdata.json', 'index')

load_play_history('spotifyfiles/SearchQueries.json', 'records')

load_play_history('spotifyfiles/FamilyPlan.json', 'columns')
