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
    print(f"{color} Flags: {formatted_keyword_list}")

def print_score_summary(green_list, red_list):
    green_score = len(green_list) 
    red_score = len(red_list)
    total_score = green_score - red_score ## For now I am using a straight 1-1 scoring system. Later iterations will give weighting and even include "deal-breakers"
    print(f"Green Flags: {green_score}\nRed Flags: {red_score}\nFinal Score: {total_score}")

def main(): 
    job_text = input("Please enter job text here:").lower()
    green_flags_set = get_green_flags(job_text, green_flags)
    red_flags_list = get_red_flags(job_text, red_flags)

    print("\n\n----------RESULT----------")
    format_keywords("Green", green_flags_set)
    format_keywords("Red", red_flags_list)
    print_score_summary(green_flags_set, red_flags_list)


main()
