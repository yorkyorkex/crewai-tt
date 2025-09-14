from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from .gmail_utility import authenticate_gmail, create_message, create_draft
import os

class GmailToolInput(BaseModel):
    """Input schema for GmailTool."""

    body: str = Field(..., description="The body of the email.")


class GmailTool(BaseTool):
    name: str = "Gmail Tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = GmailToolInput

    def _run(self, body: str) -> str:
        try:
            service = authenticate_gmail()

            sender = "n11453559@gmail.com"
            to = "yorkyuex@gmail.com"
            subject = "Meeting Minutes"
            message_text = body

            message = create_message(sender, to, subject, message_text)
            draft = create_draft(service, "me", message)

            return f"Email sent successfully! Draft id: {draft['id']}"
        except Exception as e:
            return f"Error sending email: {e}"
