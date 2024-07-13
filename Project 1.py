#Encryption and Decryption of a message using Caesar Cipher Algorithm
letters="abcdefghijklmnopqrstuvwxyz"
print("######## CAESAR CIPHER ALGORITHM ########")
num=int(input("Enter the number 1 to convert the message in Encryption or 2 to convert the message in Decryption: "))
if(num==1):
    print("Encryption Begins")
    message=input("Enter the message for Encryption: ")
    shift_key=int(input("Enter the key for encryption from 1-26: "))
    cipherText=""
    for letter in message:
        letter=letter.lower()
        if not letter == ' ':
            index=letters.find(letter)
            if index==-1:
                cipherText+=letter
            else:
                new_index=index+ shift_key
                if new_index >=26:
                    new_index -=26
                cipherText += letters[new_index]
    print(cipherText)
elif(num==2):
    print("Decryption Begins")
    message=input("Enter the message for Decryption: ")
    shift_key=int(input("Enter the key for decryption from 1-26: "))
    cipherText=""
    for letter in message:
        letter=letter.lower()
        if not letter == ' ':
            index=letters.find(letter)
            if index==-1:
                cipherText+=letter
            else:
                new_index=index - shift_key
                if new_index < 0:
                    new_index +=26
                cipherText += letters[new_index]
    print(cipherText)
else:
    print("Invalid Choice! Message cannot be Encrypted or Decrypted")
