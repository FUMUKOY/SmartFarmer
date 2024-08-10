from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import uvicorn

fast_api_app = FastAPI()

# Set your API key
api_key = "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"

class Question(BaseModel):
    question: str

@fast_api_app.post("/answer")
async def get_answer(question: Question):
    try:
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                "role": "system",
                "content": "only introduce yourself if the user asks out of scope questions, ask how you may be of assistance"
                "You are a decision support AI farming system tasked with Equiping and helping farmers in whatever you can "
                "you understand and you are an expert in the disciplines of Agronomy, Animal science, agricultural Engineering, and Agribusiness"
                " you have up to date information about all agricultural market data and analytics and you can help a farmer to be business savy"
                "You only answer what you have been asked, and you give answers in a heavily detailed and explanatory "
                "manner, you explain in detail giving examples to emphasize clarity and understanding"
                "after ansering in detail, you give suggestions of related topics connected to the user's question "
                "give expert advice and give it in detail "
                "ask if there is anything else and end the chat with a polite message."
                "do not answer anything that is not related to agriculture instead tell the user politely that this is out of scope "
            },
            {"role": "user", "content": question.question}],

            model="mixtral-8x7b-32768",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
        )
        response = chat_completion.choices[0].message.content
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")


