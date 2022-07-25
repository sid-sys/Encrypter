from rsa import encrypt
import streamlit as st
from cryptography.fernet import Fernet
st.title("MessageEncrypter")
message = st.text_input('Enter the message')
key = b'Tj1IKVVTV1hiNDdheV1ZSnd-Wjc3QzcjVVNRaFwjWkQ='
if st.button("Encrypt"):
    encMessage = Fernet(key).encrypt(message.encode())
    encMessage = encMessage.decode("utf-8") 
    st.write("Your Encrypted message:")
    st.code(encMessage)

EncMessage =  st.text_input("Enter Encypted Message")
if st.button("Decrypt"):
    EncMessage =  EncMessage.encode("utf-8") 
    decMessage = Fernet(key).decrypt(EncMessage).decode()
    st.write("Your Decrypted message:")
    st.write(decMessage)
