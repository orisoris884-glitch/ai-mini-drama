import json
import random
from datetime import datetime

GENRES = [
    "relationship betrayal",
    "secret identity",
    "revenge",
    "rich vs poor",
    "family secret",
    "unexpected friendship",
    "jealousy",
    "mystery",
    "second chance",
    "hidden inheritance"
]

CHARACTERS = [
    ("Alex", "22-year-old man"),
    ("Mia", "21-year-old woman"),
    ("Daniel", "24-year-old man"),
    ("Emma", "22-year-old woman")
]

genre = random.choice(GENRES)
timestamp = datetime.now().strftime("%Y-%m-%d")

story = {
    "date": timestamp,
    "genre": genre,
    "title": f"Episode: {genre.title()}",
    "duration": "45-60 seconds",

    "style": {
        "format": "vertical 9:16",
        "cinematic": True,
        "realistic_characters": True,
        "fast_pacing": True,
        "dramatic_lighting": True,
        "social_media_style": True
    },

    "characters": [
        {
            "name": CHARACTERS[0][0],
            "description": CHARACTERS[0][1]
        },
        {
            "name": CHARACTERS[1][0],
            "description": CHARACTERS[1][1]
        },
        {
            "name": CHARACTERS[2][0],
            "description": CHARACTERS[2][1]
        }
    ],

    "scenes": [
        {
            "number": 1,
            "type": "HOOK",
            "duration": 5,
            "description":
                "Start with an extremely shocking moment that immediately "
                "makes the viewer want to know what happened.",
            "dialogue": ""
        },
        {
            "number": 2,
            "type": "SETUP",
            "duration": 7,
            "description":
                "Introduce the main characters and establish the problem.",
            "dialogue": ""
        },
        {
            "number": 3,
            "type": "CONFLICT",
            "duration": 8,
            "description":
                "The main character discovers something suspicious.",
            "dialogue": ""
        },
        {
            "number": 4,
            "type": "ESCALATION",
            "duration": 8,
            "description":
                "The situation becomes emotionally intense.",
            "dialogue": ""
        },
        {
            "number": 5,
            "type": "REVEAL",
            "duration": 8,
            "description":
                "Reveal information that completely changes the story.",
            "dialogue": ""
        },
        {
            "number": 6,
            "type": "TWIST",
            "duration": 8,
            "description":
                "Introduce a second unexpected twist.",
            "dialogue": ""
        },
        {
            "number": 7,
            "type": "CLIFFHANGER",
            "duration": 6,
            "description":
                "End immediately before the biggest answer is revealed.",
            "dialogue": ""
        }
    ],

    "requirements": [
        "No filler",
        "Strong hook in first 2 seconds",
        "Every scene advances the story",
        "Natural dialogue",
        "Emotional reactions",
        "Major twist near the end",
        "End with a cliffhanger",
        "Suitable for TikTok",
        "Do not copy existing stories"
    ]
}

with open("story.json", "w", encoding="utf-8") as f:
    json.dump(story, f, indent=2, ensure_ascii=False)

print("DRAMA GENERATED")
print(json.dumps(story, indent=2, ensure_ascii=False))
