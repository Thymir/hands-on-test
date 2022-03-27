from bot import WhatsappBot
import unittest


class TestWhatsappMessages(unittest.TestCase):

    def setUp(self):
        self.newsletter_messages = [
            "Great! Please, let me know your e-mail",
            "Okay, I hope you enjoy the experience at the restaurant",
            "Please, let me know if you agree or not",
        ]
        self.email_messages = [
            "Perfect, we've stored your e-mail! Enjoy the experience at the restaurant",
            "It seems that this e-mail is not valid. Please make sure it's correct",
        ]
        self.closure_messages = [
            "Thanks for reaching out. I can't help you with anything else yet but if you want to make a reservation you can call the restaurant again"
        ]

        self.error_messages = [
            "There has been an error. Please try again later."
        ]

    def test_newsletter_reject(self):
        # reject
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("reject", "newsletter")  # has no interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[1])
        self.assertEqual(response["action"], "hangup")

        # unclear intent then reject
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("unsure towards notifications", "newsletter")
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[2])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("reject", "newsletter")  # has no interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[1])
        self.assertEqual(response["action"], "hangup")

        # confirm then reject
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("confirm", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("reject", "newsletter")  # has no interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[1])
        self.assertEqual(response["action"], "hangup")

        # invalid email -> reject
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("confirm", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("invalid@domain", "newsletter")  # invalid email
        self.assertEqual(response["answer"]["message"], self.email_messages[1])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("reject", "newsletter")  # has no interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[1])
        self.assertEqual(response["action"], "hangup")

    def test_newsletter_success(self):

        # valid email
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("confirm", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("email@domain.com", "newsletter")  # valid email
        self.assertEqual(response["answer"]["message"], self.email_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("anything", "newsletter")  # nothing to do -> hangup
        self.assertEqual(response["answer"]["message"], self.closure_messages[0])
        self.assertEqual(response["action"], "hangup")

        # invalid email then valid email
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("confirm", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("invalid@domain", "newsletter")  # invalid email
        self.assertEqual(response["answer"]["message"], self.email_messages[1])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("valid@domain.com", "newsletter")  # valid email
        self.assertEqual(response["answer"]["message"], self.email_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("anything", "newsletter")  # nothing to do -> hangup
        self.assertEqual(response["answer"]["message"], self.closure_messages[0])
        self.assertEqual(response["action"], "hangup")

        # unclear intent then confirm
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("unsure towards notifications", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[2])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("confirm", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("valid@domain.com", "newsletter")  # valid email
        self.assertEqual(response["answer"]["message"], self.email_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("anything", "newsletter")  # nothing to do -> hangup
        self.assertEqual(response["answer"]["message"], self.closure_messages[0])
        self.assertEqual(response["action"], "hangup")

    def test_email_valid(self):

        # valid email
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("valid@domain.com", "ask_for_email")  # valid email
        self.assertEqual(response["answer"]["message"], self.email_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("anything", "ask_for_email")  # nothing to do -> hangup
        self.assertEqual(response["answer"]["message"], self.closure_messages[0])
        self.assertEqual(response["action"], "hangup")

        # invalid email then valid email
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("invalid@domain", "ask_for_email")  # invalid email
        self.assertEqual(response["answer"]["message"], self.email_messages[1])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("valid@domain.com", "ask_for_email")  # valid email
        self.assertEqual(response["answer"]["message"], self.email_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("anything", "ask_for_email")  # nothing to do -> hangup
        self.assertEqual(response["answer"]["message"], self.closure_messages[0])
        self.assertEqual(response["action"], "hangup")

    def test_card(self):
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("anything", "ask_for_card")  # nothing to do -> hangup
        self.assertEqual(response["answer"]["message"], self.closure_messages[0])
        self.assertEqual(response["action"], "hangup")

    def test_email_error(self):
        my_bot = WhatsappBot(language="en")
        response = my_bot.message("email@error.com", "ask_for_email")  # error email
        self.assertEqual(response["answer"]["message"], self.error_messages[0])
        self.assertEqual(response["action"], "hangup")

        my_bot = WhatsappBot(language="en")
        response = my_bot.message("confirm", "newsletter")  # has interest
        self.assertEqual(response["answer"]["message"], self.newsletter_messages[0])
        self.assertEqual(response["action"], "continue")
        response = my_bot.message("email@error.com", "newsletter")  # error email
        self.assertEqual(response["answer"]["message"], self.error_messages[0])
        self.assertEqual(response["action"], "hangup")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestWhatsappMessages('test_newsletter_reject'))
    suite.addTest(TestWhatsappMessages('test_newsletter_success'))
    suite.addTest(TestWhatsappMessages('test_email_valid'))
    suite.addTest(TestWhatsappMessages('test_card'))
    suite.addTest(TestWhatsappMessages('test_email_error'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
