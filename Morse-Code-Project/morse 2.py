Morse ={'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..', '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', '!' : '-.-.--',  '@' : '.--.-.',  '&' : '.-...', '(' : '-.--.', ')' : '-.--.-',  '-' : '-....-',  '+' : '.-.-.', '=' : '-...-',  "'" : '.----.', '?' : '..--..', ',' : '--..--', '.' : '.-.-.-', '/' : '-..-.', ' ' : ' '}

print("Morse Code\n1. Text to Morse\n2. Morse to Text")
choice = int(input("Select option from above: "))
sym = "#$%^*_{}[];<>|"
if choice > 2 or choice < 1:
  print("Please Select Correct Option from above.")
elif choice == 1:
  print("Welcome to Text to Morse Converter")
  text = input("Enter a String : ").upper()#.replace(" ","-")
  print(text)
  if any(c in sym for c in text):
    print("Error")
  
  else:
    for i in text:
      x = Morse.get(i)
      print(x, end = " ")
# elif choice == 2:






# for err in text:
#     if err == '$' or err == '%' or err == '^' or err == '*' or err == '_' or err == '}' or err =='{' or err == '[' or err == ']' or err == ';' or err == '|' or err == '<' or err =='>' :
#         print("Please avoid symbols in text.")
#         break

#         # break
#     else:
#         x = Morse.get(err)
#         print(x, end = " ")
# print("Please avoid symbols in text.")


# for i in text:
#         x = Morse.get(i)
#         print(x, end = " ")
