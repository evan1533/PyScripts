import os
import SimpleEncryption as enc
import msvcrt as m

def wait():
    m.getch()

phrase = str(input("What is the password?\n"))
phrase.upper();
enc_phrase = enc.encrypt_text(phrase)
print(enc_phrase)
print(enc.decrypt_text(enc_phrase))
wait();
