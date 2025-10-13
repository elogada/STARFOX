# STARFOX

### WHAT IS STARFOX

STARFOX is the bleeding edge memcore at the moment. It is kind.

### WHAT IS A MEMCORE?

A memcore is a plug-and-play personality. It uses ChromaDB as a vector database. It also has a system prompt and a personality-specific voice.

The memcore allows AstraMech (or any compatible assistant) to:

* Have a different personality as per user demands
* Swap out subject specialization
* Preserve robot souls even across system migrations (e.g., WSL → Windows 11)
* ...And manage it all with a simple desktop environment

This design keeps everything offline, modular, and portable, with equipment that you can buy from a typical commercial computer store.

This particular memcore was made by Bayani Elogada <bayanielogada@gmail.com>.

### Installing the memcore

1. Remove any existing memcore files from `C:/memcore`
1. Paste the files in this repository into the `C:/memcore` folder.

Historical context is in the pipeline.

###  How to run

* Make sure LM Studio API Server is running with at least LFM2-1.2B, using the identifier `astral_cortex` .

```
cd c:/astramech/ && python C:/astramech/query.py
```

### Credits

* Author: Bayani Elogada (bayanielogada@gmail.com)
* Project: AstraMech / astral_cortex