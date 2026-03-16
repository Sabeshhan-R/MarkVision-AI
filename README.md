# 🎯 MarkVision AI - Marksheet Extractor

MarkVision AI is a Streamlit-powered web application that automates the extraction of student data from scanned marksheet images. It leverages the power of **Amazon Nova 2 Lite** via Amazon Bedrock for high-speed, cost-effective multimodal reasoning.

## 🚀 Features
- **Multimodal AI Extraction**: Automatically detects Board Name, Student Name, Subjects, Marks, and Total Marks using Amazon Nova.
- **Bulk Processing**: Upload multiple marksheet images (JPG, PNG) at once.
- **Excel Export**: Download all extracted data into a single, structured Excel file for easy record-keeping.
- **Clean UI**: Built with Streamlit for a smooth and intuitive user experience.

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: [Amazon Nova 2 Lite](https://aws.amazon.com/ai/generative-ai/nova/) (via Amazon Bedrock)
- **Data Handling**: [Pandas](https://pandas.pydata.org/)
- **Excel Engine**: [Openpyxl](https://openpyxl.readthedocs.io/)
- **Cloud SDK**: [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/nova-ai-hackathon.git
   cd nova-ai-hackathon
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS Credentials:**
   Ensure you have AWS credentials configured (via `aws configure`) with access to the `us-east-1` region and Amazon Bedrock Nova models.

## 🏃 Run the App
```bash
streamlit run app.py
```

## 📄 License
MIT License
