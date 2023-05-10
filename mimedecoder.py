import base64, quopri
import sys
import re


def encoded_words_txt(words):
	regex_s = r'=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}='
	charset, encoding, encoded_text = re.match(regex_strip, words).group
	if encoding == 'B':
		byte_string = base64.b64decode(encoded_text)
	elif encoding == 'Q':
		byte_string = quopri.decodestring(encoded_text)
	return byte_string.decode(charset)
#insert string here for decoding, option
n = ""
# Uncomment the following below to run command line decoding.
# n = sys.argv[0]
encoded_words_txt(n)


