# 🔄 ACMC (Addon-Collection Missmatch Checker)

This tool compares your local `collection.lua` file with a live Steam Workshop Collection to ensure all addon IDs are properly synced. Avoid missing content and server errors caused by outdated Lua files.

---

## ✨ Features

- ✅ Parses your `collection.lua` file for `resource.AddWorkshop(...)` entries
- ✅ Fetches the actual Workshop Collection via Steam Web API
- ✅ Compares both lists and shows:
  - 🚫 Addons in the Workshop collection but **missing in Lua**
  - ⚠️ Addons in Lua but **not in the collection**
- ✅ CLI interface with helpful prompts
- 🔜 Planned: Auto-update or patch `collection.lua`

---

## 🖥 Requirements

- **Python 3.6+**
- Dependencies: `requests`

Install requirements:

```bash
pip install requests
