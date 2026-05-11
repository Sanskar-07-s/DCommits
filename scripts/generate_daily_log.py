import os
import datetime
import random
import json
import urllib.request
from pathlib import Path

# --- Fallback Data (In case internet is down) ---
FACTS = [
    "Agentic AI (2025): AI is shifting from passive chatbots to autonomous agents capable of planning and executing tasks.",
    "The first computer mouse was carved out of a block of wood in 1964.",
    "Ada Lovelace wrote the first algorithm for a machine in 1842.",
    "Approximately 90% of the world's money exists only in digital form.",
    "Python was named after the comedy troupe 'Monty Python', not the snake.",
    "The first 'bug' was a real moth found in a relay of the Harvard Mark II in 1947.",
    "SpaceX's Starlink has over 6,000 satellites providing global internet.",
    "AI is now designing entirely new proteins for breakthrough medical treatments.",
    "Digital Twins are real-time virtual replicas of city infrastructure used for optimization.",
    "6G networks are expected to be up to 100x faster than 5G.",
    "Microsoft is investing in small modular reactors to power AI data centers.",
    "Neuralink has successfully tested brain-computer interfaces in humans.",
    "Sodium-ion batteries are a sustainable alternative to lithium-ion.",
    "PHP originally stood for 'Personal Home Page'.",
    "Space Invaders aliens move faster because the processor rendered fewer sprites faster.",
    "The first hard drive, the IBM 305 RAMAC, was the size of two refrigerators and held 5MB.",
    "QWERTY was designed to slow down typists to prevent mechanical jams on typewriters."
]

QUOTES = [
    "Clean code is not written, it's rewritten.",
    "Simplicity is the soul of efficiency.",
    "Before you code, think about the data structures first.",
    "Don't comment what the code does, comment why it does it.",
    "Refactor early, refactor often.",
    "The best way to get a project done faster is to start sooner."
]

def fetch_hn_top_story():
    """Fetch the top story title and link from Hacker News."""
    try:
        # Get top story IDs
        with urllib.request.urlopen("https://hacker-news.firebaseio.com/v0/topstories.json") as response:
            ids = json.loads(response.read().decode())
            top_id = ids[0]
        
        # Get top story details
        with urllib.request.urlopen(f"https://hacker-news.firebaseio.com/v0/item/{top_id}.json") as response:
            story = json.loads(response.read().decode())
            return f"{story.get('title')} ({story.get('url', 'https://news.ycombinator.com/item?id=' + str(top_id))})"
    except Exception as e:
        print(f"Failed to fetch HN story: {e}")
        return None

def get_today_log_path(log_dir):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return Path(log_dir) / f"{today}.md"

def generate_daily_log():
    log_dir = os.environ.get("LOG_DIR", "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    log_path = get_today_log_path(log_dir)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    
    # Content Randomness
    daily_fact = random.choice(FACTS)
    daily_quote = random.choice(QUOTES)
    hn_story = fetch_hn_top_story()
    
    # Emoji Randomness
    emojis = ["🚀", "💡", "🧠", "🔥", "✨", "🛠️", "💻", "⚡", "🌈"]
    header_emoji = random.choice(emojis)
    
    # Template Selection (Randomized Layout)
    layouts = [
        # Layout A: Standard
        f"""# {header_emoji} Daily Dev Log | {date_str}

---

### 🌐 Tech Discovery from Web
> **Trending on HN:** {hn_story if hn_story else "Fetching fresh news..."}

### 💡 Daily Insight
> {daily_fact}

---

## 🧠 Learning & Discovery
- [ ] *What did you learn today?*

## 💻 Code & Implementation
- [ ] *Key features or bug fixes...*

## ⚠️ Challenges
- [ ] *Any issues faced?*

---
<p align="right"><i>Generated at {timestamp}</i></p>
""",
        # Layout B: Insight Focused
        f"""# {date_str} | Dev Journal {header_emoji}

> "{daily_quote}"

---

### 📰 Today's Tech Headline
- **Hacker News Top:** {hn_story if hn_story else "Exploring the digital frontier..."}

### 🔬 Fact of the Day
Did you know? {daily_fact}

---

## 📝 Work Logs
- [ ] Task 1...
- [ ] Task 2...

## 📅 Roadmap
- [ ] Tomorrow's goals...

---
<p align="center"><i>System Update: {timestamp}</i></p>
"""
    ]
    
    template = random.choice(layouts)

    if not log_path.exists():
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"Created new log: {log_path}")
    else:
        # Append update section with random message
        update_msgs = [
            f"\n\n## 🔄 Update @ {timestamp}\n- Pushed new iterations and refined logic.",
            f"\n\n## ⚡ Quick Sync @ {timestamp}\n- Resolved pending tasks and optimized flow.",
            f"\n\n## 🧪 Experimentation @ {timestamp}\n- Tested new patterns and validated results.",
            f"\n\n## 🛠️ Refinement @ {timestamp}\n- Polishing code structure and documentation.",
            f"\n\n## 🛰️ Remote Sync @ {timestamp}\n- Synchronizing local progress with repository state.",
            f"\n\n## 🌊 Flow Update @ {timestamp}\n- Maintaining momentum on current development branch."
        ]
        update_content = random.choice(update_msgs)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(update_content)
        print(f"Appended update to: {log_path}")

if __name__ == "__main__":
    generate_daily_log()
