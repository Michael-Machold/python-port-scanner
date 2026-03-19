#### 🔍 Advanced Python Port Scanner

#### 

#### A multithreaded network reconnaissance tool built in Python for scanning open ports, identifying services, and performing basic banner grabbing. Designed to simulate real-world port scanning techniques in a controlled lab environment.

#### 

#### 🚀 Features

#### 

#### 🔎 Scan custom port ranges

#### 

#### ⚡ Multithreaded scanning for improved performance

#### 

#### 🌐 Target IP or domain support

#### 

#### 🧠 Service detection for common ports

#### 

#### 📡 Banner grabbing (including HTTP response detection)

#### 

#### 🎨 Color-coded terminal output using Colorama

#### 

#### 📝 JSON report generation

#### 

#### ⏱️ Scan timing metrics

#### 

#### 🛠️ Technologies Used

#### 

#### Python 3

#### 

#### socket (network connections)

#### 

#### argparse (CLI argument parsing)

#### 

#### concurrent.futures (multithreading)

#### 

#### json (report generation)

#### 

#### colorama (terminal styling)

#### 

#### 📦 Installation

#### 

#### Clone the repository:

#### 

#### git clone https://github.com/yourusername/python-port-scanner.git

#### cd python-port-scanner

#### 

#### Install dependencies:

#### 

#### pip3 install colorama

#### ▶️ Usage

#### 

#### Basic scan:

#### 

#### python3 scanner.py scanme.nmap.org

#### 

#### Custom port range:

#### 

#### python3 scanner.py scanme.nmap.org -p 20-100

#### 

#### Full example:

#### 

#### python3 scanner.py scanme.nmap.org -p 20-100 -t 100 -o results.json

#### 🖥️ Example Output

#### Target: scanme.nmap.org (45.33.32.156)

#### Scanning ports 20-100 with 100 threads

#### 

#### \[OPEN] Port 22 (SSH)

#### \[OPEN] Port 80 (HTTP)

#### 

#### Scan complete.

#### Time taken: 0:00:02.13

#### Results saved to results.json

#### 📄 Sample JSON Output

#### \[

#### &#x20;   {

#### &#x20;       "port": 22,

#### &#x20;       "service": "SSH",

#### &#x20;       "banner": "SSH-2.0-OpenSSH..."

#### &#x20;   },

#### &#x20;   {

#### &#x20;       "port": 80,

#### &#x20;       "service": "HTTP",

#### &#x20;       "banner": "HTTP/1.1 200 OK..."

#### &#x20;   }

#### ]

#### 🧪 Testing Environment

#### 

#### This tool was tested in a controlled lab environment using:

#### 

#### Kali Linux (attacker machine)

#### 

#### Metasploitable (vulnerable target VM)

#### 

#### scanme.nmap.org (authorized public test host)

#### 

#### ⚠️ Disclaimer

#### 

#### This tool is intended for educational purposes only.

#### 

#### All testing was conducted on:

#### 

#### Authorized systems

#### 

#### Local lab environments

#### 

#### Publicly permitted targets

#### 

#### Do NOT use this tool on networks or systems without explicit permission.

