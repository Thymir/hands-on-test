# Test considerations

test_message.py can be found in src directory.

The capability to confirm or reject interest while entering the email provoke, in my opinion, some inconsistencies.

I consider that the ability to confirm interest and then do it again is awkward.

If the user confirms the interest and changes his mind the message displayed would be:
  "Okay, I hope you enjoy the experience at the restaurant"
Then the bot wouldn't hangup and upon the next interaction would send:
  "Thanks for reaching out. I can't help you with anything else yet but if you want to make a reservation you can call the restaurant again"

This last interaction doesn't meet any purpose and does not fit the conversation, as such I considered as wrong in the tests, therefore some tests fail.

I would change it, when conversation_status == "expectingEmail" if a rejection is detected then the bot sets next_action to "hangup"

# Code changes

## Email detection

If it's required to detect emails such as:
    "My email is info@bookline.io"
Where not only the email is given, then words other than the email shouldn't be considered as part of the email.

The current validate_email function returns:
  re.match(r"[^@]+@[^@]+\.[^@]+", email)
Allows spaces mid email, "My email is info@bookline.io" is considered as the whole email.
I would change it for:
  re.search(r"[^@\s]+@[^@\s]+\.[^@\s]+", email)

The email can be retrieved with
  email = self._validate_email(query.strip()).group()

## Redundant code between flows

There is redundant code for asking for the email. This could be in a function for both to call.
Another solution is to call a specific conversation flow based on your conversation_status which I think would lead into cleaner code.
