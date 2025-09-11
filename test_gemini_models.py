#!/usr/bin/env python3
"""
Test available Gemini models and their status
"""
import os
import google.generativeai as genai

def test_gemini_models():
    """Test different Gemini model configurations"""

    # Get API key
    api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
    if not api_key:
        print("❌ GOOGLE_AI_STUDIO_API_KEY not found")
        return

    print(f"🔑 API Key: {api_key[:15]}...")
    print("🧪 Testing Gemini Models Availability")
    print("=" * 60)

    # Configure Gemini
    try:
        genai.configure(api_key=api_key)
        print("✅ Gemini API configured successfully")
    except Exception as e:
        print(f"❌ Gemini configuration failed: {e}")
        return

    # Test different model names
    models_to_test = [
        "gemini-2.5-pro",
        "gemini-2.5-flash",
        "gemini-2.5-pro-preview",
        "gemini-2.5-flash-preview",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "gemini-1.5-pro-latest",
        "gemini-1.5-flash-latest",
        "gemini-pro",
        "gemini-flash"
    ]

    print("\n🔍 Testing Model Availability:")
    print("-" * 40)

    working_models = []
    failed_models = []

    for model_name in models_to_test:
        print(f"\n🧪 Testing: {model_name}")
        try:
            # Try to create the model
            model = genai.GenerativeModel(model_name)
            print(f"  ✅ Model created successfully")

            # Try a simple generation to test if it actually works
            response = model.generate_content("Hello, test message")
            if response and response.text:
                print(f"  ✅ Generation successful: {response.text[:50]}...")
                working_models.append((model_name, "Working"))
            else:
                print(f"  ⚠️ Model created but generation returned empty")
                working_models.append((model_name, "Created but empty response"))

        except Exception as e:
            error_msg = str(e)
            print(f"  ❌ Failed: {error_msg[:100]}...")
            failed_models.append((model_name, error_msg[:100]))

    print("\n" + "=" * 60)
    print("📊 RESULTS SUMMARY")
    print("=" * 60)

    print(f"\n✅ WORKING MODELS ({len(working_models)}):")
    for model, status in working_models:
        print(f"  • {model}: {status}")

    print(f"\n❌ FAILED MODELS ({len(failed_models)}):")
    for model, error in failed_models:
        print(f"  • {model}: {error}")

    print("\n💡 RECOMMENDED FALLBACK ORDER:")
    recommended = [m[0] for m in working_models]
    for i, model in enumerate(recommended, 1):
        print(f"  {i}. {model}")

    if working_models:
        print("\n🎉 SUCCESS! Found working Gemini models!")
        print(f"🚀 Primary model to use: {working_models[0][0]}")
    else:
        print("\n💥 No working models found. Check API key and quota.")

if __name__ == "__main__":
    test_gemini_models()