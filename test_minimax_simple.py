#!/usr/bin/env python3
"""
Simple test script for MiniMax TTS API integration
"""
import os
import requests
import json

def test_minimax_api():
    """Test MiniMax TTS API with real credentials"""

    # Get credentials from environment
    api_key = os.getenv('MINIMAX_API_KEY')
    group_id = os.getenv('MINIMAX_GROUP_ID')

    if not api_key or not group_id:
        print("❌ Missing MiniMax credentials")
        return False

    print(f"🔑 Using Group ID: {group_id}")
    print(f"🔑 API Key: {api_key[:10]}...")

    # MiniMax API endpoint and parameters (from working workflow)
    url = "https://api.minimax.io/v1/t2a_v2"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Use the exact payload structure from the working workflow
    payload = {
        "model": "speech-2.5-hd-preview",
        "text": "Hello, this is a test of the MiniMax text-to-speech API integration.",
        "stream": False,
        "voice_setting": {
            "voice_id": "male-qn-qingse",
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

    print("📡 Sending request to MiniMax API with correct payload structure...")
    print(f"Payload: {json.dumps(payload, indent=2)}")

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)

        print(f"📊 Response status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ API call successful!")

            # Check for successful response
            base_resp = data.get("base_resp", {})
            if base_resp.get("status_code") != 0:
                print(f"❌ MiniMax API error: {base_resp.get('status_msg', 'Unknown error')}")
                print(f"Full response: {json.dumps(data, indent=2)}")
                return False

            # Extract audio from data.audio (hex format)
            data_section = data.get("data", {})
            if isinstance(data_section, dict) and "audio" in data_section:
                audio_hex = data_section["audio"]
                print(f"🎵 Audio data received: {len(audio_hex)} characters")
                try:
                    audio_bytes = bytes.fromhex(audio_hex)
                    print(f"✅ Successfully decoded hex audio: {len(audio_bytes)} bytes")

                    # Save test audio file
                    with open('/workspaces/AIAP-lecture-slides/test_audio.mp3', 'wb') as f:
                        f.write(audio_bytes)
                    print("💾 Test audio saved to test_audio.mp3")

                    return True
                except ValueError as e:
                    print(f"❌ Failed to decode hex audio: {e}")
                    return False
            else:
                print(f"❌ No audio data found in response. Available keys: {list(data_section.keys()) if isinstance(data_section, dict) else type(data_section)}")
                print(f"Full response: {json.dumps(data, indent=2)}")
                return False
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error during API call: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing MiniMax TTS API Integration")
    print("=" * 50)

    success = test_minimax_api()

    if success:
        print("\n🎉 MiniMax API integration test PASSED!")
        print("✅ API endpoint working correctly")
        print("✅ Authentication successful")
        print("✅ Audio generation working")
        print("✅ Hex decoding working")
        print("✅ Ready for video generation pipeline")
    else:
        print("\n💥 MiniMax API integration test FAILED")
        print("❌ Check the error messages above")