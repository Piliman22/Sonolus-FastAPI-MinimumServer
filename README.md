# Sonolus FastAPI – Minimum Server

A **minimal Sonolus server example** built with  
[sonolus-fastapi](https://pypi.org/project/sonolus-fastapi/).

This repository demonstrates the **smallest possible setup**
that supports:

- `server_info`
- `authenticate`

It is intended as a **starting point** for building Sonolus servers
using Python and FastAPI.

---

## ✨ Features

- Minimal Sonolus server implementation
- Supports core Sonolus routes:
  - `/sonolus/info`
  - `/sonolus/authenticate`
- Built on FastAPI
- Handler-based API design
- Easy to extend (items, packs, sessions, etc.)

> ⚠️ This repository is intentionally minimal.  
> Item routes (levels, posts, backgrounds, etc.) are **not included**.

---

## 📦 Requirements

- Python 3.9+
- `sonolus-fastapi`

---

## 📥 Installation

```bash
pip install sonolus-fastapi
```

## 🚀 Usage

```bash
git clone https://github.com/Piliman22/Sonolus-FastAPI-MinimumServer
```

```bash
python main.py
```

Then open:

http://localhost:8010/sonolus/info