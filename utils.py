import json
import os
import random

from settings import *

async def get_quote():
	with open(os.path.join(DATA_DIR, "famous_quotes.json"), errors='ignore') as quote_file:
		quotes = json.load(quote_file)
	random_quote = random.choice(list(quotes))
	fQuote = "\"" + random_quote["quoteText"] + "\" - " + random_quote["quoteAuthor"]
	return fQuote

def text_with_baby(text):
	listed = text.split()
	listed.pop(0)
	start = 0
	end = len(listed)
	while(start < end):
		ind = random.randint(1, end) 
		listed.insert(ind, "baby")
		start += ind
	return ' '.join(listed)

# Credit to Zenrac for this TextToOWO method
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
	li = s.rsplit(old, 1)
	return new.join(li)

def text_to_owo(text):
	""" Converts your text to OwO """
	smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

	text = text.replace('L', 'W').replace('l', 'w')
	text = text.replace('R', 'W').replace('r', 'w')

	text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
	text = last_replace(text, '?', '? owo')
	text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

	for v in vowels:
		if 'n{}'.format(v) in text:
			text = text.replace('n{}'.format(v), 'ny{}'.format(v))
		if 'N{}'.format(v) in text:
			text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

	return text
