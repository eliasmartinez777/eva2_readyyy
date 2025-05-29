import os
import logging
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from config import GMAIL_CREDENTIALS_PATH, SCOPES, TOKEN_PATH, SENDER_EMAIL

class EmailService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.service = self._authenticate()

    def _authenticate(self):
        creds = None
        if os.path.exists(TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    GMAIL_CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open(TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())
        
        return build('gmail', 'v1', credentials=creds)

    def send_email(self, subject, body, to_email):
        try:
            from email.mime.text import MIMEText
            import base64
            
            message = MIMEText(body)
            message['to'] = to_email
            message['from'] = SENDER_EMAIL
            message['subject'] = subject
            
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            
            self.service.users().messages().send(
                userId="me",
                body={'raw': encoded_message}
            ).execute()
            
            self.logger.info(f"Email enviado a {to_email}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error enviando email: {str(e)}")
            return False