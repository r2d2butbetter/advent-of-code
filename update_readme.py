import requests
import json

# Fetch the Advent of Code leaderboard data
session_cookie = os.getenv("SESSION_COOKIE")
url = "https://adventofcode.com/2024/leaderboard/private/view/2469665.json"
headers = {
    "Cookie": f"session={session_cookie}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    leaderboard_data = response.json()
else:
    print(f"Failed to retrieve data: {response.status_code}")
    exit(1)

# Format the leaderboard data for the README file
leaderboard_stats = ""
for member in leaderboard_data['members'].values():
    leaderboard_stats += f"{member['name']}: {member['local_score']} points\n"

# Update the README file
with open("README.md", "r") as readme_file:
    readme_content = readme_file.readlines()

# Assume the stats section starts with a specific marker
start_marker = "<!-- AOC-STATS-START -->\n"
end_marker = "<!-- AOC-STATS-END -->\n"

start_index = readme_content.index(start_marker) + 1
end_index = readme_content.index(end_marker)

# Replace the old stats with the new stats
readme_content[start_index:end_index] = [leaderboard_stats]

with open("README.md", "w") as readme_file:
    readme_file.writelines(readme_content)
