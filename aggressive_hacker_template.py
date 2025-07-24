def create_aggressive_hacker_html(briefing_content: str, date: str) -> str:
    """Create an aggressive hacker-style HTML email template."""
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HACKER BRIEFING - {date}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
            
            body {{
                font-family: 'Orbitron', monospace;
                background: #000;
                color: #0f0;
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }}
            
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background: linear-gradient(45deg, #000, #111);
                border: 3px solid #0f0;
                position: relative;
                overflow: hidden;
            }}
            
            .container::before {{
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(0,255,0,0.1), transparent);
                animation: scan 3s infinite;
            }}
            
            @keyframes scan {{
                0% {{ left: -100%; }}
                100% {{ left: 100%; }}
            }}
            
            .header {{
                background: linear-gradient(90deg, #000, #0a0a0a, #000);
                padding: 30px;
                text-align: center;
                border-bottom: 2px solid #0f0;
                position: relative;
            }}
            
            .title {{
                font-size: 3em;
                font-weight: 900;
                color: #0f0;
                text-shadow: 0 0 20px #0f0, 0 0 40px #0f0;
                margin: 0;
                letter-spacing: 5px;
                animation: glow 2s ease-in-out infinite alternate;
            }}
            
            @keyframes glow {{
                from {{ text-shadow: 0 0 20px #0f0, 0 0 40px #0f0; }}
                to {{ text-shadow: 0 0 30px #0f0, 0 0 60px #0f0, 0 0 80px #0f0; }}
            }}
            
            .subtitle {{
                font-size: 1.2em;
                color: #0a0;
                margin: 10px 0;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            
            .date {{
                font-size: 1em;
                color: #050;
                margin: 5px 0;
                font-weight: bold;
            }}
            
            .content {{
                padding: 30px;
                background: rgba(0, 20, 0, 0.3);
                position: relative;
            }}
            
            .content::before {{
                content: '> ';
                color: #0f0;
                font-weight: bold;
                position: absolute;
                left: 10px;
                top: 30px;
            }}
            
            .section {{
                margin-bottom: 25px;
                border-left: 3px solid #0f0;
                padding-left: 20px;
                background: rgba(0, 10, 0, 0.2);
                padding: 15px;
                margin: 15px 0;
            }}
            
            .section-title {{
                font-size: 1.4em;
                font-weight: 700;
                color: #0f0;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-bottom: 15px;
                text-shadow: 0 0 10px #0f0;
            }}
            
            .section-content {{
                color: #0a0;
                line-height: 1.8;
                font-size: 0.95em;
            }}
            
            .footer {{
                background: linear-gradient(90deg, #000, #0a0a0a, #000);
                padding: 20px;
                text-align: center;
                border-top: 2px solid #0f0;
            }}
            
            .terminal {{
                background: #000;
                border: 2px solid #0f0;
                padding: 15px;
                margin: 10px 0;
                font-family: 'Courier New', monospace;
                color: #0f0;
                position: relative;
            }}
            
            .terminal::before {{
                content: 'root@system:~$ ';
                color: #0a0;
                font-weight: bold;
            }}
            
            .highlight {{
                color: #ff0;
                font-weight: bold;
                text-shadow: 0 0 5px #ff0;
            }}
            
            .warning {{
                color: #f60;
                font-weight: bold;
                text-shadow: 0 0 5px #f60;
            }}
            
            .success {{
                color: #0f0;
                font-weight: bold;
                text-shadow: 0 0 5px #0f0;
            }}
            
            .info {{
                color: #09f;
                font-weight: bold;
                text-shadow: 0 0 5px #09f;
            }}
            
            .matrix-bg {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent 98%, #0f0 100%);
                background-size: 20px 20px;
                opacity: 0.1;
                z-index: -1;
                animation: matrix-fall 10s linear infinite;
            }}
            
            @keyframes matrix-fall {{
                0% {{ transform: translateY(-100%); }}
                100% {{ transform: translateY(100%); }}
            }}
            
            /* Additional styles for markdown content */
            .content h1, .content h2, .content h3, .content h4, .content h5, .content h6 {{
                color: #0f0;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 10px;
                text-shadow: 0 0 5px #0f0;
            }}
            
            .content h1 {{ font-size: 1.8em; }}
            .content h2 {{ font-size: 1.5em; }}
            .content h3 {{ font-size: 1.3em; }}
            
            .content p {{
                margin-bottom: 15px;
                line-height: 1.6;
                color: #0a0;
            }}
            
            .content ul, .content ol {{
                margin-left: 20px;
                margin-bottom: 15px;
                color: #0a0;
            }}
            
            .content li {{
                margin-bottom: 5px;
                color: #0a0;
            }}
            
            .content strong {{
                color: #ff0;
                font-weight: bold;
            }}
            
            .content em {{
                color: #09f;
                font-style: italic;
            }}
            
            .content a {{
                color: #0f0;
                text-decoration: underline;
            }}
            
            .content a:hover {{
                color: #ff0;
            }}
            
            .content blockquote {{
                border-left: 3px solid #0f0;
                padding-left: 15px;
                margin: 15px 0;
                color: #0a0;
            }}
            
            .content code {{
                background: #000;
                color: #0f0;
                padding: 2px 5px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            
            .content pre {{
                background: #000;
                color: #0f0;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
                border: 1px solid #0f0;
            }}
        </style>
    </head>
    <body>
        <div class="matrix-bg"></div>
        <div class="container">
            <div class="header">
                <h1 class="title">HACKER BRIEFING</h1>
                <p class="subtitle">SYSTEM INTELLIGENCE REPORT</p>
                <p class="date">{date}</p>
            </div>
            
            <div class="content">
                {briefing_content}
            </div>
            
            <div class="footer">
                <div class="terminal">
                    <span class="success">[OK]</span> Transmission complete | 
                    <span class="info">[INFO]</span> AI-powered analysis | 
                    <span class="highlight">[SECURE]</span> Encrypted channel
                </div>
                <p style="margin-top: 15px; color: #050; font-size: 0.9em;">
                    🔒 SECURE TRANSMISSION | ⚡ REAL-TIME DATA | 🚀 AI-POWERED INSIGHTS
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_template