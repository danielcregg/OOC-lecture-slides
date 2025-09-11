#!/bin/bash
# Setup API keys for local testing

echo "🔑 Setting up API keys for voice cloning test..."
echo ""

# Check if keys are already set
if [ -n "$GOOGLE_AI_STUDIO_API_KEY" ] && [ -n "$MINIMAX_API_KEY" ]; then
    echo "✅ API keys already set in environment"
    echo "   GOOGLE_AI_STUDIO_API_KEY: ${GOOGLE_AI_STUDIO_API_KEY:0:10}..."
    echo "   MINIMAX_API_KEY: ${MINIMAX_API_KEY:0:10}..."
else
    echo "❌ API keys not found in environment"
    echo ""
    echo "Please set them using:"
    echo "   export GOOGLE_AI_STUDIO_API_KEY='your_google_key_here'"
    echo "   export MINIMAX_API_KEY='your_minimax_key_here'"
    echo "   export MINIMAX_GROUP_ID='your_group_id_here'  # optional"
    echo ""
    echo "You can find these keys in:"
    echo "   - GitHub repository settings → Secrets and variables → Actions"
    echo "   - Google AI Studio: https://aistudio.google.com/app/apikey"
    echo "   - MiniMax console: https://api.minimax.chat/"
    exit 1
fi

echo ""
echo "🚀 Running voice cloning test..."
python test_voice_cloning.py