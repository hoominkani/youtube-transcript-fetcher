from flask import Flask, request, render_template, send_file
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = video_url.split('v=')[1]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja'])
            # 字幕の最初の部分を表示するために最初の5つのエントリーを取得
            transcript_preview = transcript[:5]
            # 字幕をテキストファイルに保存
            with open('transcript.txt', 'w', encoding='utf-8') as f:
                for entry in transcript:
                    f.write(entry['text'] + '\n')
            return render_template('index.html', transcript_preview=transcript_preview, download_link=True)
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

@app.route('/download')
def download_file():
    path = "transcript.txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)