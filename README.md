# 📝 Daily Dev Log Automation System

[![GitHub License](https://img.shields.io/github/license/Sanskar/Daily-Dev-Log?style=flat-square&color=blue)](LICENSE)
[![Daily Log Action](https://github.com/Sanskar/Daily-Dev-Log/actions/workflows/auto-daily-log.yml/badge.svg)](https://github.com/Sanskar/Daily-Dev-Log/actions/workflows/auto-daily-log.yml)
[![Weekly Summary Action](https://github.com/Sanskar/Daily-Dev-Log/actions/workflows/weekly-summary.yml/badge.svg)](https://github.com/Sanskar/Daily-Dev-Log/actions/workflows/weekly-summary.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

An automated system designed to streamline a developer's daily logging process, generate weekly productivity summaries, and maintain an active GitHub contribution streak effortlessly.

---

## 🌟 Key Features

- **Automated Daily Logs:** Generates a structured markdown log every day at 18:00 UTC.
- **Intelligent Appending:** Detects existing logs for the day and appends a timestamped update instead of overwriting.
- **Weekly Analytics:** Sunday night summaries extracting learning topics, code entries, and productivity metrics.
- **Standard Library Only:** Zero external dependencies (no `pip install` required for core features).
- **GitHub Integration:** Built-in GitHub Actions for hands-free maintenance.
- **Portable & Extensible:** Custom log and summary directories via environment variables.

---

## 📂 Project Structure

```text
Daily-Dev-Log/
│
├── .github/
│   └── workflows/
│       ├── auto-daily-log.yml    # Daily automation (18:00 UTC)
│       └── weekly-summary.yml    # Weekly summary (Sunday 20:00 UTC)
│
├── logs/                         # Daily markdown logs (YYYY-MM-DD.md)
├── summaries/                    # Weekly generated summaries
├── scripts/
│   ├── generate_daily_log.py     # Core log generation logic
│   └── weekly_summary.py         # Summary extraction logic
│
├── tests/                        # Unit tests for automation scripts
│   └── test_scripts.py
│
├── README.md                     # Documentation
└── requirements.txt              # Standard library declaration
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.9 or higher.
- A GitHub repository to host the logs.

### 2. Local Setup
Clone the repository and run the scripts manually to test:

```bash
# Generate today's log
python scripts/generate_daily_log.py

# Generate weekly summary
python scripts/weekly_summary.py
```

### 3. Running Tests
Ensure everything is working correctly:

```bash
python -m unittest tests/test_scripts.py
```

---

## ⚙️ Configuration

The system supports the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `LOG_DIR` | Path to store daily logs | `logs/` |
| `SUMMARY_DIR` | Path to store summaries | `summaries/` |

---

## 🤖 GitHub Actions Automation

This project is designed to be fully autonomous:
1. **Daily Log:** Triggered automatically every day. It creates a new file or appends to it, ensuring your contribution graph stays active.
2. **Weekly Summary:** Triggered every Sunday. It aggregates the past week's data into a clean report.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 👤 Author

**Sanskar**
- GitHub: [@Sanskar](https://github.com/Sanskar)
- Email: [sanskardhat6@gmail.com](mailto:sanskardhat6@gmail.com)
- LinkedIn: [Sanskar](https://www.linkedin.com/in/sanskar)

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Built with ❤️ by the Daily Dev Log Automation System*
