import os
import json
from datetime import datetime, timezone
import urllib.request

token = os.environ["GITHUB_TOKEN"]
username = "jjuunnii98"

payload = json.dumps({
    "query": """
    {
      user(login: "%s") {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """ % username
}).encode()

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=payload,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    },
)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read())

weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
days = sorted(
    [d for w in weeks for d in w["contributionDays"]],
    key=lambda d: d["date"],
)

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Count streak backwards from today.
# If today has 0 contributions, skip it (day isn't over yet) and start from yesterday.
streak = 0
for day in reversed(days):
    if day["date"] > today:
        continue
    if day["contributionCount"] > 0:
        streak += 1
    elif day["date"] < today:
        break

color = "brightgreen" if streak >= 7 else "orange" if streak >= 3 else "yellow"
badge = {
    "schemaVersion": 1,
    "label": "streak",
    "message": f"{streak} days",
    "color": color,
    "style": "flat-square",
    "namedLogo": "github",
}

with open("streak.json", "w") as f:
    json.dump(badge, f, indent=2)

print(f"Streak: {streak} days")
