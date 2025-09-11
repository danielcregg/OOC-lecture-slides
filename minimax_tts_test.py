import os, json, time, base64, sys, requests

def main():
    api_key = os.getenv('MINIMAX_API_KEY')
    group_id = os.getenv('MINIMAX_GROUP_ID')
    if not api_key:
        print('MINIMAX_API_KEY not set')
        sys.exit(1)

    base_url = "https://api.minimax.chat/v1/t2a_pro"
    url = base_url + (f"?GroupId={group_id}" if group_id else "")

    text = "This is a short test of the MiniMax text to speech API."

    payload = {
        "model": "speech-01-turbo",
        "text": text,
        "stream": False,
        "voice_setting": {
            "voice_id": "male-qn-qingse",
            "speed": 1.0,
            "vol": 1.0
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": "mp3",
            "channel": 1
        }
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print('Sending MiniMax TTS request...')
    r = requests.post(url, headers=headers, json=payload, timeout=60)
    print('Status code:', r.status_code)

    try:
        data = r.json()
    except Exception:
        print('Non-JSON response:', r.text[:500])
        return

    print('Top-level keys:', list(data.keys()))
    print('Full JSON (truncated):')
    print(json.dumps(data, indent=2)[:2000])

    audio_bytes = None

    # Possible locations for audio
    if isinstance(data.get('audio_file'), str):
        audio_url = data['audio_file']
        print('Downloading audio from audio_file URL...')
        ar = requests.get(audio_url, timeout=60)
        if ar.status_code == 200:
            audio_bytes = ar.content
            print('Downloaded audio via URL')
        else:
            print('Failed to download audio URL:', ar.status_code)

    if audio_bytes is None:
        nested = data.get('data', {})
        if isinstance(nested, dict) and 'audio' in nested:
            raw_audio = nested['audio']
            if isinstance(raw_audio, str):
                # Try hex then base64
                try:
                    audio_bytes = bytes.fromhex(raw_audio)
                    print('Decoded hex audio from data.audio')
                except ValueError:
                    try:
                        audio_bytes = base64.b64decode(raw_audio)
                        print('Decoded base64 audio from data.audio')
                    except Exception:
                        print('Failed to decode data.audio')

    # Additional nested path guess
    if audio_bytes is None and 'data' in data:
        task_result = data['data'].get('task_result') if isinstance(data['data'], dict) else None
        if isinstance(task_result, dict) and 'audio' in task_result:
            raw_audio = task_result['audio']
            if isinstance(raw_audio, str):
                for decoder, label in ((bytes.fromhex, 'hex'), (base64.b64decode, 'base64')):
                    try:
                        audio_bytes = decoder(raw_audio)
                        print(f'Decoded {label} audio from data.task_result.audio')
                        break
                    except Exception:
                        continue

    if audio_bytes is None:
        print('No audio bytes found in response; cannot proceed.')
        return

    out_dir = 'minimax_test_output'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'test_audio.mp3')
    with open(out_path, 'wb') as f:
        f.write(audio_bytes)
    print('Saved audio to', out_path)

if __name__ == '__main__':
    main()
