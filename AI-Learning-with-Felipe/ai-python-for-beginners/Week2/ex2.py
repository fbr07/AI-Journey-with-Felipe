# from dotenv import load_dotenv
from openai import OpenAI

# Now that we have imported OpenAI we can use the OpenAi
# print_llm_response get_llm_response


# def get_llm_response(prompt):
#    completion = client.chat.completions.create(
#        model="gpt-4o-mini",
#        messages=[
#            {
#                "role": "system",
#                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
#            },
#            {"role": "user", "content": prompt},
#        ],
#        temperature=0.0,
#    )
#    response = completion.choices[0].message.content
#    return response


# To use the OpenAI API service you need an API key.
# You receive the OpenAPI key and set it in path as windows path in environment
# variables. This is the safest way instead of adding the API in the file
# client = OpenAI()
# print(client) #after printing if it states any error then you API is not
# set up correctly in the environment variables

client = OpenAI()


# Step 2: Define your function
def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response


prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)
