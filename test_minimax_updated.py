#!/usr/bin/env python3
"""
Test script for MiniMax TTS API integration
Run with: python test_minimax_updated.py
Make sure to set environment variables:
export MINIMAX_API_KEY="your_actual_key"
export MINIMAX_GROUP_ID="your_group_id"  # optional
"""

import os
import requests
from pathlib import Path
import tempfile

class MiniMaxTester:
    def __init__(self):
        self.minimax_api_key = os.getenv('MINIMAX_API_KEY')
        self.minimax_group_id = os.getenv('MINIMAX_GROUP_ID')
        self.temp_dir = Path(tempfile.mkdtemp())

        if not self.minimax_api_key:
            print("ERROR: MINIMAX_API_KEY environment variable not set")
            return

        print(f"API Key configured: {self.minimax_api_key[:10]}...")
        print(f"Group ID: {self.minimax_group_id}")

    def test_minimax_api(self, text="Hello, this is a test of the updated MiniMax TTS API integration."):
        """Test the MiniMax API with the updated format"""
        print(f"\n=== Testing MiniMax API ===")
        print(f"Text to convert: {text}")

        base_url = "https://api.minimax.io/v1/t2a_v2"

        if self.minimax_group_id:
            url = f"{base_url}?GroupId={self.minimax_group_id}"
            print(f"Using voice cloning with group_id: {self.minimax_group_id}")
        else:
            url = base_url
            print("Using default voice")

        headers = {
            "Authorization": f"Bearer {self.minimax_api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "speech-2.5-hd-preview",
            "text": text,
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

        print(f"Request URL: {url}")
        print(f"Request headers: {headers}")
        print(f"Request payload: {payload}")

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            print(f"\nResponse status: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                print(f"Response keys: {list(result.keys())}")
                print(f"Full response: {result}")

                # Check for successful response
                base_resp = result.get("base_resp", {})
                if base_resp.get("status_code") == 0:
                    print("✅ API call successful!")

                    # Extract audio from data.audio (hex format)
                    data = result.get("data", {})
                    if isinstance(data, dict) and "audio" in data:
                        audio_hex = data["audio"]
                        print(f"✅ Found hex audio data (length: {len(audio_hex)})")

                        try:
                            audio_bytes = bytes.fromhex(audio_hex)
                            print(f"✅ Successfully decoded hex audio ({len(audio_bytes)} bytes)")

                            # Save the audio file
                            audio_path = self.temp_dir / "test_audio.mp3"
                            with open(audio_path, 'wb') as f:
                                f.write(audio_bytes)

                            print(f"✅ Audio saved to: {audio_path}")
                            return True
                        except ValueError as e:
                            print(f"❌ Failed to decode hex audio: {e}")
                            return False
                    else:
                        print(f"❌ No audio data found in response data: {list(data.keys()) if isinstance(data, dict) else type(data)}")
                        return False
                else:
                    print(f"❌ API error: {base_resp.get('status_msg', 'Unknown error')}")
                    return False
            else:
                print(f"❌ HTTP error: {response.status_code}")
                print(f"Response: {response.text}")
                return False

        except requests.RequestException as e:
            print(f"❌ Request error: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Response: {e.response.text}")
            return False

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False

def main():
    tester = MiniMaxTester()
    if not tester.minimax_api_key:
        return

    success = tester.test_minimax_api()
    if success:
        print("\n🎉 MiniMax API integration test PASSED!")
        print("The updated workflow should now work correctly.")
    else:
        print("\n❌ MiniMax API integration test FAILED!")
        print("Check your API credentials and try again.")

if __name__ == "__main__":
    main()