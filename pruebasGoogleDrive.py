import openai
openai.api_key= "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"
completion = openai.Completion.create(engine = "text-davinci-003",
                                      prompt = "¿Que es chat Gpt?",
                                      max_tokens = 200)
print(completion.choices[0].text)