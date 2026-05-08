import requests
import os

urls = [
    "https://i5.walmartimages.com/seo/25-Cup-Food-Processor-Large-Meat-Grinder-Electric-Chopper-Vegetable-Food-Blender-1200W-Powerful-Copper-Motor-Includes-3-Sets-Bi-Level-Blades-1Bowl-6L_d412e1c5-6b78-4c52-b386-fb9b3670f82c.1bee51e78d5407362233d0fe00d2347e.jpeg",
    "https://i.pinimg.com/videos/thumbnails/originals/ef/26/55/ef265505014c3a82f83f5965ecb44ecc.0000000.jpg",
    "https://i.ebayimg.com/images/g/-Z8AAOSwH1lnA7A8/s-l1200.jpg",
    "https://i5.walmartimages.com/asr/e5055d16-2ea2-497a-bda4-53211b47903d.7dfa689855cb6110adc8639162b4ae6f.jpeg",
    "https://i5.walmartimages.com/seo/Electric-Chicken-Breast-Shredder-Twist-Machine-Automatic-Meat-Shredder-Tool-for-Home-Restaurant-Use-White_91cc77c6-eec7-4885-a987-19dda6aabdcf.bf97af0c43016ba5e9a67ce09e3eb2e8.jpeg"
]

dest_dir = r"C:\Users\smile\알파에이전트\docs\automation\shorts_output\temp_assets\meat_shredder"
for i, url in enumerate(urls):
    try:
        response = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(os.path.join(dest_dir, f"full_img_{i}.jpg"), "wb") as f:
                f.write(response.content)
            print(f"Downloaded: full_img_{i}.jpg")
    except Exception as e:
        print(f"Failed {url}: {e}")
