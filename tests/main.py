# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

# Create FastAPI app with metadata
app = FastAPI(
    title="Improvise Python App - Token & Text Checksum API",
    description="API to generate tokens and compute checksums for text",
    version="1.0.0"
)

# ------------------ Pydantic model ------------------
class TextPayload(BaseModel):
    text: str


# ------------------ Existing token endpoint ------------------
@app.get("/token")
def generate_token():
    """
    Return a simple demo token (not secure).
    Replace with real logic if needed.
    """
    demo_token = hashlib.sha256(b"demo-secret").hexdigest()
    return {"token": demo_token}


# ------------------ New endpoint: /generate ------------------
@app.post("/generate")
def generate(payload: TextPayload):
    """
    Accepts JSON body with `text` and returns its SHA-256 checksum.
    Example input:
        { "text": "hello world" }

    Example output:
        {
            "welcome": "Welcome, Jeevanandan R.!",
            "original_text": "hello world",
            "checksum_sha256": "<hash>"
        }
    """
    try:
        text_bytes = payload.text.encode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid text: {e}")

    checksum = hashlib.sha256(text_bytes).hexdigest()

    # Customized welcome message
    welcome_msg = "Welcome, Jeevanandan R.!"

    return {
        "welcome": welcome_msg,
        "original_text": payload.text,
        "checksum_sha256": checksum,
    }


# ------------------ Health endpoint ------------------
@app.get("/health")
def health_check():
    """Simple healthcheck endpoint"""
    return {"status": "ok"}


# ------------------ Run with Uvicorn ------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
