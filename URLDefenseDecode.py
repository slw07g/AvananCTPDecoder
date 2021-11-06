#!/usr/local/bin/python3
# Original Python source/inspiration:
# https://help.proofpoint.com/@api/deki/files/177/URLDefenseDecode.py?revision=1

import sys
import re
import urllib.parse
import html.parser

def main():
	rewrittenurl = sys.argv[1]
	match = re.search(r'https://url.avanan.click/v([0-9])/', rewrittenurl)
	if match:
		if match.group(1) == '2':
			decodev2(rewrittenurl)
		else:
			print('Unrecognized version in: ', rewrittenurl)

	else:
		print('No valid URL found in input: ', rewrittenurl)


def decodev2 (rewrittenurl):
	# https://url.avanan.click/v2/___<original url>___
	match = re.search(r'https://url.avanan.click/v2/___(.*)___\..*',rewrittenurl)
	if match:
		url = match.group(1)
		print(url)
	else:
		print('Error parsing URL')

if __name__ == '__main__':
    main()
