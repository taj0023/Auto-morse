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
	print('Usage: "morse <morse_string> -d <delimitor>"')
	exit()

string = sys.argv[1]

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
			try:
				if sys.argv[2] == '-d':
					l.append(sys.argv[3])
			except IndexError:
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