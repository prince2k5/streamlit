import pandas as pd
import inspect
import streamlit as st
import importlib
from inspect import getmembers, isfunction, signature
import numpy

df=pd.DataFrame()

l={k for k in dir(df) if not k.startswith('_')}
m={k for k in dir(pd) if not k.startswith('_')}

lst_operation=['Add','subtract','multiply','division','change data type','filter','replace','remove','append new col','append new row','append dataframe',
               'pivot','unpivot','crosstab','join/merge/concat','sort','drop index','drop column','export','fill blanks/na','reindex','set_index','reset_index'
               ,'stack','unstack','get summary','join all the values of column',]

if __name__=='__main__':
    dict1={}
    def explain(m):
        try:
            dict1[m[0]] = signature(m[1])
            return dict1
        except ValueError:
            return f"{m[0]}(???)"  # some functions don't provide a signature


    # dict1={m[0]:explain(m) for m in getmembers(numpy, isfunction)}
    # print(dict1)
    a = {m[0]: signature(m[1]) for m in getmembers(pd, isfunction)}
    a1 = {m[0]: signature(m[1]) for m in getmembers(pd.DataFrame, isfunction)}
    aa=pd.Series(a1)
    aa1=aa.reset_index()
    aa2=aa1[aa1.iloc[:, 0].str.startswith('_') == False]

    st.caption("https://pandas.pydata.org/docs/user_guide/index.html")
    with st.sidebar:
        with st.expander('DataFrame methods'):
            st.dataframe(l)
        with st.expander('Pandas properties'):
            st.dataframe(m)

        with st.expander('Pandas Common Operations'):
            st.table(lst_operation)

    with st.expander('Pandas Properties'):
        st.table(pd.Series(a))
    with st.expander('DataFrame Properties'):
        st.table(aa2)
    # with st.container():
    # if st.button('import CSV'):
    file1= st.file_uploader('Please select the csv file')

    if file1 is not None:
        df1=pd.read_csv(file1)
        st.dataframe(df1)

        st.caption('Column Operations')
        cols=st.multiselect('select columns',df1.columns)

        st.write('what do you want to do')
        st.text('suggestions')

        choice=st.multiselect('Choose the operation',lst_operation)

        if st.checkbox('Exclude above columns'):
            new_columns=[i for i in df1.columns if i not in cols]
            # st.text(new_columns)
            st.dataframe(df1.loc[:,new_columns])

        cols_filter=st.selectbox('select columns to be filtered',df1.columns)
        if st.checkbox('Filter column'):
            # new_columns=[i for i in df1.columns if i not in cols]
            # st.text(new_columns)
            val=st.text_input('Enter value')
            st.dataframe(df1[df1[cols_filter]==val])

        cols_repl = st.selectbox('select columns to be replaced', df1.columns)
        if st.checkbox('replace column value'):
            val_input = st.text_input('Enter value to be replaced')
            val_tgt=st.text_input('Enter value to be set')
            if val_tgt is None:
                val_tgt=''
            st.dataframe(df1[cols_repl].str.replace(val_input,val_tgt))

        if choice=='get summary':
            st.text(df1.describe())