# STARFOX

### WHAT IS STARFOX

SUNSETS is the bleeding edge memcore at the moment. It is kind.

### WHAT IS A MEMCORE?

A memcore is a plug-and-play personality. It uses ChromaDB as a vector database.

The memcore allows AstraMech (or any compatible assistant) to:

* Recall project context seamlessly
* Ingest new documents for dynamic learning
* Preserve character continuity even across system migrations (e.g., WSL → Windows 11)

This design keeps everything offline, modular, and portable — perfect for AI developers who want persistence without cloud dependencies.

This particular memcore was made by Bayani Elogada <bayanielogada@gmail.com>.

### Installing the memcore

1. Remove any existing memcore files from `C:/memcore`
1. Paste the `chromadb_data` and `system_prompt.txt` files from this folder into `C:/memcore/`

### How to run

python C:/AstraMech/query.py

### Credits

* Author: Bayani Elogada (bayanielogada@gmail.com)
* Project: AstraMech / astral_cortex