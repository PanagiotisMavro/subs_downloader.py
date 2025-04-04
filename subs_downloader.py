import argparse
import yt_dlp

def download_all_english_subtitles(url):
    ydl_opts = {
        'skip_download': True,              # Don't download video/audio
        'writesubtitles': True,             # Download subtitles
        'writeautomaticsub': True,          # Include auto-generated if no manual
        'subtitleslangs': ['en'],           # English only
        'subtitlesformat': 'srt',           # Save as .srt
        'outtmpl': '%(title)s.%(ext)s',     # Output file format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download all English subtitles from YouTube")
    parser.add_argument("-u", "--url", required=True, help="YouTube video URL")
    args = parser.parse_args()

    download_all_english_subtitles(args.url)
