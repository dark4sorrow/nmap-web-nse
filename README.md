# Nmap Web NSE Orchestrator

A Python-based utility for orchestrating Nmap Scripting Engine (NSE) scans via a web interface or secondary service. This tool is a core component of the **NIC Operations Portal**.

## 🚀 Features
- Automated Nmap discovery and vulnerability scanning.
- Designed for integration with the GalacticBacon cyberdeck.
- Lightweight Python implementation using Nmap Scripting Engine.

## 🛠 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dark4sorrow/nmap-web-nse.git
   cd nmap-web-nse
   ```

2. **Rebuild the Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 🖥 Usage
Run the tool directly using the virtual environment:
```bash
./venv/bin/python nmap_tool.py
```

## 🔒 Security Notice
This tool is intended for internal network auditing and authorized security testing only.
