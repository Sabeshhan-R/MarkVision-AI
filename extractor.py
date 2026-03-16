import boto3

textract = boto3.client("textract")

def extract_text(file_bytes):
    response = textract.detect_document_text(
        Document={"Bytes": file_bytes}
    )

    text = ""

    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            text += block["Text"] + "\n"

    return text