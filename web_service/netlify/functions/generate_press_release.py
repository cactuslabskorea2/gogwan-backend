import json
from google import genai

def handler(event, context):
    """보도자료 생성 함수"""

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
        user_prompt = body.get('prompt')
        reference_content = body.get('reference_content')

        if not user_prompt:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': '프롬프트가 필요합니다'})
            }

        GEMINI_API_KEY = "AIzaSyD6_hNN5EyO_-OSmDrx3aFJzDwZ9xKMkTE"
        client = genai.Client(api_key=GEMINI_API_KEY)

        full_prompt = '당신은 대한민국 정부기관의 전문 보도자료 작성자입니다.\n공식적이고 명확하며, 객관적인 톤으로 작성해주세요.\n\n'

        if reference_content:
            full_prompt += f'다음은 참고할 기존 보도자료입니다:\n\n{reference_content}\n\n위 보도자료의 스타일과 구조를 참고하여 작성해주세요.\n\n'

        full_prompt += f'''사용자 요청사항:
{user_prompt}

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
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': 'Gemini API가 빈 응답을 반환했습니다'})
            }

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'success': True, 'content': text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': f'처리 중 오류 발생: {str(e)}'})
        }
