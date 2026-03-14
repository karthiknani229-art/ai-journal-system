from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def analyze_emotion(text):

    try:

        prompt = f"""
        Detect the emotion in this journal entry.

        Entry: {text}

        Return one word emotion like:
        happy, sad, anxious, stressed, excited
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        emotion = response.choices[0].message.content.strip()

        return emotion

    except Exception as e:
        print("AI Error:", e)
        return "unknown"