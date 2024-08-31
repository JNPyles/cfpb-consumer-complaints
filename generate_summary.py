!pip install groq

# Import Libraries
import os
from groq import Groq
import time
import pandas as pd

# Import data
data = pd.read_csv('complaints_with_narrative_sample_100_by_product.csv')

# Set up client 
client = Groq(api_key=[...])

# Method to get summary
def get_summary(complaint_narrative):
  time.sleep(1) # Sleep 1 second to respect API limits
  completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f""" Summarize the following consumer complaint narrative in 50 words or less. Focus on the summary on the specific issue raised in the complaint and the key facts surrounding it.
            complaint: {complaint_narrative}
            """
        }
    ],
    temperature=0.5,
    max_tokens=100,
    top_p=0.8,
    stream=True,
    stop=None,
  )
  summary = ""
  for chunk in completion:
    summary += chunk.choices[0].delta.content or ""
  return summary

# Apply the "get_summary" method to each complaint narrative
data['Narrative Summary'] = data['Consumer complaint narrative'].apply(get_summary)
