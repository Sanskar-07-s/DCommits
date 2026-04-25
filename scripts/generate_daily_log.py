import os
import datetime
from pathlib import Path

import random

TIPS = [
    "Clean code is not written, it's rewritten.",
    "The best way to get a project done faster is to start sooner.",
    "Before you code, think about the data structures first.",
    "Don't comment what the code does, comment why it does it.",
    "Always leave the code specialized and the data generalized.",
    "Simplicity is the soul of efficiency.",
    "The most dangerous phrase in the language is, 'We've always done it this way.'",
    "Testing is not about finding bugs, it's about gaining confidence.",
    "Refactor early, refactor often.",
    "A language that doesn't affect your way of thinking about programming is not worth knowing."
]

def get_today_log_path(log_dir):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return Path(log_dir) / f"{today}.md"

def generate_daily_log():
    log_dir = os.environ.get("LOG_DIR", "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    log_path = get_today_log_path(log_dir)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    daily_tip = random.choice(TIPS)
    
    template = f"""# 📝 Daily Dev Log | {datetime.datetime.now().strftime("%B %d, %Y")}

---

### 💡 Daily Dev Tip
> {daily_tip}

---

## 🧠 Learning & Discovery
- [ ] *What did you learn today?*

## 💻 Code & Implementation
- [ ] *Key features or bug fixes...*

## ⚠️ Challenges & Roadblocks
- [ ] *Any issues faced?*

## ✅ Solutions & Breakthroughs
- [ ] *How did you solve them?*

## 📅 Plan for Tomorrow
- [ ] *Next steps...*

---
<p align="right">
  <i>Generated with ❤️ at {timestamp}</i>
</p>
"""

    if not log_path.exists():
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"Created new log: {log_path}")
    else:
        # Append update section
        update_content = f"\n\n## Update @ {timestamp}\n- Continued working on refined tasks."
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(update_content)
        print(f"Appended update to: {log_path}")

if __name__ == "__main__":
    generate_daily_log()
