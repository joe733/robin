import streamlit as slt
from urllib.parse import quote
from random import sample

alpha = 'abcdefghijklmnopqrstuvwxyz'

slt.title("Get Jitsi Meet Link")
named_link = slt.text_input("Enter Meeting Name (optional)")
if slt.button("Generate"):
    if named_link != '':
        if len(named_link) <= 4:
            slt.write("Error: text length must be > 4")
        else:
            slt.write(f"Join: https://meet.jit.si/{quote(named_link)}")
    else:
        slt.write('Join: https://meet.jit.si/'+'-'.join([''.join(sample(alpha, 3)) for _ in range(3)]))