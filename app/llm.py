# Author: Rogelio "Roj" Padida Jr.
# LLM-based discount calculation via OpenAI

import os
import openai

# load LLM key
openai.api_key = os.getenv("LLM_API_KEY")

# Prompt template with explicit rules
_PROMPT = """
You are a discount calculator for a bowling shoe rental service. Use these rules: # noqa
- Age: 0-12: 20%, 13-18: 10%, 65+: 15%
- Disability status: disabled: 25%
- Medical conditions: diabetes: 10%, hypertension: 10%, chronic condition: 10%

Customer info:
Age: {age}
Is disabled: {is_disabled}
Medical conditions: {medical_conditions}

Return **only** the highest discount percentage as a plain number (e.g., 25). If none, return 0. # noqa
"""


async def get_discount(customer_data) -> float:
    """Call OpenAI to get discount percent."""
    prompt = _PROMPT.format(
        age=customer_data.age,
        is_disabled=customer_data.is_disabled,
        medical_conditions=", ".join(customer_data.medical_conditions) or "none" # noqa
    )
    # Roj’s debug log
    # print("Prompt to LLM:", prompt)
    resp = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=8
    )
    text = resp.choices[0].message.content.strip()
    # extract numeric
    try:
        return float(text.replace("%", ""))
    except:  # noqa
        return 0.0
