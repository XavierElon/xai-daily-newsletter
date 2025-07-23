import logging
from datetime import date
from email_sender import EmailSender
from generate_daily_briefing import generate_daily_briefing
from xai_sdk import Client
import os
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/xxx/Documents/coding/xai-daily-newsletter/service.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()

def daily_task():
    """Generate briefing and send email."""
    logging.info(f"Starting daily task for {date.today()}")
    
    try:
        # Generate the briefing
        client = Client(api_key=os.getenv("XAI_API_KEY"))
        generate_daily_briefing(client, date.today())
        
        # Send the email
        sender = EmailSender()
        sender.send_briefing_email()
        
        logging.info("Daily task completed successfully!")
        
    except Exception as e:
        logging.error(f"Error in daily task: {e}")
        raise  # Re-raise to indicate failure

def main():
    logging.info("Daily briefing service started")
    
    # Run the task once and exit
    daily_task()
    
    logging.info("Task completed successfully")

if __name__ == "__main__":
    main()