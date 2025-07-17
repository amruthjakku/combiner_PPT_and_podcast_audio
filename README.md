# combiner_PPT_and_podcast_audio

## Description
This project combines a PowerPoint presentation (PPT) and a podcast audio file to generate a video. It converts PPT slides to images, synchronizes them with the audio, and produces a final MP4 video.

## Requirements
- Python 3.x
- libreoffice (for PPT to PDF conversion)
- pdftoppm (for PDF to PNG conversion)
- ffmpeg (for video creation)

## Usage
1. Place your PPT file and audio file in the project directory.
2. Update the filenames in `ppt_audio_to_video.py` if needed:
   - `PPT_FILE`: PowerPoint file name
   - `AUDIO_FILE`: Audio file name
3. Run the script:
   ```bash
   python ppt_audio_to_video.py
   ```
4. The output video will be saved as `output.mp4`.

## Workflow
1. Convert PPT to PDF using LibreOffice.
2. Convert PDF to PNG images (one per slide) using pdftoppm.
3. Calculate audio duration and divide it among slides.
4. Use ffmpeg to combine images and audio into a video.

## Output
- The generated video will display each slide for an equal portion of the audio duration, synchronized with the podcast.