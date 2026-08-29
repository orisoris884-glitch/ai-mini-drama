import os
import json
import urllib.request

API_KEY = os.environ["GEMINI_API_KEY"]

prompt = """
Create an original TikTok mini-drama.

Requirements:
- 45–60 seconds
- 7 scenes
- Strong hook in the first 2 seconds
- Realistic human characters
- Emotional relationship/mystery drama
- Natural dialogue
- Every scene must advance the story
- Major twist near the end
- Strong cliffhanger
- End with "PART 2?"
- No fruit, vegetables, talking objects, or children's cartoon style
- Do not copy an existing story

Return ONLY valid JSON in this exact structure:

{
  "title": "short title",
  "characters": [
    {
      "name": "name",
      "description": "appearance and personality"
    }
  ],
  "scenes": [
    {
      "scene": 1,
      "duration": 5,
      "visual": "detailed description of what the camera sees",
      "dialogue": "spoken dialogue",
      "emotion": "emotion"
    }
  ],
  "caption": "TikTok caption",
  "hashtags": ["#story", "#drama", "#fyp"]
}
"""

url = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key=" + API_KEY
)

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

request = urllib.request.Request(
    url,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

text = result["candidates"][0]["content"]["parts"][0]["text"]

# Remove markdown fences if the model adds them
text = text.replace("```json", "").replace("```", "").strip()

story = json.loads(text)

with open("story.json", "w", encoding="utf-8") as f:
    json.dump(story, f, indent=2, ensure_ascii=False)

print("✅ AI DRAMA GENERATED")
print(json.dumps(story, indent=2, ensure_ascii=False))
