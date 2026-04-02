"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


USERS = {
    "The Contradictory Empath": {
    "genre": "folk",
    "mood": "sad",
    "energy": 0.9,
    "likes_acoustic": True,
    },
    "The Genre Ghost": {
    "genre": "polka",
    "mood": "happy",
    "energy": 0.70,
    "likes_acoustic": False,
    },
    "The Tie Maker": {
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.385,   # exactly equidistant from 0.42 and 0.35
    "likes_acoustic": True,
    },
    "The Nostalgic Soul": {
    "genre": "country",
    "mood": "nostalgic",
    "energy": 0.54,
    "likes_acoustic": True,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in USERS.items():
        print(f"\n{'='*40}")
        print(f"User: {name}")
        print(f"{'='*40}")
        recommendations = recommend_songs(user_prefs, songs, k=3)
        for song, score, explanation in recommendations:
            print(f"  {song['title']} by {song['artist']} — Score: {score:.2f}")
            print(f"  Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
