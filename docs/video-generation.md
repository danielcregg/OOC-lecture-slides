# AI-Generated Lecture Videos

This repository includes an advanced GitHub Action workflow that automatically generates narrated videos from lecture PDFs using AI tools.

## 🎥 How It Works

### 1. **PDF Analysis**
- Sends entire PDF to Google Gemini AI
- Gemini analyzes each slide and generates educational narration scripts
- Scripts are written in academic tone, perfect for university lectures

### 2. **Voice Synthesis**
- Uses MiniMax TTS API with voice cloning
- Clones instructor voice from `my-voice-sample.wav`
- Generates natural-sounding narration for each slide

### 3. **Video Assembly**
- Extracts high-quality images from PDF slides
- Combines slides with AI-generated audio
- Creates professional 1080p MP4 videos using FFmpeg

### 4. **Smart Caching**
- Only regenerates videos when PDFs are updated
- Tracks file changes to avoid unnecessary processing
- Maintains cache for efficient workflows

## 🚀 Usage

### Manual Trigger
1. Go to **Actions** tab in GitHub
2. Select **"Generate Lecture Videos"** workflow
3. Click **"Run workflow"**
4. Options:
   - **Lecture Filter**: Generate videos for specific lectures (e.g., "lecture1,lecture2" or "all")
   - **Force Regenerate**: Force regenerate all videos (ignore cache)

### Example Filters
- `all` - Process all lectures
- `lecture1` - Process only lecture1
- `lecture1,lecture3` - Process lecture1 and lecture3

## ⚙️ Setup Requirements

### GitHub Secrets
Add these secrets in your repository settings:

```
GOOGLE_AI_STUDIO_API_KEY=your_gemini_api_key
MINIMAX_API_KEY=your_minimax_api_key
```

### Voice Sample
- Place your voice sample as `my-voice-sample.wav` in the root directory
- Should be clear, high-quality recording of your voice
- Recommended: 10-30 seconds of natural speech

## 📁 Output Structure

```
videos/
├── README.md                                    # Auto-generated video index
├── lecture1-course-introduction.mp4            # Generated video files
├── lecture2-ai-assisted-programming-intro.mp4
└── ...
```

## 🔧 Technical Details

### Video Specifications
- **Resolution**: 1920x1080 (Full HD)
- **Format**: MP4 (H.264 video, AAC audio)
- **Quality**: CRF 23 (high quality, reasonable file size)
- **Audio**: 22.05kHz WAV, converted to 128k AAC

### Processing Pipeline
1. **PDF → Images**: Extract slides at 300 DPI PNG
2. **PDF → Script**: Gemini generates academic narration
3. **Script → Audio**: MiniMax TTS with voice cloning
4. **Images + Audio → Video**: FFmpeg assembly with timing

### Caching System
- Tracks PDF file hashes to detect changes
- Stores generation metadata in `video_generation_cache.json`
- Skips unchanged lectures automatically

## 🎯 Gemini Prompt

The workflow uses this prompt for script generation:

> Create a short educational narration script for each slide in this PDF lecture presentation.
> 
> Requirements:
> - Use an academic tone suitable for university students
> - Keep each slide narration concise but informative (approximately 15-30 seconds when spoken)
> - Include natural pauses between slides
> - Number each slide script clearly (e.g., "Slide 1:", "Slide 2:", etc.)
> - Focus on explaining key concepts and connecting ideas
> - Avoid reading bullet points verbatim - instead explain and elaborate

## 🛠 Troubleshooting

### Common Issues

**1. API Limits**
- Gemini: Rate limited, workflow includes delays
- MiniMax: Check your API quota and limits

**2. Large PDFs**
- Gemini has file size limits (~20MB for PDFs)
- Consider splitting very large presentations

**3. Audio Quality**
- Ensure voice sample is high quality
- MiniMax works best with clear, noise-free samples

**4. Video Generation Fails**
- Check FFmpeg logs in workflow output
- Ensure all slides have corresponding audio

### Debugging
- Check workflow logs in GitHub Actions
- Enable debug mode by setting workflow inputs
- Test individual components locally

## 🔮 Future Enhancements

Potential improvements:
- Custom video templates and branding
- Multiple voice options
- Subtitle generation
- Interactive video elements
- YouTube auto-upload
- Video analytics and engagement tracking

## 📊 Workflow Monitoring

The workflow provides detailed logging:
- PDF processing status
- Gemini script generation results
- Audio synthesis progress
- Video assembly completion
- Cache hit/miss statistics

## 🤝 Contributing

To improve the video generation workflow:
1. Test with different PDF formats
2. Optimize Gemini prompts for better scripts
3. Enhance video quality settings
4. Add error recovery mechanisms

---

*This AI-powered video generation system transforms static slides into engaging educational content automatically.*