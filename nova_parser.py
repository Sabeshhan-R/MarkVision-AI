import boto3
import json
import base64

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

def parse_marksheet(image_bytes, media_type="image/jpeg"):

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """
Analyze this marksheet image of a student.

Tasks:
1. Detect which board it belongs to (e.g., CBSE, Tamil Nadu State Board, etc.)
2. Extract the student's full name.
3. Extract all subjects and their respective marks.
4. Extract the total/grand total marks.

CRITICAL: Return ONLY a valid JSON object. No preamble, no explanation, no markdown outside the JSON block.

Format:
{
 "board": "Board Name",
 "name": "Student Name",
 "subjects": {
    "Subject1": "Mark1",
    "Subject2": "Mark2"
 },
 "total": "Total Marks"
}
"""

    body = {
        "messages":[
            {
                "role":"user",
                "content":[
                    {"text": prompt},
                    {
                        "image": {
                            "format": media_type.split("/")[-1] if "/" in media_type else media_type,
                            "source": {
                                "bytes": image_base64
                            }
                        }
                    }
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 2000
        }
    }

    response = bedrock.invoke_model(
        modelId="us.amazon.nova-2-lite-v1:0",
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    
    # Extract the text from the Nova response structure
    try:
        text = response_body["output"]["message"]["content"][0]["text"]
        
        # Robust JSON extraction (handles markdown blocks)
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
            
        return json.loads(text)
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
        return {
            "board": "Unknown",
            "name": "Error Parsing",
            "subjects": {},
            "total": "0"
        }