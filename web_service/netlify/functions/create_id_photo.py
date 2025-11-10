import json
import base64
import os
from google import genai
from google.genai import types

def handler(event, context):
    """증명사진 생성 함수 - Gemini 2.5 Flash Image"""

    # CORS 헤더
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }

    # OPTIONS 요청 처리
    if event['httpMethod'] == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers, 'body': ''}

    try:
        body = json.loads(event['body'])
        image_data = body.get('image')
        background_color = body.get('background_color', 'white')

        if not image_data:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': '이미지 데이터가 필요합니다'})
            }

        # Gemini API 클라이언트 생성
        GEMINI_API_KEY = "AIzaSyD6_hNN5EyO_-OSmDrx3aFJzDwZ9xKMkTE"
        client = genai.Client(api_key=GEMINI_API_KEY)

        # 프롬프트
        prompt = f"""Edit this photo to create a professional ID/passport photo:

1. Remove the background completely and replace it with a solid {background_color} color
2. Center the person's face in the frame
3. Crop to standard ID photo ratio (3:4)
4. Adjust lighting to be natural and even
5. Enhance quality to professional ID photo standards

Create a high-quality ID photo suitable for passports or identification documents."""

        # Base64 디코딩
        image_bytes = base64.b64decode(image_data)

        # Gemini 2.5 Flash Image로 이미지 생성
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[
                prompt,
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
            ],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio="3:4")
            )
        )

        # 생성된 이미지 추출
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                result_image_base64 = base64.b64encode(part.inline_data.data).decode('utf-8')

                return {
                    'statusCode': 200,
                    'headers': headers,
                    'body': json.dumps({
                        'success': True,
                        'message': '증명사진이 생성되었습니다',
                        'processed_image': result_image_base64
                    })
                }

        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': '이미지 생성에 실패했습니다'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': f'처리 중 오류 발생: {str(e)}'})
        }
