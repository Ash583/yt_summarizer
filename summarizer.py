from youtube_transcript_api import YouTubeTranscriptApi
import openai

openai.api_key = "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"

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def get_transcript(video_id):
    text = ""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    for i in transcript:
        text += i["text"] + " "
    return text

def get_summary(url):
    video_id = get_video_id(url)
    if not video_id:
        return "Invalid URL"
    text = get_transcript(video_id)
    prompt = "Summarize this video: " + text[:3000]
    resp = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return resp.choices[0].text.strip()
