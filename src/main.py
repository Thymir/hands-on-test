from bot import WhatsappBot

if __name__ == "__main__":

    my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

    # Conv 1
    my_bot.message("Yes, I would like to receive notifications", "newsletter")

    # Conv 2
    my_bot.message("No, I would hate to receive notifications", "newsletter")

    # Conv 3
    my_bot.message("My email is info@bookline.io", "ask_for_email")

    # Conv 4
    my_bot.message("My email is not_a_valid_email.com", "ask_for_email")

    # Conv 5
    my_bot.message("This should not happen, so bot should hangup", "ask_for_card")
