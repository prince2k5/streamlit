import pandas as pd
import streamlit as st
import importlib
from inspect import getmembers, isfunction, signature
from PIL import Image

st.set_page_config(page_title="⚙Know Your Module🛠",layout="wide")
st.title('⚙Know Your Module🛠')

dict1={}


def explain(m):
    try:
        dict1[m[0]] = signature(m[1])
        return dict1
    except ValueError:
        return f"{m[0]}(???)"  # some functions don't provide a signature

if __name__=='__main__':
    try:
        modulename = st.text_input('Please enter name of the module')
        if modulename is not None or modulename!="":
            if modulename is not None:
                try:
                    mod_name = importlib.import_module(modulename)
                    m = {k for k in dir(mod_name) if not k.startswith('_')}
                    a = {m[0]: signature(m[1]) for m in getmembers(mod_name, isfunction)}
                    st.table(pd.Series(a))

                    if m is not None:
                        with st.expander('Module properties'):
                            selected=st.selectbox("Module Properties",m)
                            if selected is not None:
                                try:
                                    st.code(signature(mod_name.__dict__[selected]))
                                except:
                                    st.table(getmembers(mod_name.__dict__[selected]))

                except Exception as err:
                    st.exception(err)
    except:
        pass
    with st.expander('SQL'):
        img=Image.open(r"C:\Users\princ\Downloads\sqlcheatsheet.png")
        st.image(img)
