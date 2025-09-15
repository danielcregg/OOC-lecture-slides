#!/usr/bin/env python3
"""
MiniMax Voice Cloning Script
Based on working local implementation
Supports: file upload, voice cloning, and speech generation with custom voices
"""

import os
import json
import requests
import argparse
from pathlib import Path

class MiniMaxVoiceClone:
    def __init__(self):
        # Use same environment variables a        elif args.command == "clone":
            result = cloner.clone_voice(args.file_id, args.voice_id)
            if result.get('success'):
                print("\n🎉 Voice cloning completed successfully!")
                print("\n📝 To use your cloned voice for speech generation:")
                voice_to_use = result.get('returned_voice_id', args.voice_id)
                print(f"   python minimax_voice_clone.py generate-speech '{voice_to_use}' 'Your text here'")
            else:
                print(f"\n❌ Voice cloning failed: {result.get('error', 'Unknown error')}")
                
        elif args.command == "list":
            cloner.list_voice_clones()
            
        elif args.command == "generate-speech":ing script
        self.group_id = os.getenv("GROUP_ID")
        self.api_key = os.getenv("API_KEY")
        
        # Also check for alternative environment variable names
        if not self.group_id:
            self.group_id = os.getenv("MINIMAX_GROUP_ID")
        if not self.api_key:
            self.api_key = os.getenv("MINIMAX_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "Missing API key. Set either API_KEY or MINIMAX_API_KEY environment variable.\n"
                "Example: export API_KEY='your_minimax_api_key'"
            )
        
        print(f"✅ API Key configured: {self.api_key[:10]}...")
        if self.group_id:
            print(f"✅ Group ID: {self.group_id}")
        else:
            print("⚠️  No Group ID provided - using default settings")

    def upload_file(self, file_path):
        """Uploads a file to the MiniMax API."""
        if not Path(file_path).exists():
            print(f"❌ File not found: {file_path}")
            return None
            
        print(f"📤 Uploading file: {file_path}")
        
        url = f'https://api.minimax.io/v1/files/upload'
        if self.group_id:
            url += f'?GroupId={self.group_id}'
            
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'purpose': 'voice_clone'
        }
        
        try:
            with open(file_path, 'rb') as f:
                files = {
                    'file': f
                }
                response = requests.post(url, headers=headers, data=data, files=files)
                response.raise_for_status()
                
                result = response.json()
                file_id = result.get("file", {}).get("file_id")
                
                if file_id:
                    print(f"✅ File uploaded successfully. File ID: {file_id}")
                    return file_id
                else:
                    print(f"❌ Error uploading file: {response.text}")
                    return None
                    
        except requests.exceptions.RequestException as e:
            print(f"❌ Upload request failed: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"   Response: {e.response.text}")
            return None
        except Exception as e:
            print(f"❌ Upload error: {e}")
            return None

    def clone_voice(self, file_id, voice_id):
        """Clones a voice using the MiniMax API."""
        print(f"🎭 Cloning voice with ID: {voice_id}")
        
        url = f'https://api.minimax.io/v1/voice_clone'
        if self.group_id:
            url += f'?GroupId={self.group_id}'
            
        payload = json.dumps({
            "file_id": file_id,
            "voice_id": voice_id
        })
        headers = {
            'authorization': f'Bearer {self.api_key}',
            'content-type': 'application/json'
        }
        
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            
            result = response.json()
            print("✅ Voice cloning request successful.")
            print(f"   Full Response: {json.dumps(result, indent=2)}")
            
            # Extract important information from response
            voice_clone_info = {
                'success': True,
                'voice_id': voice_id,  # The voice_id we provided
                'original_file_id': file_id  # The file_id we used
            }
            
            # Check for additional IDs in response (MiniMax may return different structure)
            if 'data' in result:
                data = result['data']
                if 'voice_id' in data:
                    voice_clone_info['returned_voice_id'] = data['voice_id']
                if 'file_id' in data:
                    voice_clone_info['returned_file_id'] = data['file_id']
                if 'clone_id' in data:
                    voice_clone_info['clone_id'] = data['clone_id']
            
            # Also check top level for IDs
            if 'voice_id' in result:
                voice_clone_info['returned_voice_id'] = result['voice_id']
            if 'file_id' in result:
                voice_clone_info['returned_file_id'] = result['file_id']
            if 'clone_id' in result:
                voice_clone_info['clone_id'] = result['clone_id']
            
            # Display extracted information
            print("\n📋 VOICE CLONING RESULTS:")
            print(f"   🎭 Requested Voice ID: {voice_clone_info['voice_id']}")
            print(f"   📄 Original File ID: {voice_clone_info['original_file_id']}")
            
            if 'returned_voice_id' in voice_clone_info:
                print(f"   ✅ Returned Voice ID: {voice_clone_info['returned_voice_id']}")
            if 'returned_file_id' in voice_clone_info:
                print(f"   ✅ Returned File ID: {voice_clone_info['returned_file_id']}")
            if 'clone_id' in voice_clone_info:
                print(f"   ✅ Clone ID: {voice_clone_info['clone_id']}")
            
            print("\n💡 IMPORTANT: Save these IDs for generating speech with your cloned voice!")
            
            return voice_clone_info
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Voice cloning request failed: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"   Response: {e.response.text}")
            return {'success': False, 'error': str(e)}
        except Exception as e:
            print(f"❌ Voice cloning error: {e}")
            return {'success': False, 'error': str(e)}

    def list_voice_clones(self):
        """List existing voice clones (if supported by API)"""
        print("📋 Listing existing voice clones...")
        
        # This endpoint may not exist - it's for testing
        url = f'https://api.minimax.io/v1/voice_clones'
        if self.group_id:
            url += f'?GroupId={self.group_id}'
            
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print("✅ Voice clones retrieved:")
                print(f"   {json.dumps(result, indent=2)}")
                return result
            elif response.status_code == 404:
                print("ℹ️  Voice clone listing not supported by API")
                return None
            else:
                print(f"⚠️  API returned status {response.status_code}: {response.text}")
                return None
                
        except Exception as e:
            print(f"ℹ️  Could not list voice clones (may not be supported): {e}")
            return None

    def generate_speech(self, voice_id, text, output_filename="output.mp3"):
        """Generates speech from text using the MiniMax T2A v2 API."""
        print(f"🎵 Generating speech with voice: {voice_id}")
        print(f"📝 Text: {text[:100]}{'...' if len(text) > 100 else ''}")
        
        url = f'https://api.minimax.io/v1/t2a_v2'
        if self.group_id:
            url += f'?GroupId={self.group_id}'
            
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "model": "speech-2.5-hd-preview",  # Using the HD preview model
            "text": text,
            "stream": False,
            "voice_setting": {
                "voice_id": voice_id,
                "speed": 1,
                "vol": 1,
                "pitch": 0
            },
            "audio_setting": {
                "sample_rate": 32000,
                "bitrate": 128000,
                "format": "mp3",
                "channel": 1
            }
        })
        
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            
            response_data = response.json()
            base_resp = response_data.get("base_resp", {})
            
            if base_resp.get("status_code") == 0:
                audio_hex = response_data.get("data", {}).get("audio")
                if audio_hex:
                    audio_bytes = bytes.fromhex(audio_hex)
                    output_path = Path(output_filename)
                    with open(output_path, "wb") as f:
                        f.write(audio_bytes)
                    print(f"✅ Speech generated successfully: {output_path} ({len(audio_bytes)} bytes)")
                    return output_path
                else:
                    print(f"❌ No audio data in response: {response.text}")
                    return None
            else:
                print(f"❌ Speech generation failed: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Speech generation request failed: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"   Response: {e.response.text}")
            return None
        except Exception as e:
            print(f"❌ Speech generation error: {e}")
            return None

    def test_voice_clone_workflow(self, audio_file, voice_id, test_text=None):
        """Test the complete voice cloning workflow"""
        print("🧪 Testing Complete Voice Cloning Workflow")
        print("=" * 50)
        
        # Default test text if none provided
        if not test_text:
            test_text = "Hello, this is a test of my cloned voice using MiniMax API. How does it sound?"
        
        # Step 1: Upload file
        print("\n📤 STEP 1: Upload Audio File")
        file_id = self.upload_file(audio_file)
        if not file_id:
            print("❌ Workflow failed at file upload")
            return False
        
        # Step 2: Clone voice
        print(f"\n🎭 STEP 2: Clone Voice (ID: {voice_id})")
        clone_result = self.clone_voice(file_id, voice_id)
        if not clone_result.get('success', False):
            print("❌ Workflow failed at voice cloning")
            print(f"   Error: {clone_result.get('error', 'Unknown error')}")
            return False
        
        # Use the returned voice ID if available, otherwise use original
        actual_voice_id = clone_result.get('returned_voice_id', voice_id)
        if actual_voice_id != voice_id:
            print(f"📝 Note: Using returned voice ID '{actual_voice_id}' instead of '{voice_id}'")
            voice_id = actual_voice_id
        
        # Wait a moment for voice cloning to process
        print("⏳ Waiting for voice cloning to process...")
        import time
        time.sleep(2)
        
        # Step 3: Generate speech with cloned voice
        print(f"\n🎵 STEP 3: Generate Speech")
        output_file = f"cloned_voice_{voice_id}_test.mp3"
        audio_path = self.generate_speech(voice_id, test_text, output_file)
        if not audio_path:
            print("❌ Workflow failed at speech generation")
            return False
        
        print("\n" + "=" * 50)
        print("🎉 VOICE CLONING WORKFLOW COMPLETE!")
        print("=" * 50)
        print(f"🎵 Generated audio: {audio_path}")
        print(f"🎭 Voice ID: {voice_id}")
        print(f"📝 Test text: {test_text}")
        print("\n🔊 Listen to the generated audio to verify voice quality!")
        return True


def main():
    parser = argparse.ArgumentParser(description="MiniMax Voice Cloning and Text-to-Speech App.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Voice cloning workflow command (new)
    test_parser = subparsers.add_parser("test", help="Test the complete voice cloning workflow.")
    test_parser.add_argument("file_path", type=str, help="The path to the audio file (mp3, m4a, or wav).")
    test_parser.add_argument("voice_id", type=str, help="A unique ID for the cloned voice (minimum 8 characters, letters and numbers, starting with a letter).")
    test_parser.add_argument("--text", type=str, help="Custom test text (optional).")

    # Individual component commands
    upload_parser = subparsers.add_parser("upload", help="Upload an audio file for voice cloning.")
    upload_parser.add_argument("file_path", type=str, help="The path to the audio file.")

    clone_parser = subparsers.add_parser("clone", help="Clone a voice from an uploaded file.")
    clone_parser.add_argument("file_id", type=str, help="The file ID returned from upload.")
    clone_parser.add_argument("voice_id", type=str, help="A unique ID for the cloned voice.")

    # List voice clones command
    list_parser = subparsers.add_parser("list", help="List existing voice clones (if supported).")

    speech_parser = subparsers.add_parser("generate-speech", help="Generate speech from text using a voice.")
    speech_parser.add_argument("voice_id", type=str, help="The ID of the voice to use (can be cloned or built-in).")
    speech_parser.add_argument("text", type=str, help="The text to convert to speech.")
    speech_parser.add_argument("--output", type=str, default="output.mp3", help="Output filename (default: output.mp3).")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        cloner = MiniMaxVoiceClone()
        
        if args.command == "test":
            # Test complete workflow
            custom_text = args.text if hasattr(args, 'text') and args.text else None
            cloner.test_voice_clone_workflow(args.file_path, args.voice_id, custom_text)
            
        elif args.command == "upload":
            cloner.upload_file(args.file_path)
            
        elif args.command == "clone":
            result = cloner.clone_voice(args.file_id, args.voice_id)
            if result.get('success'):
                print("\n🎉 Voice cloning completed successfully!")
                print("\n📝 To use your cloned voice for speech generation:")
                voice_to_use = result.get('returned_voice_id', args.voice_id)
                print(f"   python minimax_voice_clone.py generate-speech '{voice_to_use}' 'Your text here'")
            else:
                print(f"\n❌ Voice cloning failed: {result.get('error', 'Unknown error')}")
            
        elif args.command == "generate-speech":
            # Handle special test texts
            if args.text == "hamlet":
                hamlet_speech = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them: to die, to sleep
No more; and by a sleep, to say we end
The heart-ache, and the thousand natural shocks
That Flesh is heir to? 'Tis a consummation
Devoutly to be wished. To die, to sleep,
To sleep, perchance to Dream; aye, there's the rub,
For in that sleep of death, what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause."""
                cloner.generate_speech(args.voice_id, hamlet_speech, args.output)
            else:
                cloner.generate_speech(args.voice_id, args.text, args.output)
                
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()