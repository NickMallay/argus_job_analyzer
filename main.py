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
    


##Output number of green flags
def determine_green_flags(job_text, green_flags_list):
    green_flags_set = set() ## I want each keyword to count only once, so i am using a set rather than a list
    job_keyword_list = job_text.lower().split(" ")
    for word in job_keyword_list:
        if word in green_flags_list:
            green_flags_set.add(word)
    return green_flags_set

def determine_red_flags(job_text, red_flags_criteria):
    ##Take the jobtext, keep it as a string, interate through each red flag phrase and check for it in the job text string
    red_flag_list = []
    for red_flag in red_flags_criteria:
        if red_flag in job_text:
            red_flag_list.append(red_flag)
    return red_flag_list

def format_keywords(color, flag_list):
    formatted_keyword_list = ", ".join(list(flag_list)) + "."
    print(f"{color} Flags: {formatted_keyword_list}")

def get_score_string(flag_list):
    score = len(flag_list)
    return f"Score: {score}"

def main(): ## a mock structure to test the determine_green_flags function
    job_text = input("Please enter job text here:")
    green_flags_set = determine_green_flags(job_text, green_flags)
    
    format_keywords("Green", green_flags_set)
    print(get_score_string(green_flags_set))

main()
