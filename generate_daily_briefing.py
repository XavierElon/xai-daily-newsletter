import os
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
from pathlib import Path

from xai_sdk import Client
from xai_sdk.chat import system, user
from xai_sdk.search import SearchParameters, news_source, web_source

load_dotenv()

def generate_daily_briefing(client: Client, briefing_date: date):
    """
    Generate a daily briefing for the given date using Grok 4 with live search.
    """
    # Calculate the previous day for news gathering
    previous_day = briefing_date - timedelta(days=1)
    
    prompt = f"""
    You are Grok built by xAI. Generate a tech presidential briefing for {briefing_date}.
    
    CRITICAL DATE REQUIREMENT: This is a DAILY briefing. Focus on the BIGGEST tech stories from {previous_day} (yesterday).
    Use ONLY news from {previous_day} - the previous day.
    DO NOT use news from earlier dates or previous years.
    
    LIVE SEARCH INSTRUCTIONS:
    - Search for: "AI news {previous_day}", "Silicon Valley tech {previous_day}", "tech acquisitions {previous_day}", "AI breakthroughs {previous_day}", "big tech news {previous_day}"
    - Look for articles published specifically on {previous_day}
    - Focus on AI breakthroughs, major acquisitions, Silicon Valley developments, and big tech news
    - If you can't find enough major stories from {previous_day}, use the most important tech news from the past 2-3 days
    
    Structure your response as follows:
    
    ## Must Know: Key Stories
    - 8-10 MAJOR tech stories from {previous_day} with real headlines and summaries
    - Focus on: AI breakthroughs, major acquisitions, Silicon Valley developments, big tech news
    - Include actual news sources and links
    - Each story must have a title that links to the source
    - These should be the biggest tech stories from yesterday
    
    ## Good to Know: Trends and Tools
    - Bullet points on emerging AI trends, new tools, and industry developments from {previous_day}
    - Include specific company names and real developments
    - Focus on Silicon Valley ecosystem and major tech players
    
    ## Bullshit Police: Overhyped Claims
    - Critique overhyped or misleading tech claims from {previous_day}
    - Call out marketing fluff vs. real innovation
    - Focus on AI hype vs. real breakthroughs
    
    Requirements:
    - Use ONLY real news from {previous_day} (yesterday)
    - Include actual URLs and news sources
    - Keep it engaging, factual, and under 1000 words
    - NO simulated or fictional content
    - NO disclaimers about being simulated
    - Make it a hacker briefing with a tech/hacker tone
    - Focus on AI breakthroughs, Silicon Valley news, and major tech developments from yesterday
    """
    
    try:
        # Set up search parameters with date filtering for previous day
        from_date = datetime(previous_day.year, previous_day.month, previous_day.day)
        to_date = datetime(previous_day.year, previous_day.month, previous_day.day)
        
        search_params = SearchParameters(
            mode="on",  # Force search to be enabled
            from_date=from_date,
            to_date=to_date,
            return_citations=True,
            max_search_results=20,  # Increased for more AI/tech stories
            sources=[
                news_source(country="US"),  # Focus on US tech news
                web_source(country="US")
            ]
        )
        
        chat = client.chat.create(
            model='grok-4-0709', 
            temperature=0.7,
            search_parameters=search_params
        )
        chat.append(system("You are a helpful AI for tech news summaries. Focus on the biggest AI breakthroughs, Silicon Valley developments, and major tech acquisitions from the previous day. Never use news from previous years."))
        chat.append(user(prompt))
        
        response = chat.sample()
        briefing = response.content
        
        # Print citations for debugging
        if hasattr(response, 'citations') and response.citations:
            print(f"Sources used: {response.citations}")
        
        print(f"Generated briefing for {briefing_date} (news from {previous_day})")
        
        # Create directory structure: briefings/MM-YYYY/
        month_year = briefing_date.strftime("%m-%Y")
        briefings_dir = Path("briefings") / month_year
        
        # Create directory if it doesn't exist
        briefings_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filename with date
        date_str = briefing_date.strftime("%Y-%m-%d")
        filename = briefings_dir / f"briefing_tech_briefing_{date_str}.md"
        
        # Save the briefing
        with open(filename, "w") as f:
            f.write(briefing)
        print(f"Briefing saved to {filename}")
        
    except Exception as e:
        print(f"Error generating briefing: {e}")
        raise

if __name__ == "__main__":
    # Check if API key is available
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        print("Error: XAI_API_KEY environment variable not found!")
        print("Please set your XAI_API_KEY in the .env file")
        exit(1)
    
    client = Client(api_key=api_key)
    generate_daily_briefing(client, date.today())