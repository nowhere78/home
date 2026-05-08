# Coupang Partners Automation Walkthrough

I have implemented the core engine for your Coupang Partners automation. You can now generate high-quality shopping review videos by simply providing a product name.

## What's New

### 1. Coupang Agent (`coupang_agent.py`)
A dedicated script to manage Coupang product reviews. It connects your product ideas to the AI video engine.
- **Path**: `src/luna-agent/coupang_agent.py`

### 2. Shopping Niche Profile
I've added a new `COUPANG_REVIEW_NICHE` to the video pipeline. 
- **Features**: Aggressive "viral" hooks, faster pacing, and shopping-specific CTAs ("Check the link in the comments!").
- **Visuals**: Optimized to search for product and shopping-related imagery.

---

## 🛠️ How to Use (Test Run)

Open your terminal in the project root and run the following command to create your first Coupang review video:

```powershell
python src/luna-agent/coupang_agent.py --product "가성비 게이밍 마우스"
```

### What will happen:
1. **AI Scripting**: Gemma (or Luna) will generate a persuasive script about a gaming mouse.
2. **Image Fetching**: The engine will find high-quality images of gaming mice/tech.
3. **Voice Over**: Edge-TTS will generate a fast-paced Korean voice.
4. **Final Assembly**: FFmpeg will merge everything into an MP4 video in `output/shorts/`.

---

## Next Steps
- **API Integration**: Once you provide your Coupang Partners API keys, we can automate the product search and link generation.
- **Daily Scheduling**: We can set this to run every morning with the top 3 trending products.

Try running the command above and let me know how the video looks!
