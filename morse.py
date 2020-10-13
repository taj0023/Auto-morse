#!/usr/bin/env python3
import sys

d = {
		"A" :	".-" ,		
		"B" :	"-...",
		"C" :	"-.-.", 	
		"D" :	"-..",
		"E" :	".", 		
		"F" :	"..-.",
		"G" :	"--.", 	
		"H" :	"....",
		"I" :	"..", 		
		"J" :	".---",
		"K" :	"-.-" ,	
		"L" :	".-..",
		"M" :	"--" ,		
		"N" :	"-.",
		"O" :	"---" ,	
		"P" :	".--.",
		"Q" :	"--.-" ,	
		"R" :	".-.",
		"S"	:	"...", 	
		"T" :	"-",
		"U" :	"..-" ,	
		"V" :	"...-",
		"W" :	".--", 	
		"X" :	"-..-",
		"Y" :	"-.--", 	
		"Z" :	"--..",
		"0" :	"-----" ,	
		"1" :	".----",
		"2" :	"..---" ,	
		"3" :	"...--",
		"4" :	"....-" ,	
		"5" :	".....",
		"6" :	"-....", 	
		"7" :	"--...",
		"8" :	"---..", 	
		"9" :	"----.",
		"." :	".-.-.-", 	
		"," :	"--..--",
		"?" :	"..--..", 	
		"=" :	"-...-"
	}
reverse_d = {
			 '.-': 'A',
			 '-...': 'B',
			 '-.-.': 'C',
			 '-..': 'D',
			 '.': 'E',
			 '..-.': 'F',
			 '--.': 'G',
			 '....': 'H',
			 '..': 'I',
			 '.---': 'J',
			 '-.-': 'K',
			 '.-..': 'L',
			 '--': 'M',
			 '-.': 'N',
			 '---': 'O',
			 '.--.': 'P',
			 '--.-': 'Q',
			 '.-.': 'R',
			 '...': 'S',
			 '-': 'T',
			 '..-': 'U',
			 '...-': 'V',
			 '.--': 'W',
			 '-..-': 'X',
			 '-.--': 'Y',
			 '--..': 'Z',
			 '-----': '0',
			 '.----': '1',
			 '..---': '2',
			 '...--': '3',
			 '....-': '4',
			 '.....': '5',
			 '-....': '6',
			 '--...': '7',
			 '---..': '8',
			 '----.': '9',
			 '.-.-.-': '.',
			 '--..--': ',',
			 '..--..': '?',
			 '-...-': '='
			}
if len(sys.argv) == 1:
	print('Usage: "python3 morse.py <morse_string> -d <delimitor>"')
	exit()
#['./unda.py', '-d', '/', 'AN']
if len(sys.argv) == 4:
	if sys.argv[1] == '-d':
		delimitor = sys.argv[2]
		string = sys.argv[3]
	elif sys.argv[2] == '-d':
		delimitor = sys.argv[3]
		string = sys.argv[1]
elif len(sys.argv) == 2:
	string = sys.argv[1]
else:
	print("INVALID ARGUMENTS!")
	exit()



def morse_decode(s):
	l = []
	for each in string.split():
		if each in reverse_d.keys():
			l.append(reverse_d[each])
		else:
			l.append(each)

	return "".join(l)


def morse_encode(s):
	l = []
	for c in s:
		if c == " ":
			if '-d' in sys.argv:
				l.append(delimitor)
			else:
				l.append("|")
		if c.upper() in d.keys():
			l.append(d[c.upper()])
			l.append(" ")
		elif c.upper() not in d.keys():
			l.append(c)
			l.append(" ")

	return "".join(l)


def main():
	if '.' not in string and '-' not in string:
		print(morse_encode(string))
	else:
		print(morse_decode(string))

main()