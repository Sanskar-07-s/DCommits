import unittest
import os
import shutil
from pathlib import Path
import datetime
from scripts.generate_daily_log import get_today_log_path

class TestDailyLog(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_logs"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        os.environ["LOG_DIR"] = self.test_dir

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if "LOG_DIR" in os.environ:
            del os.environ["LOG_DIR"]

    def test_log_creation(self):
        # Import inside to ensure env var is picked up if needed, though get_today_log_path is pure
        from scripts.generate_daily_log import generate_daily_log
        generate_daily_log()
        
        today_file = get_today_log_path(self.test_dir)
        self.assertTrue(today_file.exists())
        
        with open(today_file, "r") as f:
            content = f.read()
            self.assertIn("## Learning Topic", content)

    def test_log_append(self):
        from scripts.generate_daily_log import generate_daily_log
        generate_daily_log() # Create
        generate_daily_log() # Append
        
        today_file = get_today_log_path(self.test_dir)
        with open(today_file, "r") as f:
            content = f.read()
            self.assertIn("Update @", content)

class TestWeeklySummary(unittest.TestCase):
    def setUp(self):
        self.log_dir = "test_logs_summary"
        self.summary_dir = "test_summaries"
        for d in [self.log_dir, self.summary_dir]:
            if os.path.exists(d):
                shutil.rmtree(d)
            os.makedirs(d)
        os.environ["LOG_DIR"] = self.log_dir
        os.environ["SUMMARY_DIR"] = self.summary_dir

    def tearDown(self):
        for d in [self.log_dir, self.summary_dir]:
            if os.path.exists(d):
                shutil.rmtree(d)
        for e in ["LOG_DIR", "SUMMARY_DIR"]:
            if e in os.environ:
                del os.environ[e]

    def test_summary_generation(self):
        # Create a dummy log file
        today = datetime.date.today().strftime("%Y-%m-%d")
        log_path = Path(self.log_dir) / f"{today}.md"
        log_path.write_text("## Learning Topic\n- Testing Summary\n## Code Written\n- script.py\n## Problems Faced\n- Bug\n## Solutions\n- Fix\n## Tomorrow Plan\n- Done", encoding="utf-8")
        
        from scripts.weekly_summary import get_weekly_summary
        get_weekly_summary()
        
        summary_file = Path(self.summary_dir) / "weekly-summary.md"
        self.assertTrue(summary_file.exists())
        
        content = summary_file.read_text(encoding="utf-8")
        self.assertIn("Testing Summary", content)
        self.assertIn("Productivity Score", content)

if __name__ == "__main__":
    unittest.main()
