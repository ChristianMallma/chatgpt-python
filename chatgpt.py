# Library: https://github.com/openai/openai-python
import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Para salir escriba => exit")

while True:
  prompt = input("\Hazme una pregunta: ")

  if prompt == "exit":
    break

  completion  = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        n=3,
                                        max_tokens=2048) # longitud máxima de la respuesta (tamaño máximo 4096 caracteres)

  for i in range(3):
    print(f"\nAnswer[{i}]: {completion.choices[i].text}")
