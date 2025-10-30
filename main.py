from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import os
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig, Part, Modality

app = FastAPI(title="GOGWAN API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Vertex AI 클라이언트 (나노바나나 사용)
# 환경 변수에서 JSON 읽기 (Railway용) 또는 로컬 파일 사용
if os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON'):
    import json
    import tempfile
    # 환경 변수에서 JSON 읽어서 임시 파일 생성
    creds_json = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON'))
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(creds_json, f)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f.name
else:
    # 로컬 파일 사용
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
        os.path.dirname(__file__),
        'gogwan-4902b9a702be.json'
    )

client = genai.Client(
    vertexai=True,
    project='gogwan',
    location='global'
)


class IdPhotoRequest(BaseModel):
    image: str
    background_color: str = "white"


class GhibliRequest(BaseModel):
    image: str


class PressReleaseRequest(BaseModel):
    prompt: str
    reference_content: str = None


@app.get("/")
def read_root():
    return {"message": "GOGWAN API Server", "status": "running"}


@app.post("/api/create-id-photo")
async def create_id_photo(request: IdPhotoRequest):
    """증명사진 생성 - Gemini 2.5 Flash Image"""
    try:
        # Base64 디코딩
        image_bytes = base64.b64decode(request.image)

        # 프롬프트 생성
        prompt = f"""Edit this photo to create a professional ID/passport photo:

1. Remove the background completely and replace it with a solid {request.background_color} color
2. Center the person's face in the frame
3. Crop to standard ID photo ratio (3:4)
4. Adjust lighting to be natural and even
5. Enhance quality to professional ID photo standards

Create a high-quality ID photo suitable for passports or identification documents."""

        # Gemini 2.5 Flash Image (나노바나나)로 이미지 생성
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[
                prompt,
                Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
            ],
            config=GenerateContentConfig(
                response_modalities=[Modality.TEXT, Modality.IMAGE]
            )
        )

        # 생성된 이미지 추출
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                result_image_base64 = base64.b64encode(part.inline_data.data).decode('utf-8')
                return {
                    "success": True,
                    "message": "증명사진이 생성되었습니다",
                    "processed_image": result_image_base64
                }

        raise HTTPException(status_code=500, detail="이미지 생성에 실패했습니다")

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"처리 중 오류 발생: {str(e)}")


@app.post("/api/convert-to-ghibli")
async def convert_to_ghibli(request: GhibliRequest):
    """지브리풍 변환 - Gemini 2.5 Flash Image"""
    try:
        image_bytes = base64.b64decode(request.image)

        prompt = """Transform this photo into a Studio Ghibli animation style:

Style characteristics:
1. Soft, warm watercolor-like colors
2. Clear, defined anime outlines
3. Dreamy, fantasy Ghibli atmosphere
4. Detailed background with natural lighting
5. Similar to Spirited Away or Howl's Moving Castle

Keep the original composition and pose, but make it look exactly like a scene from a Ghibli animation movie."""

        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[
                prompt,
                Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
            ],
            config=GenerateContentConfig(
                response_modalities=[Modality.TEXT, Modality.IMAGE]
            )
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                result_image_base64 = base64.b64encode(part.inline_data.data).decode('utf-8')
                return {
                    "success": True,
                    "message": "지브리풍 이미지가 생성되었습니다",
                    "processed_image": result_image_base64
                }

        raise HTTPException(status_code=500, detail="이미지 생성에 실패했습니다")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"처리 중 오류 발생: {str(e)}")


@app.post("/api/generate-press-release")
async def generate_press_release(request: PressReleaseRequest):
    """보도자료 생성"""
    try:
        full_prompt = '당신은 대한민국 정부기관의 전문 보도자료 작성자입니다.\n공식적이고 명확하며, 객관적인 톤으로 작성해주세요.\n\n'

        if request.reference_content:
            full_prompt += f'다음은 참고할 기존 보도자료입니다:\n\n{request.reference_content}\n\n위 보도자료의 스타일과 구조를 참고하여 작성해주세요.\n\n'

        full_prompt += f'''사용자 요청사항:
{request.prompt}

다음 구조로 대한민국 정부기관 공식 보도자료 형식에 맞춰 작성해주세요:

【제목】
간결하고 핵심을 담은 한 줄 제목

【부제】
제목을 보완하는 설명 (2줄 이내)

【본문】
본문은 자연스러운 문장으로 작성하되, 다음 구조를 따르세요:

□ 도입부
  ○ 정책/사업의 배경과 목적을 간단히 설명

□ 핵심 내용
  ○ 지원 대상, 금액, 기간, 방법 등 주요 정보 포함
  ○ 숫자나 통계는 구체적으로 표기

□ 향후 계획 및 기대효과
  ○ 기대효과와 향후 계획을 명시

작성 규칙:
- □와 ○ 기호만 사용하고, 그 뒤에 바로 내용을 작성하세요
- 각 문단은 자연스러운 문장으로 구성
- 공식적이고 전문적인 톤을 유지

보도자료는 반드시 한국어로 작성하며, 【제목】【부제】【본문】 구조를 명확히 지켜주세요.'''

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=full_prompt
        )

        text = response.text

        if not text:
            raise HTTPException(status_code=500, detail="Gemini API가 빈 응답을 반환했습니다")

        return {"success": True, "content": text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"처리 중 오류 발생: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
