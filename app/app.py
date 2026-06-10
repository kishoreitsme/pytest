from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "hi this is from python code"

if __name__ == "__main__":
    # IMPORTANT: host must be 0.0.0.0 for Docker
    app.run(host="0.0.0.0", port=5000)