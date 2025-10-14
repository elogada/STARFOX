#!/user/bin/python3
import os
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
DB_PATH = "./chromadb_data"
DOCS_PATH = "./docs"
os.makedirs(DB_PATH, exist_ok=True)
client = PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("astral_cortex")

embedder = SentenceTransformer("all-MiniLM-L6-v2")
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def load_docs(path=DOCS_PATH):
    texts = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(os.path.join(path, file), encoding="utf-8") as f:
                texts.append(f.read())
    return texts

docs = load_docs()
chunks = []
for doc in docs:
    chunks.extend(chunk_text(doc))

# 2️⃣ embed
embeddings = embedder.encode(chunks, show_progress_bar=True)

# 3️⃣ store
collection.add(
    documents=chunks,
    embeddings=embeddings,
    metadatas=[{"source": f"chunk_{i}"} for i in range(len(chunks))],
    ids=[f"id_{i}" for i in range(len(chunks))]
)

print(f"✅ Stored {len(chunks)} chunks in the astral cortex.")
