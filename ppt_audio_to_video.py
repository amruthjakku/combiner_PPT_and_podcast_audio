import os
import subprocess
import glob
import math

PPT_FILE = "another_RAG_PPT.ppt"
PDF_FILE = "another_RAG_PPT.pdf"
AUDIO_FILE = "last_aud.wav"
SLIDES_DIR = "slides"
SLIDE_PREFIX = "slide"
VIDEO_FILE = "output.mp4"

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def ppt_to_pdf():
    if not os.path.exists(PDF_FILE):
        run(f'libreoffice --headless --convert-to pdf "{PPT_FILE}"')

def pdf_to_images():
    os.makedirs(SLIDES_DIR, exist_ok=True)
    run(f'pdftoppm "{PDF_FILE}" {SLIDES_DIR}/{SLIDE_PREFIX} -png')

def get_audio_duration():
    import wave
    with wave.open(AUDIO_FILE, 'rb') as w:
        frames = w.getnframes()
        rate = w.getframerate()
        return frames / float(rate)

def make_video():
    images = sorted(glob.glob(f"{SLIDES_DIR}/{SLIDE_PREFIX}-*.png"))
    n_slides = len(images)
    duration = get_audio_duration()
    slide_time = duration / n_slides

    # ffmpeg expects slide-1.png, slide-2.png, ...
    run(
        f'ffmpeg -y -framerate 1/{slide_time} -i {SLIDES_DIR}/{SLIDE_PREFIX}-%d.png '
        f'-i "{AUDIO_FILE}" -c:v libx264 -r 30 -pix_fmt yuv420p '
        f'-c:a aac -b:a 192k -shortest -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" "{VIDEO_FILE}"'
    )

if __name__ == "__main__":
    ppt_to_pdf()
    pdf_to_images()
    make_video()
    print(f"Done! Video saved as {VIDEO_FILE}")
