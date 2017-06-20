from twilio.rest import Client
import random

# If running on a server, you may need to change the quotes.txt filepath to work.
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quote = random.choice(list(f))

textQuote = "Today's Bruce Lee Quote: \n{}".format(quote)

# Insert your own Twilio Account SID and Auth Token
client = Client("####", "####")

# Insert your own registered Twilio 'to' and 'from' numbers.
client.messages.create(to="#############",
                       from_="############",
                       body=textQuote)
