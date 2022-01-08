import pandas as pd
import streamlit as st
import altair as alt

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

st.header('Enter DNA Sequence')

sequence_input =">DNA Query \nCCCTATGACCCTGGCAAAGCGGGTGGAATACTGGCAAAGATCATCAAATCCGCTAACAGTATAGAATTGATACGAAACCAGATTAACGATGCTAAAAGAT"

sequence = st.text_area("Sequence input",sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]#Skips the first line
sequence =''.join(sequence)

st.write("""
***
""")

#Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

#DNA Nucleotide Count
st.header('OUTPUT (DNA Nucleotide Count')

#1. Print Dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d= dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
        ])
    return d
X = DNA_nucleotide_count(sequence)
X
#Print the Text
st.subheader('2. Print text')
st.write('There are '+str(X['A'])+' adenine (A)')
st.write('There are '+str(X['T'])+' adenine (T)')
st.write('There are '+str(X['G'])+' adenine (G)')
st.write('There are '+str(X['C'])+' adenine (C)')

#Display Dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X,orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

#Display Bar chart using alter
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(100)
)
st.write(p)