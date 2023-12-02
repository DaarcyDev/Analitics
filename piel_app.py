import streamlit as st
from joblib import load
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier

def main():
    
    age = st.text_input('Age', value = '', max_chars=50)
    at_procurement = st.text_input('At Procurement', value ='', max_chars=50)
    mutation_count = st.text_input('Mutation Count', value = '', max_chars=50)
    mutation_status = st.text_input('Mutation Status', value='', max_chars=50)
    person_gender = st.text_input('Person Gender', value='', max_chars=50)
    primary_tumor_site = st.text_input('Primary Tumor Site', value='', max_chars=50)
    sample_type = st.text_input('Sample Type', value='', max_chars=50)
    specimen_site = st.text_input('Specimen Site', value='', max_chars=50)
    tissue_source_site = st.text_input('Tissue Source Site', value='', max_chars=50)
    
    if(st.button('Capturar informacion')):
        st.write('valores capturados')
        st.write('Age: ', {age})
        st.write('At Procurement: ', {at_procurement})
        st.write('Mutation Count: ', {mutation_count})
        st.write('Mutation Status: ', {mutation_status})
        st.write('Person Gender: ', {person_gender})
        st.write('Primary Tumor Site: ', {primary_tumor_site})
        st.write('Sample Type: ', {sample_type})
        st.write('Specimen Site: ', {specimen_site})
        st.write('Tissue Source Site: ', {tissue_source_site})
        
if __name__== '__main__':
    main()