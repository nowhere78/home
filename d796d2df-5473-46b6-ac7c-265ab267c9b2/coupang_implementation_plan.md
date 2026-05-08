# Coupang Partners Automation: Phase 1

Our goal is to leverage the existing "Alpha Agent" video engine to create high-converting shopping shorts for Coupang Partners.

## Proposed Changes

### [NEW] [coupang_agent.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/luna-agent/coupang_agent.py)
- A new script that takes a product name or category.
- Orchestrates the creation of a "Top Picks" or "Review" script using Gemma.
- Calls the video pipeline to generate the final MP4.

### [MODIFY] [luna_shorts_pipeline.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/luna-agent/luna_shorts_pipeline.py)
- Add `COUPANG_REVIEW_NICHE` with shopping-specific hooks (e.g., "Don't buy this until you see this!").
- Update prompt templates for product-focused content.

### [NEW] [coupang_products.json](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/data/coupang/coupang_products.json)
- Store metadata of products we've processed to avoid duplicates and track links.

## Verification Plan

### Manual Verification
1. Run `python src/luna-agent/coupang_agent.py --product "가성비 게이밍 마우스"`
2. Verify that a shopping-focused script is generated with "Buy" hooks.
3. Check the `output/shorts` folder for the final video.
