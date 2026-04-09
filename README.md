Argus Job Analyzer
Screens job postings for green and red flags and generates a suitability report using keyword scoring and LLM analysis. Built because job hunting is exhausting and I wanted a tool that would do the first pass for me.
How it works:
Drop job postings as .txt files into the job_posts folder, add your personal details to personal_details.txt, and run main.py. Argus will score each posting and generate an LLM summary with a clear apply/don't apply recommendation.
Current status: Working first pass. Next: file output, batch processing, ATS compliance checking.
Requires: Python, OpenAI API key set as environment variable.
