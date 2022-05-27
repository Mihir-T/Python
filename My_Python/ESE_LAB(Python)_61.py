#function to encrypt the plain text
def encrypt(plain_text, shift):
  cipher = " "
  
  # transverse the plain text
  for letter in plain_text:   
    
    # check for blank space
    if letter == " ":     
      cipher = cipher + letter
      
    elif  letter.isupper():
      #Encrypt uppercase characters in plain text
      cipher = cipher + chr((ord(letter) + shift - 65) % 26 + 65) 
       
    else:
      #Encrypt lowercase characters in plain text
      cipher = cipher + chr((ord(letter) + shift - 97) % 26 + 97)  
      
  return(cipher)

#function to decrypt the encrypted text
def decrypt(encrypted_text, shift):
    cipher = " "
  
 # transverse the encrypted text
    for letter in encrypted_text:   
    
        # check for blank space
        if letter == " ":     
            cipher = cipher + letter
      
        elif  letter.isupper():
            #Decrypt uppercase characters in encrypted text
            cipher = cipher + chr((ord(letter) + shift - 65) % 26 + 65) 
       
        else:
            #Decrypt lowercase characters in encrypted text
            cipher = cipher + chr((ord(letter) + shift - 97) % 26 + 97)  
      
    return(cipher)   
 

text = input("Enter the plain text:")
s = int(input("Enter shift number:"))
e=encrypt(text,s)
d=decrypt(e,-s)
print("\nEncrypted text is:",e)
print("\nDecrypted text is:",d)
