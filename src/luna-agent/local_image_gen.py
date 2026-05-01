import os
import time

def generate_local_image(prompt, output_dir="docs/intelligence/shorts/media"):
    """
    [V12 사내 아트 디렉터]
    로컬 Stable Diffusion(Flux 등) 모델을 사용하여 외부 API 비용 없이 이미지를 생성합니다.
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = f"broll_{int(time.time())}.jpg"
    output_path = os.path.join(output_dir, filename)
    
    print(f"🎨 [Image Gen] 프롬프트로 로컬 이미지 생성 중... '{prompt}'")
    
    try:
        # 실제 환경에서는 아래 주석을 풀고 diffusers 파이프라인을 사용합니다.
        # import torch
        # from diffusers import StableDiffusionXLPipeline
        # pipe = StableDiffusionXLPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16)
        # pipe = pipe.to("cuda")
        # image = pipe(prompt).images[0]
        # image.save(output_path)
        
        # 임시 플레이스홀더 로직 (GPU/설정 전까지 안전하게 동작하기 위함)
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (1080, 1920), color = (40, 40, 40))
        d = ImageDraw.Draw(img)
        d.text((100, 960), f"AI Gen: {prompt[:30]}...", fill=(255,255,255))
        img.save(output_path)
        
        print(f"✅ [Image Gen] 이미지 렌더링 완료: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"❌ [Image Gen] 로컬 이미지 생성 실패: {e}")
        return None

if __name__ == "__main__":
    generate_local_image("A futuristic bitcoin whale diving into the ocean of digital charts")
