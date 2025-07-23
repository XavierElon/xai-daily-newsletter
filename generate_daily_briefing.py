import os
from datetime import date
from dotenv import load_dotenv
from pathlib import Path

from xai_sdk import Client
from xai_sdk.chat import system, user

load_dotenv()

def generate_daily_briefing(client: Client, today: date):
    """
    Generate a daily briefing for the given date.
    """
    prompt = f"""
    You are Grok built by xAI. Generate a tech presidential briefing for {today} containing all the news from yesterday.
    Use live search to gather the latest tech news from reliable sources.
    Structure:
    - Must know: 3-5 key stories with summaries.
    - Good to know: Bullet points on trends/tools.
    - Bullshit police: Critique overhyped claims.
    - Please make sure each bullet point/story has a title and that title is a link to the source.
    Keep it engaging, factual, and under 1000 words.
    """
    try:
        chat = client.chat.create(model='grok-3')
        chat.append(system("You are a helpful AI for tech news summaries."))
        chat.append(user(prompt))
        
        response = chat.sample()
        briefing = response.content
        print(response)
        
        month_year = today.strftime("%m-%Y")
        briefings_dir = Path("briefings") / month_year
        
        briefings_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = today.strftime("%Y-%m-%d")
        filename = briefings_dir / f"briefing_tech_briefing_{date_str}.md"
        
        with open(filename, "w") as f:
            f.write(briefing)
        print(f"Briefing saved to {filename}")
    except Exception as e:
        print(f"Error generating briefing: {e}")
        exit(1)

if __name__ == "__main__":
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        print("Error: XAI_API_KEY environment variable not found!")
        print("Please set your XAI_API_KEY in the .env file")
        exit(1)
        
    client = Client(api_key=os.getenv("XAI_API_KEY"))
    generate_daily_briefing(client, date.today())