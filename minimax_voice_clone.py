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
        # Use same environment variables as your working script
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
        """List existing voice clones using multiple potential endpoints"""
        print("📋 Attempting to list voice clones...")
        
        # Try multiple potential endpoints
        endpoints_to_try = [
            'https://api.minimax.io/v1/voice_clones',
            'https://api.minimax.io/v1/voices',
            'https://api.minimax.io/v1/voice_clone/list',
            'https://api.minimax.io/v1/t2a/voices',
            'https://api.minimax.io/v1/voice_settings'
        ]
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        for endpoint in endpoints_to_try:
            try:
                url = endpoint
                if self.group_id:
                    separator = '&' if '?' in url else '?'
                    url += f'{separator}GroupId={self.group_id}'
                
                print(f"   🔍 Trying endpoint: {endpoint}")
                response = requests.get(url, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"✅ Success! Voice data retrieved from: {endpoint}")
                    print(f"📋 Response: {json.dumps(result, indent=2)}")
                    return result
                elif response.status_code == 404:
                    print(f"   ❌ Not found: {endpoint}")
                    continue
                elif response.status_code == 401:
                    print(f"   🔐 Authentication issue: {endpoint}")
                    continue
                else:
                    print(f"   ⚠️  Status {response.status_code}: {response.text[:200]}...")
                    continue
                    
            except Exception as e:
                print(f"   ❌ Error trying {endpoint}: {e}")
                continue
        
        print("ℹ️  No working voice listing endpoint found.")
        print("\n💡 Alternative: Try testing with known voice IDs:")
        print("   - DanielTestVoice123 (from recent test)")
        print("   - Try generate-speech with your known voice IDs")
        
        # Suggest testing known voice IDs
        return self._test_known_voices()
    
    def _test_known_voices(self):
        """Test speech generation with potentially known voice IDs"""
        print("\n🧪 Testing known voice IDs...")
        
        # List of voice IDs that might exist based on recent activity
        test_voice_ids = [
            "danielVoice15092025",    # Most recent voice clone
            "DanielTestVoice123",     # From earlier successful test
            "DanielVoice1min",        # From earlier attempt
            "MyTestVoice123",         # Common test pattern
        ]
        
        working_voices = []
        
        for voice_id in test_voice_ids:
            print(f"\n   🎭 Testing voice: {voice_id}")
            try:
                # Use a very short test to avoid wasting tokens
                result = self.generate_speech(
                    voice_id=voice_id, 
                    text="Test", 
                    output_filename=f"voice_test_{voice_id}.mp3"
                )
                if result:
                    working_voices.append(voice_id)
                    print(f"   ✅ Voice '{voice_id}' is working!")
                else:
                    print(f"   ❌ Voice '{voice_id}' not found")
            except Exception as e:
                print(f"   ❌ Error testing '{voice_id}': {e}")
        
        if working_voices:
            print(f"\n🎉 Found {len(working_voices)} working voice(s):")
            for voice in working_voices:
                print(f"   🎤 {voice}")
            return {"working_voices": working_voices}
        else:
            print("\n❌ No working voice clones found.")
            return {"working_voices": []}

    def delete_voice_clone(self, voice_id):
        """Delete a voice clone using the MiniMax API"""
        print(f"🗑️ Attempting to delete voice clone: {voice_id}")
        
        # Try multiple potential delete endpoints
        delete_endpoints = [
            f'https://api.minimax.io/v1/voice_clone/{voice_id}',
            f'https://api.minimax.io/v1/voice_clone/delete',
            f'https://api.minimax.io/v1/voices/{voice_id}',
            f'https://api.minimax.io/v1/voice_clones/{voice_id}/delete'
        ]
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        for endpoint in delete_endpoints:
            try:
                url = endpoint
                if self.group_id:
                    separator = '&' if '?' in url else '?'
                    url += f'{separator}GroupId={self.group_id}'
                
                print(f"   🔍 Trying DELETE endpoint: {endpoint}")
                
                # Try DELETE method
                response = requests.delete(url, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"✅ Successfully deleted voice '{voice_id}'")
                    print(f"   Response: {json.dumps(result, indent=2)}")
                    return True
                elif response.status_code == 404:
                    print(f"   ❌ Endpoint not found: {endpoint}")
                    continue
                else:
                    print(f"   ⚠️  Status {response.status_code}: {response.text[:200]}...")
                    
                # Also try POST method with delete action (some APIs use this pattern)
                if 'delete' in endpoint:
                    payload = json.dumps({"voice_id": voice_id})
                    response = requests.post(url, headers=headers, data=payload, timeout=10)
                    
                    if response.status_code == 200:
                        result = response.json()
                        print(f"✅ Successfully deleted voice '{voice_id}' via POST")
                        print(f"   Response: {json.dumps(result, indent=2)}")
                        return True
                        
            except Exception as e:
                print(f"   ❌ Error trying {endpoint}: {e}")
                continue
        
        print(f"❌ Could not find working delete endpoint for voice '{voice_id}'")
        print("ℹ️  MiniMax might not provide voice deletion via API")
        return False

    def delete_all_voice_clones(self):
        """Delete all voice clones by first finding them, then deleting each one"""
        print("🗑️ DELETING ALL VOICE CLONES")
        print("=" * 40)
        
        # First, get list of working voices
        print("Step 1: Finding existing voice clones...")
        list_result = self.list_voice_clones()
        
        if not list_result or not list_result.get('working_voices'):
            print("❌ No working voice clones found to delete.")
            return False
        
        working_voices = list_result['working_voices']
        print(f"\n📋 Found {len(working_voices)} voice(s) to delete:")
        for voice in working_voices:
            print(f"   🎤 {voice}")
        
        # Confirm deletion
        print(f"\n⚠️  WARNING: This will attempt to delete {len(working_voices)} voice clone(s)")
        print("   This action cannot be undone!")
        
        # For safety in automated environment, we'll proceed but with clear warnings
        print("\nStep 2: Attempting to delete each voice...")
        
        deleted_count = 0
        failed_count = 0
        
        for voice_id in working_voices:
            print(f"\n🗑️ Deleting voice: {voice_id}")
            success = self.delete_voice_clone(voice_id)
            if success:
                deleted_count += 1
                print(f"   ✅ Deleted: {voice_id}")
            else:
                failed_count += 1
                print(f"   ❌ Failed to delete: {voice_id}")
        
        # Summary
        print("\n" + "=" * 40)
        print("🗑️ DELETION SUMMARY")
        print("=" * 40)
        print(f"✅ Successfully deleted: {deleted_count}")
        print(f"❌ Failed to delete: {failed_count}")
        print(f"📊 Total processed: {len(working_voices)}")
        
        if failed_count > 0:
            print("\n💡 Note: Some voices might not be deletable via API.")
            print("   You may need to delete them manually from MiniMax dashboard.")
        
        return deleted_count > 0

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

    # Delete voice clone commands
    delete_parser = subparsers.add_parser("delete", help="Delete a specific voice clone.")
    delete_parser.add_argument("voice_id", type=str, help="The voice ID to delete.")

    delete_all_parser = subparsers.add_parser("delete-all", help="Delete ALL voice clones (use with caution!).")

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
                
        elif args.command == "list":
            cloner.list_voice_clones()
            
        elif args.command == "delete":
            success = cloner.delete_voice_clone(args.voice_id)
            if success:
                print(f"\n🎉 Voice '{args.voice_id}' deleted successfully!")
            else:
                print(f"\n❌ Failed to delete voice '{args.voice_id}'")
                print("   Check if the voice exists or if deletion is supported.")
                
        elif args.command == "delete-all":
            print("⚠️  WARNING: You are about to delete ALL your voice clones!")
            print("   This action cannot be undone.")
            success = cloner.delete_all_voice_clones()
            if success:
                print("\n🎉 Voice deletion process completed!")
            else:
                print("\n❌ Voice deletion process failed or no voices found.")
            
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