import re
class Regex:

	def __init__(self, spam_indicator) :
		pattern = spam_indicator.lower().split(' ')
		self.patterns = '(.*)' + '(.*)'.join(pattern) + '(.*)'

	def is_match(self, text) :
		for pattern in self.patterns :
			if(re.search(text, pattern)) :
				return True

