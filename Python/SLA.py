
days= int(input("Enter no. of days : "))
print('''
      Enter Week of Day the Month Begins with : 
          0:Monday 
          1:Tuesday
          2:Wednesday
          3:Thursday
          4:Friday
          5:Saturday
          6:Sunday
      ''')
      
week=int(input("Enter Starting day : "))
print("Mo | Tu | We | Th | Fr | Sa | Su ")

match week:
    case 0 :
        pass
    case 1 :
        print("     ",end="")
    case 2 :
        print("          ",end="")
    case 3 :
        print("               ",end="")
    case 4 :
        print("                    ",end="")
    case 5 :
        print("                         ",end="")
    case 6 :
        print("                              ",end="")
        
current_pos=week
for i in range(1,days+1):
    print(f"{i:>2}   ",end="")
    current_pos+=1
    if current_pos%7 == 0:
        print()
    
        
# Q2
def histogran(numbers):
    for num in numbers :
        print("*"*num)
        
histogran([3,4,5])

# Q3

def is_palindrome(phrase):
  # Keep only alphanumeric characters and convert to lowercase
  cleaned = "".join(ch.lower() for ch in phrase if ch.isalnum())

  # Compare the cleaned string with its reverse
  return cleaned == cleaned[::-1]

# test_phrases.
# Test cases from the assignment
test_phrases = [
    "Go hang a salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!",
    "This is not a palindrome",
]

for p in test_phrases:
  print(f'"{p}" -> {is_palindrome(p)}')
        
    