import os
import openai

#your api key goes here, you can get your api key in openai website, and you need to log in
openai.api_key = "YOUR_API_KEY"


# Define the initial prompt
initial_prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\"."

while True:
    # Prompt the user for a question
    prompt_question = input("Enter your prompt question (or type '!exit' to exit): ")

    # Check if the user wants to exit the program
    if prompt_question == "!exit":
        print("Exiting the program...")
        break

    # Combine the initial prompt and user question
    prompt = f"{initial_prompt}\n\nQ: {prompt_question}\nA:"

    # Generate a response
    # here you can change your model, you can use check which model is avaliable on openai's website
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # Extract the AI-generated response
    ai_response = response.choices[0].text.strip()

    
    print("AI Response:", ai_response)
