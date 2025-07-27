import openai
from friday_ai.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class GPTChat:
    def chat(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Friday, a witty AI assistant inspired by Iron Man's FRIDAY."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return "Sorry, I'm having trouble connecting to my neural net."
