# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

This recommender suggests songs based on a user's mood, genre, energy level, and acoustic preference. It assumes the user can describe their taste with those four inputs. It is built for classroom exploration - not a real app - but it models how real recommender systems make decisions.

---

## 3. How the Model Works

Every song in the catalog gets a score based on how well it matches what the user wants. Here is how the points are handed out:

- **Genre match** - if the song's genre matches the user's favorite, it gets +1 point.
- **Mood match** - if the song's mood matches, it gets +2 points. Mood is weighted higher because it has the strongest effect on how a song feels.
- **Energy proximity** - the closer the song's energy is to the user's target, the more points it earns, up to +2. A perfect match gives the full 2 points; a total mismatch gives 0.
- **Acousticness fit** - if the user likes acoustic music and the song is acoustic (or vice versa), the song gets +1 point.

The maximum a song can score is 6. Songs are ranked from highest to lowest, and the top results are returned. Compared to the starter code, energy was doubled in importance and genre was halved, so finding the right energy level matters more than matching a genre label.

---

## 4. Data

The catalog has 10 songs. Genres included are pop, lofi, rock, ambient, jazz, synthwave, and indie pop. Moods include happy, chill, focused, intense, relaxed, and moody. No songs were added or removed from the starter dataset. Several genres and moods common in real life are missing entirely - there is no hip-hop, EDM, folk, R&B, or metal. There is also no way to express preferences like tempo, danceability, or emotional valence, even though those fields exist on every song.

---

## 5. Strengths

The system works best when the user's preferences closely match what is in the catalog. The Late Night Studier (lofi, focused, low energy, acoustic) gets a perfect-score recommendation because every dimension lines up. Energy proximity works well as a continuous signal - it does not just ask "high or low?" but finds the closest match across the whole range. The acousticness rule also works cleanly: users who prefer acoustic tracks reliably get quieter, more organic-sounding songs at the top of their list.

---

## 6. Limitations and Bias

**Genre representation imbalance creates a filter bubble.** The catalog has three lofi songs but only one each for rock, jazz, ambient, synthwave, and indie pop. A lofi fan gets three chances to earn the genre bonus while a jazz fan gets only one. Lofi songs end up near the top of nearly every acoustic, low-energy user's list — not because they are the best match, but because there are more of them.

**Missing genres mean some users get nothing relevant.** Hip-hop, EDM, and folk do not exist in the catalog at all. A user who asks for those genres will never earn the genre bonus, and the recommender silently falls back to energy and acousticness without explaining why.

**Mood is the heaviest signal, but mood coverage is thin.** With only six moods across ten songs, many user moods will never match anything. That +2 mood bonus - the biggest single weight — is simply unavailable to those users, and the recommender gives no indication that anything is wrong.

---

## 7. Evaluation

Four distinct user profiles were tested, each representing a different listening personality:

- **The Hype Beast** - high energy (0.80), hip-hop genre, confident mood, non-acoustic. Represents a genre-focused, high-intensity listener.
- **The Late Night Studier** - moderate energy (0.40), lofi genre, focused mood, acoustic. Represents a calm, concentration-oriented listener.
- **The Weekend Warrior** - very high energy (0.95), EDM genre, euphoric mood, non-acoustic. Represents an extreme-energy party listener.
- **The Sunday Morning** - low energy (0.25), folk genre, peaceful mood, acoustic. Represents a quiet, relaxed morning listener.

The most surprising result was that The Hype Beast - a hip-hop fan wanting confident music - received zero genre or mood matches in their top 3. The recommender fell back entirely on energy and acousticness, returning pop and synthwave tracks with no explanation. It was also striking that The Late Night Studier was the only profile to hit a perfect score of 6.00, while every other user's top score was under 3.0 — a gap that comes entirely from lofi being the best-represented genre in the catalog.

---

## 8. Future Work

- Add more songs, especially for underrepresented genres like hip-hop, EDM, and folk.
- Use valence and danceability in the score — they are already loaded but never used.
- Add a warning when a user's genre or mood has no matches in the catalog.
- Cap how many songs from the same genre can appear in the top results, so recommendations feel more varied.
- Try fuzzy mood matching so that "wistful" and "sad" are treated as similar rather than completely different.

---

## 9. Personal Reflection

Building this recommender made it clear how much the catalog shapes the output - the model is only as good as the data it has to work with. The most interesting discovery was how a user's top score can differ by 3 or 4 points not because of their preferences, but simply because their favorite genre happens to have more songs. That kind of invisible bias is easy to miss until you run the numbers. It changed the way I think about Spotify or Apple Music recommendations - when an app keeps suggesting the same artists, it might not be learning your taste so much as reflecting what is most represented in its catalog.
