import openai
import config

client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def analyze_resume(resume_text, job_text):
    prompt = f"""
You are a helpful job-matching assistant. Compare the following resume and job description, and do the following:
1. Give a match score out of 100
2. Give 3–5 bullet-point reasons for the match score
3. Suggest at least 3 personalized improvements for the resume

Resume:
{resume_text}

Job Description:
{job_text}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    resume = load_file("resume.txt")
    job = load_file("job_description.txt")
    print("🤖 Analyzing match between resume and job posting...\n")
    result = analyze_resume(resume, job)
    print(result)
