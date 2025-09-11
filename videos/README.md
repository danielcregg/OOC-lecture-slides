# AI-Generated Lecture Videos

This directory contains automatically generated videos for the AIAP lecture slides.

## How Videos Are Generated

1. **PDF Processing**: Each lecture PDF is processed by Google Gemini AI
2. **Script Generation**: Gemini creates educational narration scripts for each slide
3. **Voice Synthesis**: MiniMax TTS generates audio using voice cloning
4. **Video Assembly**: FFmpeg combines slides and audio into final videos

## Available Videos

- [lecture1-course-introduction](./lecture1-course-introduction.mp4)
- [lecture2-ai-assisted-programming-intro](./lecture2-ai-assisted-programming-intro.mp4)

## Video Specifications

- **Resolution**: 1920x1080 (Full HD)
- **Format**: MP4 (H.264 video, AAC audio)
- **Frame Rate**: Variable (based on audio duration)
- **Audio**: AI-generated narration with voice cloning

## Regeneration

Videos are automatically regenerated when:
- The source PDF is updated
- Manual regeneration is triggered via GitHub Actions

---

*Videos generated automatically using AI tools*
