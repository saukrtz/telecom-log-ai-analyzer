import requests
import json
import os

def analyze_logs(log_file, api_key):
    """
    Analyzes logs using Groq's Llama 3.1 8b model.
    """
    with open(log_file, 'r') as f:
        logs = f.read()

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Analyze the following production logs for a Telecom Monitoring system.
    Identify:
    - Root cause
    - Severity
    - Recommended remediation

    Logs:
    {logs}

    Please provide a structured response.
    """

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a senior SRE and Data Engineer specialized in telecom infrastructure."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Error during AI analysis: {str(e)}"

if __name__ == "__main__":
    # In a real scenario, we'd load from .env, but for this script we can pass it or read it directly
    # Since I know where it is, I'll read it.
    env_path = "/Users/as-mac-1224/Documents/genai/data_pipeline/gen_ai/day5/.env"
    api_key = None
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.startswith("GROQ_API_KEY="):
                    api_key = line.split("=")[1].strip()
    
    if api_key:
        analysis = analyze_logs("app.log", api_key)
        with open("analysis_report.md", "w") as f:
            f.write("# AI Log Analysis Report\n\n")
            f.write(analysis)
        print("Analysis completed. Results saved to analysis_report.md")
    else:
        print("API Key not found.")
