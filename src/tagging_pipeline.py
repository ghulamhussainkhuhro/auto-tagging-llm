# src/tagging_pipeline.py

import os
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Define the 8 support categories (static for now)
SUPPORT_TAGS = [
    "Billing Issue",
    "Technical Problem",
    "Account Access",
    "Feature Request",
    "General Inquiry",
    "Bug Report",
    "Refund Request",
    "Subscription Management"
]

def load_support_tickets(filepath="data/support_tickets.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        tickets = json.load(file)
    return tickets

from langchain_openai import AzureChatOpenAI

# Initialize Azure OpenAI Chat model
llm = AzureChatOpenAI(
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0.2,
    model_kwargs={"top_p": 1}
)

def build_zero_shot_prompt(ticket_message: str, tag_options: list) -> str:
    """
    Build a zero-shot prompt asking the model to classify a message using top 3 tags.
    """
    tag_list = ", ".join(tag_options)
    prompt = (
        f"You are an AI assistant that classifies customer support tickets into relevant categories.\n"
        f"Choose the top 3 categories (from the list below) that best describe the following message.\n\n"
        f"Support Message:\n\"{ticket_message}\"\n\n"
        f"Available Categories:\n{tag_list}\n\n"
        f"Respond with a JSON array of 3 category names only."
    )
    return prompt

def get_top_3_tags(ticket_message: str) -> list:
    """
    Send a prompt to the LLM and parse its response to return top 3 tags.
    """
    prompt = build_zero_shot_prompt(ticket_message, SUPPORT_TAGS)
    response = llm.invoke(prompt)
    try:
        tags = json.loads(response.content)
        if isinstance(tags, list) and all(tag in SUPPORT_TAGS for tag in tags):
            return tags
        else:
            print(f"⚠️ Unexpected format or invalid tags: {tags}")
            return []
    except Exception as e:
        print(f"❌ Error parsing response: {e}")
        print(f"Response was: {response.content}")
        return []

def tag_all_tickets(input_path="data/support_tickets.json", output_path="results/tagged_tickets.json"):
    tickets = load_support_tickets(input_path)
    tagged_results = []

    for ticket in tickets:
        print(f"🔍 Tagging ticket ID {ticket['id']}")
        tags = get_top_3_tags(ticket["message"])
        tagged_results.append({
            "id": ticket["id"],
            "message": ticket["message"],
            "tags": tags
        })

    # Save results
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(tagged_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Tagged tickets saved to {output_path}")
