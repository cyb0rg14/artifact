from hugchat import hugchat
from hugchat.login import Login

def write_article(inputs, email, password):
    sign = Login(email, password)
    cookies = sign.login()

    # save the cookies
    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)

    # create the chatbot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    # create new conversation
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

    prompt = f"""
        You are a professional writer. Help me write an article on {inputs['topic']} and write it in a way like you explaining it to {inputs['user']}. Write valid points along with explaining the topic in detailed manner & using bullet points. Make good use of markdown to distinguish title and other content. Make sure the article would be approximately {inputs['words']} words.
    """

    response = chatbot.chat(prompt)
    return response['text']

if __name__ == "__main__":
    write_article("", "", "")