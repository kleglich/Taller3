import pytube
import whisper

youtubevideoId ="https://www.youtube.com/watch?v=C9gP_b8yuOw"
model = whisper.load_model("small")

youtubeVideo = pytube.Youtube(youtubevideoId)
audio = youtubeVideo.streams.get_audio_only()
audio.download(fillname="tmp.mp4")

result = model.transcribe("tmp.mp4")

print(result["text"])
