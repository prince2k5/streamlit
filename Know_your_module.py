import pandas as pd
import streamlit as st
import importlib
from inspect import getmembers, isfunction, signature
from PIL import Image
import base64

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
        with st.expander("module Attributes"):
            if modulename is not None:
                if modulename is not None:
                    try:
                        mod_name = importlib.import_module(modulename)
                        m = {k for k in dir(mod_name) if not k.startswith('_')}
                        for m in getmembers(mod_name, isfunction):
                            st.markdown(m[0])
                            st.code(signature(m[1]))# st.dataframe(a)
                    except:
                        pass
        a=getmembers(mod_name)

    except:
        pass

    with st.sidebar:
        lst=[]
        for i in a:
            if not str(i).startswith("_") :
                try:
                    st.write(signature(i[0]))
                except:
                    if not i[0].startswith("_"):
                        lst.append(i[0])

        st.table(lst)

    selected = st.selectbox("Please select any module and function Properties", lst)

    dict2={}
    if selected:
        st.code(signature(mod_name.__dict__[selected]))
        for p in getmembers(mod_name.__dict__[selected],isfunction) :
            if not str(p[0]).startswith("_"):
                try:
                    dict2[p[0]]=signature(p[1])
                except:
                    pass

        st.table(pd.Series(dict2))

    # except:
    #     pass
    # finally:
    with st.expander('SQL'):
        file = "https://raw.githubusercontent.com/prince2k5/streamlit/main/sqlcheatsheet.png"
        st.image(file)

