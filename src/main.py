from bot import WhatsappBot

def out(resp):
    print(resp.answer.id)
    print(resp.answer.message)
    print(resp.action)

if __name__ == "__main__":

    my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

    # Some examples of how a conversation might start
    # Conv 1
    response = my_bot.message("confirm", "newsletter")
    response = my_bot.message("algo que nada tiene que ver @ algo . nose", "newsletter")
    print(response)
