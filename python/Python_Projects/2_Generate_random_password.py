import random
import string 

def generate_password():
    length=int(input("Enter the length of the password:").strip())
    upper_case=input("Enter if upper case to be included? (yes/no)").strip()
    special_case=input("Enter if upper case to be included? (yes/no)").strip()
    include_digits=input("Enter if upper case to be included? (yes/no)").strip()

    if length<4:
        print("Password length should be atleast 4 characters")
        return

    lower=string.ascii_lowercase
    upper=string.ascii_uppercase if upper_case=="yes" else "" 
    special=string.punctuation if special_case=="yes" else ""
    digits=string.digits if include_digits=="yes" else ""
    all_together=lower+upper+special+digits
    print(all_together)

    characters=[]
    if upper_case=="yes":
        characters.append(random.choice(upper))
    #print(characters)
    if special_case=="yes":
        characters.append(random.choice(special_case))
    if include_digits=="yes":
        characters.append(random.choice(digits))

    ramaining_length=length-len(characters)
    
    for _ in range(ramaining_length):
        characters.append(random.choice(all_together))
    
    random.shuffle(characters)
    str_password="".join(characters)
    return str_password

password=generate_password()
print(f"The generated password based on your preference is:{password}")
