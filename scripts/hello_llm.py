import os
import anthropic
from dotenv import load_dotenv

PROMPT = "What is 17 * 23? Reply with only the number."

load_dotenv()

print("=== ANTHROPIC ===")
claude = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
reply = claude.messages.create(
    model="claude-haiku-5-5",
    max_tokens=4096,
    messages=[{"role": "user", "content": "Explain the Ottoman Empire history."}],
)
print(reply.model_dump_json(indent=2))