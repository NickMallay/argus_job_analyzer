## first pass will be super simple. 
# Just take a pasted job posting, parse the text, 
# keyword match, determine a score, return the score. 
# Multiple job postings, llm intergreation for dynamic reccos, etc
# will all be done as future iteration. 
# The point today is to get this real, so its easier to work on. 

##Get job text
##format and list job text as list
##compare job text list to personal profile / criteria
##return score

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
    

def get_job_text():
    print("Please input job text now:")
    job_text = input()
    return job_text

def get_formatted_job_list(job_text):
    formatted_job_list = job_text.lower().split()
    return formatted_job_list