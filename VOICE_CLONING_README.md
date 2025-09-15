# MiniMax Voice Cloning Setup

This directory contains working voice cloning functionality using the MiniMax API, based on your successful local implementation.

## 📋 Quick Start

### 1. Set Environment Variables
```bash
export API_KEY="your_minimax_api_key"
export GROUP_ID="your_group_id"  # Required for voice cloning
```

### 2. Test Voice Cloning
```bash
# Run the complete test suite
python test_voice_cloning_complete.py

# Or test the full workflow manually
python minimax_voice_clone.py test my-voice-sample.wav MyTestVoice123
```

### 3. Use Individual Commands
```bash
# Upload audio file
python minimax_voice_clone.py upload my-voice-sample.wav

# Clone voice (using file_id from upload)
python minimax_voice_clone.py clone "file_id_here" "MyVoiceID123"

# Generate speech with cloned voice
python minimax_voice_clone.py generate-speech "MyVoiceID123" "Hello world!"
```

## 📁 Files

- **`minimax_voice_clone.py`** - Main voice cloning script (matches your working local version)
- **`test_voice_cloning_complete.py`** - Comprehensive test suite
- **`my-voice-sample.wav`** - Your voice sample for cloning
- **`.env.example`** - Template for environment variables

## 🔧 Troubleshooting

### Common Issues

1. **"Missing API key"**
   - Set `API_KEY` environment variable
   - Alternative: Use `MINIMAX_API_KEY`

2. **"Voice cloning failed"**
   - Ensure `GROUP_ID` is set (required for voice cloning)
   - Check that your MiniMax account has voice cloning permissions
   - Verify audio file format (mp3, wav, m4a supported)

3. **"File upload failed"**
   - Check file exists: `ls -la my-voice-sample.wav`
   - Verify file size (should be < 50MB typically)
   - Ensure internet connectivity

### API Response Debugging

The scripts include detailed logging. Look for:
- ✅ Success indicators
- ❌ Error messages with response details
- 📤 Upload progress
- 🎭 Voice cloning status

## 🎯 Integration with Video Generation

Once voice cloning works, you can integrate it into your video generation workflow:

1. Clone your voice once: `python minimax_voice_clone.py clone file_id MyLectureVoice`
2. Use the cloned voice ID in your video generation scripts
3. Replace the default voice ID with your cloned voice ID

## 📊 Expected Results

When working correctly:
- File upload returns a `file_id`
- Voice cloning creates a custom `voice_id`
- Speech generation produces audio files with your voice
- Test files are created in the current directory

## 🚀 Next Steps

1. Run `python test_voice_cloning_complete.py` to verify everything works
2. If tests pass, integrate the cloned voice into your video workflow
3. If tests fail, review the error messages and check your API credentials