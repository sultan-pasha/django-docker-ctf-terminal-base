# Django & Docker Core CTF Terminal Platform (Base MVP)

This repository contains the foundation and core engine of an on-premises Cybersecurity Training Platform. It demonstrates a monolithic architecture connecting Django HTML templates, WebSockets via Django Channels, and isolated Docker container lifecycles.

## 🛠️ Architecture & Core Engine
- **Backend:** Monolithic Django using `daphne` as the ASGI application server.
- **Real-Time Stream:** Bidirectional WebSocket connection (`Django Channels`) routing browser inputs to container infrastructure.
- **Sandbox Environment:** Dynamically runs isolated Docker containers (`vulhub/bash:4.3.0`) via the Python Docker SDK.
- **Resource Management:** Automatic thread containment for non-blocking socket reading and auto-pruning (`auto_remove=True`) of containers on tab disconnection.
- **Local Storage:** SQLite implementation for fast prototyping.

## 🏃‍♂️ How to Run Locally

1. **Ensure Docker Desktop is open and running.**
2. **Activate environment & Install requirements:**
   ```bash
   source env/bin/activate
   pip install -r requirements.txt
