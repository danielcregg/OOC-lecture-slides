#!/bin/bash
# Setup script for MiniMax voice cloning

echo "🔧 Setting up MiniMax Voice Cloning Environment"
echo "================================================"

# Install required Python packages
echo "📦 Installing required packages..."
pip install -q requests python-dotenv

# Check for environment variables
echo ""
echo "🔑 Checking environment variables..."

if [ -z "$API_KEY" ] && [ -z "$MINIMAX_API_KEY" ]; then
    echo "❌ Missing API_KEY or MINIMAX_API_KEY environment variable"
    echo ""
    echo "Please set your MiniMax API credentials:"
    echo "   export API_KEY='your_minimax_api_key'"
    echo "   export GROUP_ID='your_group_id'  # optional"
    echo ""
    echo "Or alternatively:"
    echo "   export MINIMAX_API_KEY='your_minimax_api_key'"
    echo "   export MINIMAX_GROUP_ID='your_group_id'  # optional"
    echo ""
    exit 1
else
    echo "✅ API key found"
fi

if [ -z "$GROUP_ID" ] && [ -z "$MINIMAX_GROUP_ID" ]; then
    echo "⚠️  No Group ID found (optional for basic TTS)"
else
    echo "✅ Group ID found"
fi

# Check for audio file
echo ""
echo "🎵 Checking for audio sample..."
if [ -f "my-voice-sample.wav" ]; then
    echo "✅ Audio sample found: my-voice-sample.wav"
    file_size=$(ls -lh my-voice-sample.wav | awk '{print $5}')
    echo "   File size: $file_size"
else
    echo "⚠️  Audio sample not found: my-voice-sample.wav"
    echo "   You'll need an audio sample for voice cloning"
fi

echo ""
echo "🎯 Ready to test voice cloning!"
echo "Use: python minimax_voice_clone.py --help"