# app.py (FastAPI)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/posts')
def get_posts():
    # Simulated data
    posts = [
        {'id': 1, 'title': 'Post 1'},
        {'id': 2, 'title': 'Post 2'},
        {'id': 3, 'title': 'Post 3'},
    ]
    return posts
