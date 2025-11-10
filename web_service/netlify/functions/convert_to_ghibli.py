import json
import base64
from google import genai
from google.genai import types

def handler(event, context):
    """지브리풍 변환 함수 - Gemini 2.5 Flash Image"""

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }

    if event['httpMethod'] == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers, 'body': ''}

    try:
        body = json.loads(event['body'])
        image_data = body.get('image')

        if not image_data:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': '이미지 데이터가 필요합니다'})
            }

        GEMINI_API_KEY = "AIzaSyD6_hNN5EyO_-OSmDrx3aFJzDwZ9xKMkTE"
        client = genai.Client(api_key=GEMINI_API_KEY)

        prompt = """Transform this photo into a Studio Ghibli animation style:

Style characteristics:
1. Soft, warm watercolor-like colors
2. Clear, defined anime outlines
3. Dreamy, fantasy Ghibli atmosphere
4. Detailed background with natural lighting
5. Similar to Spirited Away or Howl's Moving Castle

Keep the original composition and pose, but make it look exactly like a scene from a Ghibli animation movie."""

        image_bytes = base64.b64decode(image_data)

        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[
                prompt,
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
            ],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"]
            )
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                result_image_base64 = base64.b64encode(part.inline_data.data).decode('utf-8')

                return {
                    'statusCode': 200,
                    'headers': headers,
                    'body': json.dumps({
                        'success': True,
                        'message': '지브리풍 이미지가 생성되었습니다',
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
