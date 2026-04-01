# ITSIT — IT Support & Infrastructure Toolkit

A lightweight command-line toolkit that automates common IT support and infrastructure tasks, built with Python and designed to work on Windows, macOS, and Linux.

---

## 🧩 Problem Statement

IT support engineers often perform repetitive tasks such as checking system health, monitoring website uptime, and analyzing logs. These tasks are usually done using multiple tools or manual commands which can be time-consuming and inefficient.

## ✅ Solution

ITSIT provides a centralized command-line toolkit that automates common infrastructure support tasks such as system monitoring, website health checks, and log analysis — all from a single and user-friendly interface.

## 🔥 Real-World Use Case

This tool simulates real-world tasks performed by **Application and Cloud Support Engineers**, such as:

- Monitoring system performance to detect resource bottlenecks
- Checking service availability and response times
- Analyzing log files to detect errors and potential issues before they escalate

---

## 📋 Features

| Feature | Description |
|---|---|
| ✅ Website Uptime Check | Checks if a website is up and measures its response time |
| ✅ System Health Check | Displays CPU, memory, and disk usage with status indicators |
| ✅ Log Analyzer | Scans a log file and summarizes errors, warnings, and info entries |

---

## 🖥️ Requirements

- Python 3.7 or higher
- The following Python libraries:

```
requests
psutil
colorama
```

Install all dependencies with:

```bash
pip install requests psutil colorama
```

---

## 🚀 How to Run

### Option 1 — Run as a Python script

```bash
python itsit.py
```

### Option 2 — Run as a standalone executable (no Python needed)

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --onefile itsit.py
```

3. Move the generated `.exe` (found inside the `dist/` folder) to your preferred location.

4. Place your `logs` folder **in the same directory as the `.exe`**:

```
📁 Your Folder/
├── ITSIT.exe
└── 📁 logs/
    └── sample.log
```

5. Run the executable by double-clicking it or via terminal.

---

## 📖 How to Use

When you run the program, you will see this menu:

```
                    ITSIT                     
         IT Support & Infrastructure Toolkit         
--------------------------------------------------
[1] Check Website Uptime
[2] Check System Health
[3] Analyze Logs
[4] Exit
```

### [1] Check Website Uptime

Enter a website URL to check if it is online and how fast it responds.

```
Enter a website url: google.com

Website Status:
Status Code:  200
Response Time:  0.341 seconds
✔  Status: HEALTHY
```

> 💡 The tool automatically adds `https://` if you don't include it.

| Response Time | Status |
|---|---|
| Under 1.5 seconds | ✅ HEALTHY |
| 1.5 – 3 seconds | ⚠️ WARNING (Slow response) |
| Over 3 seconds | ❌ CRITICAL (Very slow response) |
| Site unreachable | ❌ CRITICAL (Website Down) |

---

### [2] Check System Health

Displays your system name, OS, and current resource usage.

```
System Info:
System Name : USER-PC
OS          : Windows
OS Version  : 10.0.22621

System Health:
CPU Usage   : 12.5%
Memory Usage: 67.0%
Disk Usage  : 45.3%
✔  Overall Status: HEALTHY
```

| Threshold | Status |
|---|---|
| CPU/Memory/Disk all within safe range | ✅ HEALTHY |
| CPU > 80%, Memory > 88%, or Disk > 85% | ⚠️ WARNING |
| CPU > 90%, Memory > 90%, or Disk > 90% | ❌ CRITICAL |

---

### [3] Analyze Logs

Enter a log file name or its full path. The tool will search for it automatically.

```
Enter log file name or full path: sample.log
✔  Found: C:\MyFolder\logs\sample.log

Log Summary:
ERROR: 2
WARNING: 1
INFO: 5
Error Rate : 25.00%
Warning Rate: 12.50%
⚠  Status: WARNING
```

**How the tool finds your log file:**

1. Searches the same folder as the executable and all its subfolders (including a `logs/` subfolder)
2. If not found, shows you exactly where it looked and suggests entering the full path

**You can also enter a full path directly:**

- Windows: `C:\Users\yourname\logs\logfile`
- macOS/Linux: `/home/yourname/logs/logfile`

| Error Rate | Status |
|---|---|
| Error rate below 10% | ✅ HEALTHY |
| Error rate 10–30% or Warning rate above 30% | ⚠️ WARNING |
| Error rate above 30% | ❌ CRITICAL |

---

## 🗂️ Project Structure

```
📁 ITSIT/
├── itsit.py          ← Main application
├── requirements.txt  ← Python dependencies
├── README.md         ← You are here
└── 📁 logs/          ← Place your log files here
    └── sample.log
```

---

## 🌐 Cross-Platform Compatibility

ITSIT is designed to work consistently across all major operating systems:

| Feature | Windows | macOS | Linux |
|---|---|---|---|
| Website Check | ✅ | ✅ | ✅ |
| System Health | ✅ | ✅ | ✅ |
| Log Analyzer | ✅ | ✅ | ✅ |
| Executable (.exe / binary) | ✅ | ✅ | ✅ |

---

## 👨‍💻 Author

**John Martin.**  
Associate Software Engineer - Application & Cloud Support  
Built as a personal project to simulate real-world IT support workflows.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
