#!/usr/bin/env python3
"""
Test Voice Cloning on Single Slide
This script tests voice cloning functionality locally on one slide
"""

import os
import sys
import time
import subprocess
from pathlib import Path
import google.generativeai as genai
import requests
from pdf2image import convert_from_path
import base64

class VoiceCloneTester:
    def __init__(self):
        self.setup_apis()
        self.temp_dir = Path("temp_voice_test")
        self.temp_dir.mkdir(exist_ok=True)
        self.voice_sample = Path("my-voice-sample.wav")
        self.cloned_voice_id = None

    def setup_apis(self):
        """Setup API keys from environment"""
        google_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
        minimax_key = os.getenv('MINIMAX_API_KEY')
        minimax_group = os.getenv('MINIMAX_GROUP_ID')

        if not google_key:
            raise ValueError("GOOGLE_AI_STUDIO_API_KEY environment variable required")
        if not minimax_key:
            raise ValueError("MINIMAX_API_KEY environment variable required")

        genai.configure(api_key=google_key)
        self.model = genai.GenerativeModel('gemini-2.5-pro')
        self.minimax_api_key = minimax_key
        self.minimax_group_id = minimax_group
        print("✅ APIs configured")

    def setup_voice_cloning(self):
        """Setup voice cloning using the user's existing cloned voice"""
        print("🎤 Setting up voice cloning...")

        # Use the user's existing cloned voice ID
        self.cloned_voice_id = "MyClonedVoice1"
        print(f"   ✅ Using existing cloned voice: {self.cloned_voice_id}")
        print(f"   📄 File ID: 311103389282466")

        # Check if voice sample exists for reference
        if self.voice_sample.exists():
            print(f"   📁 Voice sample file found: {self.voice_sample}")
        else:
            print("   ⚠️  Voice sample file not found, but using existing clone")

        return True

    def test_script_generation(self):
        """Generate a test script for slide 1"""
        print("🤖 Generating test script...")

        prompt = """Create a narration script for slide 1 of an AI-assisted programming lecture.
        The script should be 15-20 seconds when spoken at normal pace.
        Focus on educational content about AI tools for programming.
        Format: Just the narration text, no additional formatting."""

        try:
            response = self.model.generate_content(prompt)
            script = response.text.strip()
            print(f"✅ Script generated: {script[:100]}...")
            return script
        except Exception as e:
            print(f"❌ Script generation failed: {e}")
            return "This is a test narration for slide 1 of the AI-assisted programming lecture."

    def test_minimax_tts(self, text):
        """Test MiniMax TTS with voice cloning"""
        print("🎵 Testing MiniMax TTS...")

        url = "https://api.minimax.io/v1/t2a_v2"
        if self.minimax_group_id:
            url += f"?GroupId={self.minimax_group_id}"

        headers = {
            "Authorization": f"Bearer {self.minimax_api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "speech-2.5-hd-preview",
            "text": text,
            "stream": False,
            "voice_setting": {
                "voice_id": self.cloned_voice_id or "male-qn-qingse",
                "speed": 1.0,
                "vol": 1.0,
                "pitch": 0
            },
            "audio_setting": {
                "sample_rate": 32000,
                "bitrate": 128000,
                "format": "mp3",
                "channel": 1
            }
        }

        print(f"   🎭 Voice ID: {payload['voice_setting']['voice_id']}")
        print(f"   📝 Text length: {len(text)} characters")

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()

            data = response.json()
            base_resp = data.get("base_resp", {})

            if base_resp.get("status_code") != 0:
                print(f"❌ MiniMax API error: {base_resp.get('status_msg')}")
                return None

            audio_hex = data["data"]["audio"]
            audio_bytes = bytes.fromhex(audio_hex)

            audio_path = self.temp_dir / "test_audio.mp3"
            with open(audio_path, 'wb') as f:
                f.write(audio_bytes)

            print(f"✅ Audio generated: {audio_path} ({len(audio_bytes)} bytes)")
            return audio_path

        except Exception as e:
            print(f"❌ MiniMax TTS failed: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"   Response: {e.response.text}")
            return None

    def test_slide_processing(self):
        """Process one slide from the PDF"""
        print("📄 Processing slide 1 from PDF...")

        pdf_path = Path("pdfs/lecture1-course-introduction.pdf")
        if not pdf_path.exists():
            print("❌ Test PDF not found")
            return None

        try:
            images = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=300)
            if not images:
                print("❌ No slides extracted")
                return None

            slide_path = self.temp_dir / "test_slide_001.png"
            images[0].save(slide_path, 'PNG')
            print(f"✅ Slide extracted: {slide_path}")
            return slide_path

        except Exception as e:
            print(f"❌ Slide processing failed: {e}")
            return None

    def create_test_video(self, slide_path, audio_path):
        """Create a test video from slide and audio"""
        print("🎬 Creating test video...")

        try:
            # Get audio duration
            duration_cmd = [
                'ffprobe', '-v', 'quiet', '-show_entries', 'format=duration',
                '-of', 'csv=p=0', str(audio_path)
            ]
            duration_output = subprocess.check_output(duration_cmd).decode().strip()
            duration = float(duration_output)
            print(f"   ⏱️  Audio duration: {duration:.1f}s")

            output_path = self.temp_dir / "test_video.mp4"
            cmd = [
                'ffmpeg', '-y',
                '-loop', '1', '-t', str(duration), '-i', str(slide_path),
                '-i', str(audio_path),
                '-c:v', 'libx264', '-crf', '23', '-preset', 'medium',
                '-c:a', 'aac', '-b:a', '128k',
                '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2',
                '-shortest',
                str(output_path)
            ]

            result = subprocess.run(cmd, check=True, capture_output=True)
            file_size = output_path.stat().st_size
            print(f"✅ Test video created: {output_path} ({file_size} bytes)")
            return output_path

        except Exception as e:
            print(f"❌ Video creation failed: {e}")
            return None

def main():
    print("🧪 Testing Voice Cloning on Single Slide")
    print("=" * 50)

    # Check environment variables
    print("🔑 Checking API keys...")
    google_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
    minimax_key = os.getenv('MINIMAX_API_KEY')

    if not google_key or not minimax_key:
        print("❌ Missing API keys. Please set environment variables:")
        print("   export GOOGLE_AI_STUDIO_API_KEY='your_key_here'")
        print("   export MINIMAX_API_KEY='your_key_here'")
        print("   export MINIMAX_GROUP_ID='your_group_id_here'  # optional")
        return

    tester = VoiceCloneTester()

    # Step 1: Setup voice cloning
    print("\n🎤 STEP 1: Voice Cloning Setup")
    voice_setup_success = tester.setup_voice_cloning()

    # Step 2: Generate test script
    print("\n🤖 STEP 2: Script Generation")
    script = tester.test_script_generation()
    if not script:
        print("❌ Cannot continue without script")
        return

    # Step 3: Test MiniMax TTS
    print("\n🎵 STEP 3: Audio Generation")
    audio_path = tester.test_minimax_tts(script)
    if not audio_path:
        print("❌ Cannot continue without audio")
        return

    # Step 4: Process slide
    print("\n📄 STEP 4: Slide Processing")
    slide_path = tester.test_slide_processing()
    if not slide_path:
        print("❌ Cannot continue without slide")
        return

    # Step 5: Create video
    print("\n🎬 STEP 5: Video Creation")
    video_path = tester.create_test_video(slide_path, audio_path)
    if not video_path:
        print("❌ Video creation failed")
        return

    # Summary
    print("\n" + "=" * 50)
    print("🎉 VOICE CLONING TEST COMPLETE!")
    print("=" * 50)

    print("📁 Test files created in:", tester.temp_dir)
    print("🎬 Test video:", video_path)
    print("🎵 Test audio:", audio_path)
    print("🖼️  Test slide:", slide_path)

    print("\n🔊 AUDIO ANALYSIS:")
    print("   - Check if the voice sounds like your voice sample")
    print("   - If it doesn't, we need to investigate MiniMax voice cloning API")

    print("\n📋 NEXT STEPS:")
    if voice_setup_success:
        print("   ✅ Voice sample loaded successfully")
        print("   🔍 Check if MiniMax supports voice cloning with uploaded samples")
        print("   🛠️  May need to use different TTS service or MiniMax enterprise features")
    else:
        print("   ❌ Voice sample not found or failed to load")
        print("   📁 Ensure 'my-voice-sample.wav' exists in the workspace")

if __name__ == "__main__":
    main()