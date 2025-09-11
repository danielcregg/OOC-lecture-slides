# AI-Generated Lecture Videos

This directory will contain automatically generated videos for the AIAP lecture slides.

## 🎬 Video Generation Status

*No videos have been generated yet. Run the "Generate Lecture Videos" GitHub Action to create videos.*

## 📋 Setup Checklist

Before running video generation, ensure:

- [ ] **GitHub Secrets Configured**
  - `GOOGLE_AI_STUDIO_API_KEY` - Your Google AI Studio API key
  - `MINIMAX_API_KEY` - Your MiniMax API key

- [ ] **Voice Sample Ready**
  - `my-voice-sample.wav` exists in repository root ✅
  - File size: ~462KB ✅
  - Quality: Clear, noise-free recording recommended

- [ ] **PDFs Available**
  - Lecture PDFs exist in `/pdfs` directory
  - PDFs are properly formatted for slide extraction

## 🚀 How to Generate Videos

1. **Go to GitHub Actions**
   - Navigate to the "Actions" tab in your repository
   - Find "Generate Lecture Videos" workflow

2. **Run Workflow**
   - Click "Run workflow" button
   - Choose options:
     - **Lecture Filter**: `all` (or specific lectures like `lecture1,lecture2`)
     - **Force Regenerate**: `false` (unless you want to regenerate all)

3. **Monitor Progress**
   - Watch workflow logs for processing status
   - Videos will appear here when complete

## 📊 Expected Processing Time

- **Per Slide**: ~30-60 seconds (Gemini + MiniMax + FFmpeg)
- **Lecture 1** (~15 slides): ~10-15 minutes
- **Lecture 2** (~20 slides): ~15-20 minutes

*Times may vary based on API response times and slide complexity*

## 🔍 Troubleshooting

If video generation fails:

1. **Check API Keys**
   - Verify secrets are set correctly in repository settings
   - Test API access independently

2. **Voice Sample Issues**
   - Ensure `my-voice-sample.wav` is high quality
   - Try a shorter, clearer sample if needed

3. **PDF Problems**
   - Check if PDFs are readable and not corrupted
   - Ensure PDFs are not password protected

4. **Workflow Logs**
   - Review detailed logs in GitHub Actions
   - Look for specific error messages

## 📁 Video Output Format

When generated, videos will be:
- **Format**: MP4 (H.264 + AAC)
- **Resolution**: 1920x1080 (Full HD)
- **Quality**: High (CRF 23)
- **Naming**: `lecture#-title.mp4`

## 🎯 Next Steps

1. **Configure API Keys** in GitHub repository secrets
2. **Run the workflow** to generate your first videos
3. **Review and iterate** on voice quality and script generation

---

*Ready to transform your slides into engaging AI-narrated videos!* 🤖🎥