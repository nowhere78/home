# =====================================================
# 🎨 100plus.kr 블로그 이미지 22개 일괄 생성 (Kaggle SDXL)
# =====================================================
# 사용법:
# 1. https://www.kaggle.com 로그인
# 2. "New Notebook" 클릭
# 3. 오른쪽 Settings → Accelerator → "GPU T4 x2" 선택
# 4. 이 코드 전체를 셀에 붙여넣고 실행
# 5. 생성된 이미지는 /kaggle/working/ 폴더에 저장됨
# 6. 오른쪽 Output 탭에서 다운로드
# =====================================================

# ── 1단계: 라이브러리 설치 ──
!pip install -q diffusers transformers accelerate safetensors invisible_watermark

# ── 2단계: 모델 로딩 ──
import torch
from diffusers import StableDiffusionXLPipeline
import os

print("🚀 SDXL 모델 로딩 중... (약 2-3분 소요)")
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
)
pipe = pipe.to("cuda")

# 메모리 최적화
pipe.enable_xformers_memory_efficient_attention()
print("✅ 모델 로딩 완료!")

# ── 3단계: 22개 이미지 프롬프트 정의 ──
prompts = {
    "01_아르기닌": "Hyper-realistic medical 3D rendering of arginine molecular structure and vascular health, clean white background, professional medical textbook illustration, high quality, 4k",
    "02_콘드로이친": "Hyper-realistic medical 3D rendering of joint cartilage and chondroitin supplement, professional medical illustration, clean background, high quality, 4k",
    "03_흑염소": "Professional medical illustration of black goat extract and traditional Korean medicine tonic, clean modern aesthetic, herbs and medicine bottles, high quality, 4k",
    "04_비타민B군": "Medical 3D infographic of vitamin B complex supplements and cellular metabolism, professional health visualization, colorful capsules, clean background, 4k",
    "05_NAC": "Hyper-realistic molecular structure of N-acetylcysteine antioxidant, professional medical illustration, clean background, glowing molecular bonds, 4k",
    "06_오메가3": "Professional 3D illustration of omega-3 fish oil capsules and heart health, clean medical aesthetic, golden capsules, anatomical heart, 4k",
    "07_혈당스파이크": "Medical illustration of blood sugar monitoring and glucose meter, professional health visualization, finger prick test, clean background, 4k",
    "08_허리디스크": "Professional 3D medical illustration of lumbar spine and intervertebral disc, clean background, anatomical cross section, blue tones, 4k",
    "09_탈모": "Medical illustration of hair follicles and scalp treatment, professional 3D rendering, clean aesthetic, microscopic view of hair root, 4k",
    "10_전립선비대증": "Professional medical illustration of prostate gland anatomy and urinary health, clean 3D rendering, blue medical tones, educational style, 4k",
    "11_아연": "Hyper-realistic 3D rendering of zinc mineral supplement and immune system cells, professional medical illustration, metallic zinc element, 4k",
    "12_수근관증후군": "Medical illustration of carpal tunnel syndrome and wrist anatomy, professional 3D rendering, nerve highlighted in yellow, clean background, 4k",
    "13_비타민D": "Professional 3D illustration of vitamin D and bone health with sunlight rays, clean medical aesthetic, golden sunshine, skeletal structure, 4k",
    "14_안구건조증": "Medical illustration of dry eye syndrome and tear gland anatomy, professional 3D rendering, clean background, blue eye cross section, 4k",
    "15_통풍": "Professional 3D illustration of gout joint inflammation and uric acid crystals, clean medical aesthetic, swollen toe joint, crystal deposits, 4k",
    "16_마카": "Medical illustration of maca root plant and Peruvian ginseng, professional 3D rendering, clean background, natural earth tones, root cross section, 4k",
    "17_당뇨": "Professional 3D illustration of diabetes blood glucose monitoring and pancreas anatomy, clean medical aesthetic, insulin molecule, 4k",
    "18_대상포진": "Medical illustration of shingles herpes zoster virus structure, professional 3D rendering, virus particles, nerve pathway, clean background, 4k",
    "19_마그네슘": "Hyper-realistic 3D rendering of magnesium mineral and muscle nerve health, professional medical illustration, electrolyte balance, 4k",
    "20_물2리터": "Clean medical illustration of water drinking and hydration health, beautiful glass of crystal clear water, water droplets, professional aesthetic, 4k",
    "21_은행잎": "Professional 3D illustration of ginkgo biloba leaf and brain blood circulation, clean medical aesthetic, green leaf with golden veins, brain anatomy, 4k",
    "22_식후커피": "Medical illustration of stomach organ and coffee cup, digestive system warning concept, professional 3D rendering, clean background, 4k",
}

# 공통 네거티브 프롬프트 (이상한 결과물 방지)
negative_prompt = "text, watermark, logo, words, letters, blurry, low quality, deformed, ugly, bad anatomy, disfigured, poorly drawn, extra limbs, mutation, nsfw, cartoon, anime"

# ── 4단계: 이미지 일괄 생성 ──
output_dir = "/kaggle/working/blog_images"
os.makedirs(output_dir, exist_ok=True)

print(f"\n🎨 22개 이미지 생성 시작!\n{'='*50}")

for idx, (filename, prompt) in enumerate(prompts.items(), 1):
    print(f"\n[{idx}/22] 생성 중: {filename}")
    print(f"   프롬프트: {prompt[:60]}...")
    
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=1024,
        height=768,
        num_inference_steps=30,
        guidance_scale=7.5,
        generator=torch.Generator("cuda").manual_seed(42 + idx)
    ).images[0]
    
    save_path = f"{output_dir}/{filename}.png"
    image.save(save_path)
    print(f"   ✅ 저장 완료: {save_path}")

print(f"\n{'='*50}")
print(f"🏆 22개 이미지 모두 생성 완료!")
print(f"📂 저장 위치: {output_dir}")
print(f"\n💡 다운로드 방법: 오른쪽 'Output' 탭 → 'blog_images' 폴더 → 다운로드")

# ── 5단계: 생성된 이미지 미리보기 ──
from IPython.display import display, Image as IPImage
import glob

print("\n📸 생성된 이미지 미리보기:")
for img_path in sorted(glob.glob(f"{output_dir}/*.png"))[:5]:
    print(f"\n{os.path.basename(img_path)}:")
    display(IPImage(filename=img_path, width=400))
