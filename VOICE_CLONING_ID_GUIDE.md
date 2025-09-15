# MiniMax Voice Cloning - ID Management Guide

## 🆔 Understanding MiniMax Voice Cloning IDs

When working with MiniMax voice cloning, several IDs are involved in the process. This guide explains what each ID is for and how to use them.

## 📋 The Voice Cloning Process & IDs

### 1. File Upload
```bash
python minimax_voice_clone.py upload my-voice-sample.wav
```
**Returns:** `file_id` (e.g., "311103389282466")
- **What it is:** Unique identifier for your uploaded audio file
- **Used for:** Voice cloning step
- **Save this:** You need it for the next step

### 2. Voice Cloning
```bash
python minimax_voice_clone.py clone "311103389282466" "MyVoice123"
```
**Input:** 
- `file_id` (from step 1)
- `voice_id` (your chosen name for the voice)

**Returns (potentially):**
- ✅ `voice_id` - Your original voice ID
- ✅ `returned_voice_id` - MiniMax's actual voice ID (if different)
- ✅ `returned_file_id` - Processed file ID (if different)
- ✅ `clone_id` - Unique clone identifier (if provided)

### 3. Speech Generation
```bash
python minimax_voice_clone.py generate-speech "MyVoice123" "Hello world"
```
**Uses:** The voice ID from step 2 (either your original or returned ID)

## 🔍 Updated Script Features

The updated `minimax_voice_clone.py` now:

### ✅ Captures All Response Data
```python
# Extracts and displays:
- voice_id (your requested ID)
- returned_voice_id (MiniMax's actual ID) 
- returned_file_id (processed file ID)
- clone_id (unique clone identifier)
```

### ✅ Smart ID Management
- Uses returned IDs when available
- Falls back to original IDs if needed
- Shows which ID is being used for speech generation

### ✅ Detailed Logging
```bash
📋 VOICE CLONING RESULTS:
   🎭 Requested Voice ID: MyVoice123
   📄 Original File ID: 311103389282466
   ✅ Returned Voice ID: MyVoice123_processed
   ✅ Clone ID: clone_abc123
```

## 🧪 Testing the Updated System

### Quick Test
```bash
python test_voice_cloning_complete.py
```

### Manual Test
```bash
# 1. Upload
python minimax_voice_clone.py upload my-voice-sample.wav

# 2. Clone (use the file_id from step 1)
python minimax_voice_clone.py clone "YOUR_FILE_ID" "MyTestVoice123"

# 3. Generate speech (use voice_id from step 2 output)
python minimax_voice_clone.py generate-speech "MyTestVoice123" "This is a test"
```

## ❓ Common Questions

### Q: Which voice ID should I use for speech generation?
**A:** Use the `returned_voice_id` if provided, otherwise use your original `voice_id`. The updated script handles this automatically.

### Q: Do I need both file_id and voice_id?
**A:** 
- **file_id**: Needed only for the cloning step
- **voice_id**: Needed for speech generation
- **clone_id**: Additional identifier that MiniMax might provide

### Q: What if the returned IDs are different from what I specified?
**A:** This is normal! MiniMax might process your voice ID or assign additional identifiers. The script now shows you exactly which IDs to use.

## 🔧 Troubleshooting

### Issue: "Voice not found" during speech generation
**Solution:** 
1. Check the voice cloning output for the actual voice ID to use
2. Try both your original voice_id and any returned_voice_id
3. Wait a few moments after cloning before generating speech

### Issue: Cloning succeeds but speech generation fails
**Debug steps:**
1. Run `python minimax_voice_clone.py list` to see available voices
2. Verify you're using the correct voice ID from cloning output
3. Check that GROUP_ID is set correctly

## 💡 Key Improvements

1. **Full Response Capture**: Now captures all IDs returned by MiniMax
2. **Smart Fallbacks**: Uses the best available ID for each operation
3. **Clear Documentation**: Shows exactly which IDs to save and use
4. **Error Recovery**: Better handling when IDs don't match expectations
5. **Testing Integration**: Test script validates the complete ID workflow

## 🎯 Next Steps

1. Test the updated script with your voice sample
2. Note which IDs are returned in your specific case
3. Use the correct voice ID for your video generation workflow
4. Save the working voice ID for future use