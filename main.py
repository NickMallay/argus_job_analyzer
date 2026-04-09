##First pass is complete. 
# Next iterations will be to allow file access, mulutiple job postings, saving the output, and llm integration for a suitability summary
import glob
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

green_flags = [
    "qa",
    "quality",
    "manual",
    "testing",
    "tester",
    "python",
    "automation",
    "selenium",
    "api",
    "sql",
    "jira",
    "agile",
    "scrum",
    "remote",
    "flexible",
    "junior",
    "entry",
    "associate",
    "mentorship",
    "training",
    "learning",
    "accessibility",
    "inclusive",
    "autonomy",
    "documentation",
    "process",
    "user-focused",
    "quality-driven",
    "contract",
    ] 
red_flags = [
    "fast-paced",
    "fast paced",
    "fast-paced environment",
    "we are a family",
    "like a family",
    "wear many hats",
    "work under pressure",
    "high-pressure",
    "high pressure",
    "overtime",
    "after hours",
    "evenings and weekends",
    "weekends",
    "nights",
    "startup mentality",
    "move fast and break things",
    "work hard play hard",
    "rockstar",
    "ninja",
    "guru",
    "dynamic environment",
    "no two days are the same",
    "handle constant interruptions",
    "outgoing personality",
    "vibrant personality",
    "extroverted",
    ]
job_posting_folder_name = "job_posts"
personal_details_file_name = "personal_details.txt"

def get_green_flags(job_text, green_flags_list):
    green_flags_set = set() ## I want each keyword to count only once, so i am using a set rather than a list
    job_keyword_list = job_text.split(" ")
    for word in job_keyword_list:
        if word in green_flags_list:
            green_flags_set.add(word)
    return green_flags_set
def get_red_flags(job_text, red_flags_criteria):
    red_flag_matches = [] ## since each red_flag is checked against job_text only once, duplicates are impossible and so i've used a list here for simplicity
    for red_flag in red_flags_criteria:
        if red_flag in job_text:
            red_flag_matches.append(red_flag)
    return red_flag_matches
def format_keywords(color, flag_list):
    formatted_keyword_list = ", ".join(list(flag_list))
    if len(formatted_keyword_list) >= 1:
        formatted_keyword_list += "."
    return f"{color} Flags: {formatted_keyword_list}"
def get_posting_report(name, green, red, score, analysis):
    return f"Name: {name}\n{green}\n{red}\n{score}\n LLM Suitability Analysis:\n{analysis}\n" #Pull together formatted parts of the report
def get_score_summary(green_list, red_list):
    green_score = len(green_list) 
    red_score = len(red_list)
    total_score = green_score - red_score ## For now I am using a straight 1-1 scoring system. Later iterations will give weighting and even include "deal-breakers"
    return f"Green Flags: {green_score}\nRed Flags: {red_score}\nFinal Score: {total_score}\n"
def get_job_posts(job_posting_folder_name):
    job_posting_contents_dict = {}
    job_post_file_list = glob.glob(f"{job_posting_folder_name}/*.txt")
    for post in job_post_file_list:
        with open(post) as p:
            job_post_content = p.read()
            job_posting_contents_dict[post] = job_post_content
    print(job_posting_contents_dict)
    return job_posting_contents_dict
def get_personal_details(file_name):

    with open(file_name) as file:
        personal_details = file.read()
        return personal_details
def call_llm(prompt):
    responce = client.chat.completions.create(model = "gpt-5-nano", messages = [{"role": "user", "content": prompt}])
    return responce.choices[0].message.content
def get_llm_prompt(job_posting, personal_details):
    #Intro (What is the point of this call), job post, personal story and needs, request
    prompt = "Your job is to parse the given job posting and, using the given personal detials, determine the suitability of the job posting for the applicant. Your response will be in the form of 'Score: (score) Suitability Analysis - (suitability analysis)' using a score between 1-100. The suitability analysis should be between 3-5 sentences and address any noteworthy opportunities or concerns. The response will be used by the applicant to determine whether or not they should apply for a job in the hope of minimizing emotional and cognitive effort expended in the job hunt. Do not hallucinate details not in the posting. Base the score exclusively on the posting and the given details. Acknowledge any missing information. Keep the tone factual and neutral. End with a clear one sentence declaration if the user should apply, should not apply, or should apply with no expectations"
    return f"Job Posting:{job_posting}\nPersonal Details:{personal_details}\n{prompt}\n"

def main(): 
    job_posts = get_job_posts(job_posting_folder_name)
    report_list = []
    for job in job_posts:
        job_name = job
        job_content = job_posts[job]
        
        green_flags_set = get_green_flags(job_content, green_flags)
        red_flags_list = get_red_flags(job_content, red_flags)
        
        green_flag_report = format_keywords("Green", green_flags_set)
        red_flag_report = format_keywords("Red", red_flags_list)
        score = get_score_summary(green_flags_set, red_flags_list)
        analysis = call_llm(get_llm_prompt(job_posts[job], get_personal_details(personal_details_file_name)))
        job_report = get_posting_report(job_name, green_flag_report, red_flag_report, score, analysis)
        report_list.append(job_report)
    for report in report_list:
        print(report)



main()

