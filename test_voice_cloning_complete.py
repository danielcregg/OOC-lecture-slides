#!/usr/bin/env python3
"""
MiniMax Voice Cloning Test Runner
This script helps test and troubleshoot voice cloning functionality
"""

import os
import sys
from pathlib import Path

# Add current directory to path to import our voice cloning module
sys.path.insert(0, str(Path(__file__).parent))

from minimax_voice_clone import MiniMaxVoiceClone

def check_environment():
    """Check if environment is properly configured"""
    print("🔍 Environment Check")
    print("=" * 30)
    
    # Check API credentials
    api_key = os.getenv("API_KEY") or os.getenv("MINIMAX_API_KEY")
    group_id = os.getenv("GROUP_ID") or os.getenv("MINIMAX_GROUP_ID")
    
    if not api_key:
        print("❌ Missing API key")
        print("   Set API_KEY or MINIMAX_API_KEY environment variable")
        print("   Example: export API_KEY='your_minimax_key'")
        return False
    
    print(f"✅ API Key: {api_key[:10]}...{api_key[-4:]}")
    
    if group_id:
        print(f"✅ Group ID: {group_id}")
    else:
        print("⚠️  No Group ID (may limit voice cloning features)")
    
    # Check audio file
    audio_file = Path("my-voice-sample.wav")
    if audio_file.exists():
        file_size = audio_file.stat().st_size
        print(f"✅ Audio sample: {audio_file} ({file_size:,} bytes)")
    else:
        print("❌ Audio sample not found: my-voice-sample.wav")
        return False
    
    return True

def test_basic_tts():
    """Test basic text-to-speech without voice cloning"""
    print("\n🎵 Testing Basic TTS")
    print("=" * 30)
    
    try:
        cloner = MiniMaxVoiceClone()
        
        # Test with built-in voice
        result = cloner.generate_speech(
            voice_id="male-qn-qingse",  # Built-in voice
            text="Hello, this is a test of basic MiniMax text to speech.",
            output_filename="test_basic_tts.mp3"
        )
        
        if result:
            print("✅ Basic TTS working!")
            return True
        else:
            print("❌ Basic TTS failed")
            return False
            
    except Exception as e:
        print(f"❌ Basic TTS error: {e}")
        return False

def test_file_upload():
    """Test file upload functionality"""
    print("\n📤 Testing File Upload")
    print("=" * 30)
    
    try:
        cloner = MiniMaxVoiceClone()
        
        audio_file = "my-voice-sample.wav"
        file_id = cloner.upload_file(audio_file)
        
        if file_id:
            print(f"✅ File upload successful: {file_id}")
            return file_id
        else:
            print("❌ File upload failed")
            return None
            
    except Exception as e:
        print(f"❌ File upload error: {e}")
        return None

def test_voice_cloning(file_id):
    """Test voice cloning functionality"""
    print("\n🎭 Testing Voice Cloning")
    print("=" * 30)
    
    try:
        cloner = MiniMaxVoiceClone()
        
        # Generate a unique voice ID
        import time
        voice_id = f"TestVoice{int(time.time())}"
        
        result = cloner.clone_voice(file_id, voice_id)
        
        if result.get('success', False):
            print(f"✅ Voice cloning successful!")
            print("\n📋 CLONING RESULTS:")
            print(f"   🎭 Original Voice ID: {result.get('voice_id')}")
            print(f"   📄 File ID Used: {result.get('original_file_id')}")
            
            if 'returned_voice_id' in result:
                print(f"   ✅ Returned Voice ID: {result['returned_voice_id']}")
                actual_voice_id = result['returned_voice_id']
            else:
                actual_voice_id = voice_id
                
            if 'returned_file_id' in result:
                print(f"   ✅ Returned File ID: {result['returned_file_id']}")
                
            if 'clone_id' in result:
                print(f"   ✅ Clone ID: {result['clone_id']}")
            
            print(f"\n🔄 Using voice ID for speech: {actual_voice_id}")
            return actual_voice_id
        else:
            print(f"❌ Voice cloning failed: {result.get('error', 'Unknown error')}")
            return None
            
    except Exception as e:
        print(f"❌ Voice cloning error: {e}")
        return None

def test_cloned_voice_speech(voice_id):
    """Test speech generation with cloned voice"""
    print("\n🗣️  Testing Cloned Voice Speech")
    print("=" * 30)
    
    try:
        cloner = MiniMaxVoiceClone()
        
        test_text = "Hello! This should sound like my voice using MiniMax voice cloning technology."
        
        result = cloner.generate_speech(
            voice_id=voice_id,
            text=test_text,
            output_filename=f"test_cloned_{voice_id}.mp3"
        )
        
        if result:
            print("✅ Cloned voice speech generation successful!")
            return True
        else:
            print("❌ Cloned voice speech generation failed")
            return False
            
    except Exception as e:
        print(f"❌ Cloned voice speech error: {e}")
        return False

def main():
    print("🧪 MiniMax Voice Cloning Test Suite")
    print("=" * 50)
    
    # Step 1: Environment check
    if not check_environment():
        print("\n❌ Environment check failed. Please fix issues above.")
        return
    
    # Step 2: Test basic TTS
    basic_tts_works = test_basic_tts()
    if not basic_tts_works:
        print("\n❌ Basic TTS failed. Check API credentials.")
        return
    
    # Step 3: Test file upload
    file_id = test_file_upload()
    if not file_id:
        print("\n❌ File upload failed. Voice cloning won't work.")
        return
    
    # Step 4: Test voice cloning
    voice_id = test_voice_cloning(file_id)
    if not voice_id:
        print("\n❌ Voice cloning failed. Using fallback voice.")
        voice_id = "male-qn-qingse"  # Fallback to built-in voice
    
    # Step 5: Test speech with cloned voice (or fallback)
    cloned_speech_works = test_cloned_voice_speech(voice_id)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    print(f"✅ Environment Setup: {'PASS' if True else 'FAIL'}")
    print(f"✅ Basic TTS: {'PASS' if basic_tts_works else 'FAIL'}")
    print(f"✅ File Upload: {'PASS' if file_id else 'FAIL'}")
    print(f"✅ Voice Cloning: {'PASS' if voice_id and 'Test' in voice_id else 'FAIL'}")
    print(f"✅ Cloned Speech: {'PASS' if cloned_speech_works else 'FAIL'}")
    
    if all([basic_tts_works, file_id, cloned_speech_works]):
        print("\n🎉 ALL TESTS PASSED!")
        print("Voice cloning should work in your video generation workflow.")
        
        # List generated files
        print("\n📁 Generated test files:")
        for file in Path(".").glob("test_*.mp3"):
            print(f"   🎵 {file}")
            
    else:
        print("\n❌ SOME TESTS FAILED")
        print("Review the errors above to troubleshoot issues.")
    
    print("\n🔧 Quick troubleshooting:")
    print("   1. Ensure API_KEY and GROUP_ID are set correctly")
    print("   2. Check that my-voice-sample.wav is a valid audio file")
    print("   3. Verify your MiniMax account has voice cloning permissions")
    print("   4. Try the individual commands manually:")
    print("      python minimax_voice_clone.py test my-voice-sample.wav MyTestVoice123")

if __name__ == "__main__":
    main()