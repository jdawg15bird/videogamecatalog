import pandas as pd

# Read the original CSV file
games = pd.read_csv("video_games_raw.csv")

print("VIDEO GAME CATALOG MANAGER")
print(games[["Title"]])  # Show row numbers and game titles

row = int(input("\nEnter a row number to inspect: "))

# iloc gets a game by its row number
print("\nSelected Game:")
print(games.iloc[row])

# at changes one value (the selected game's status)
status = input("\nEnter a new status: ")
games.at[row, "Status"] = status

# Start by marking every game as not recommended
games["Recommended"] = "No"

# loc changes multiple rows that meet BOTH conditions
games.loc[(games["Rating"] >= 8) & (games["Price"] <= 40), "Recommended"] = "Yes"

# query finds games marked Yes
print("\nRecommended Games:")
print(games.query("Recommended == 'Yes'")[["Title", "Platform", "Price", "Rating"]])

# Save to a NEW file so the original stays unchanged
games.to_csv("video_games_cleaned.csv", index=False)
print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv.")
