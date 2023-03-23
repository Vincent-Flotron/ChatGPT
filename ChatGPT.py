import openai


# Read key
with open('../../../Downloads/7zip/key3.txt', 'r') as file:
# with open("../../GPTKey/key3.txt", 'r') as file:
    content = file.read()

# set the key
openai.api_key = content

preprompt = "Now you will emulate a Progress ABL interpreter. You will return strictly ONLY the output result of the following code preceded by the key word '_OK_' if the code as no error. If the code as an error, return the corrected code preceded by the key word '_ERROR_'. For exemple, if you receive 'DEFINE e AS CHARACTER NON-UNDO INITIAL ""hola"".\nDISPLAY(e).' you must return '_OK_ hola'. And if you receive 'DEFINE e AS CHARATER NON-UNDO INITIAL ""hola"".\nDISPLAY(e)', you must return '_NOK_ there is a mistake on the word CHARATER and a dot is missing after ""DISPLAY(e)"". Here is the corrected code: DEFINE e AS CHARACTER NON-UNDO INITIAL ""hola"".\nDISPLAY(e).'\nNow here is the Progress ABL code to interpret: "

# def prompt_gpt4(prompt_text):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt_text,
#         max_tokens=2048,
#         n=1,
#         stop=None,
#         temperature=0.1,
#     )
#     return response.choices[0].text.strip()
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work

def prompt_gpt4(prompt_text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "Now you will emulate a Progress ABL interpreter. You will return striclty ONLY the output result of the following code preceded by the key word '_OK_' if the code as no error. If the code as an error, return the corrected code preceded by the key word '_ERROR_' and dont use the keyword '_OK_'"},
            {"role": "user", "content": "DEFINE e AS CHARACTER NON-UNDO INITIAL ""hola"".\nDISPLAY(e)."},
            {"role": "assistant", "content": "_OK_ hola"},
            {"role": "user", "content": "DEFINE e AS CHARATER NON-UNDO INITIAL ""hola"".\nDISPLAY(e)"},
            {"role": "assistant", "content": "_NOK_ there is a mistake on the word CHARATER and a dot is missing after ""DISPLAY(e)"". Here is the corrected code: DEFINE e AS CHARACTER NON-UNDO INITIAL ""hola"".\nDISPLAY(e)."},
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message.content  # To extract just the assistant's reply


# DEFINE myvar AS INTEGER NO-UNDO INITIAL 10\nDISPLAY("Value: " + STRING(myvar)).
continue_asking = True
# while continue_asking:

# prompt = input('Write what you want: ')
prompt = "DEFINE mess AS CHARATER NON-UNDO INITIAL ""hello world"".\nDISPLAY(mess + "" 2"")."

if ( prompt == "quit" or prompt == "q" ):
    continue_asking = False

else:
    answer = prompt_gpt4(preprompt + prompt)
    print(answer)






























# import tkinter as tk

# def ask_gpt4():
#     user_text = user_input.get()
#     prompt = f"{user_text}"
#     response_text = prompt_gpt4(prompt)
#     chat_text.insert(tk.END, f"User: {user_text}\n")
#     chat_text.insert(tk.END, f"GPT-4: {response_text}\n")
#     user_input.delete(0, tk.END)

# root = tk.Tk()
# root.title("GPT-4 Chat GUI")

# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)

# chat_text = tk.Text(frame, wrap="word", width=50, height=15)
# chat_text.pack(padx=5, pady=5)
# chat_text.config(state="disabled")

# user_input = tk.Entry(frame, width=40)
# user_input.pack(padx=5, pady=5)

# ask_button = tk.Button(frame, text="Ask GPT-4", command=ask_gpt4)
# ask_button.pack(padx=5, pady=5)

# root.mainloop()
