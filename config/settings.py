import os
from dotenv import load_dotenv
# from pathlib import Path

# Load stored env variables
load_dotenv()

class Settings:
    # Main Settings
    PROJECT_NAME = "JobIntel"
    VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    # Slack Settings
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

    # Gmail Settings
    GMAIL_CREDENTIALS_FILE = os.getenv("GMAIL_CREDENTIALS_FILE")
    GMAIL_TOKEN_FILE = os.getenv("GMAIL_TOKEN_FILE")

    # OpenAi Settings
    OPEN_API_KEY = os.getenv("OPEN_API_KEY")

    # Database Settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/jobintel.db")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate_settings(cls):
        """
        Validate all settings are set
        """
        required = [
            'SLACK_BOT_TOKEN',
            'OPENAI_API_KEY'
        ]

        not_found: list[str] = []

        for setting in required:
            if not getattr(cls, setting):
                not_found.append(setting)

        if not_found:
            raise ValueError(f"Missing required settings: {', '.join(not_found)}")
                
settings = Settings()

if __name__ == "__main__":
    try:
        settings.validate_settings()
        print("All required settings are present!")
    except ValueError as e:
        print(f"Configuration error: {e}")

