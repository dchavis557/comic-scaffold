# 🎨 Comic Project Creator (CLI)

A lightweight Python CLI tool for generating standardized comic project folder structures — built for colorists, artists, and anyone who wants their workflow organized from day one.

---

## 🚀 Features

- 📁 Creates standardized project folders automatically:
  - `Inks`, `Flats`, `Colors`, and a shared `Docs` folder
- 🔢 Supports both **single-issue** and **multi-issue series**
- 🧾 Optional `metadata.json` per project (writer, line artist, publisher)
- 🔧 Reads a JSON config for a default root path — set it once, forget it
- 🐧 Built for Linux, works anywhere Python runs

---

## 💻 Usage

```bash
python project-creator.py
```

The tool will walk you through a few prompts:

```
🎨 Comic Project Creator

🗂️ Root folder where project should be created [/home/username/comics]:
📁 Project title: SuperDude
📘 Is this a series? [Y/n]: y
🔢 Start issue number [default 1]: 1
🔢 End issue number [must be ≥ 1]: 3

Would you like to create a metadata.json file? (y/n): y
Writers: Jane Smith
Line Artists: John Doe
Publisher: Indie Press
```

---

## 📁 Folder Output Example

For a project named `SuperDude` (Issues 1–3):

```
SuperDude/
├── Issue 01/
│   ├── Inks/
│   ├── Flats/
│   └── Colors/
├── Issue 02/
│   ├── Inks/
│   ├── Flats/
│   └── Colors/
├── Issue 03/
│   ├── Inks/
│   ├── Flats/
│   └── Colors/
└── Docs/
```

For a one-shot, `Inks`, `Flats`, and `Colors` sit directly in the project root.

---

## ⚙️ Config (Optional)

Place a `project-config.json` file at:

```
/home/username/project-creator/project-config.json
```

With contents:

```json
{
  "default_root_path": "/home/username/comics"
}
```

This sets your default root folder so you don't have to type it every time.

---

## 🧾 License

MIT License © 2025 Darrin Chavis  
Use freely, modify to suit your workflow.

---

## 🙌 Acknowledgments

Built to solve a real problem in comic production.  
Designed by a colorist, for creators.
