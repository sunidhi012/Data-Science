import streamlit as st
from model import gemini


st.header(
    'Gemini Integration LLM'
)

st.subheader(
    'Version 3.8 Flash'
)

## Text Placeholder
# st.text_input(
#     'Enter your prompt',
#     value = 'Explain about animal',
#      placeholder = 'Enter your name',
#      max_chars = 20,
#      type='password'
# )

st.text_area(
    'Enter your prompt',
    placeholder='Explain about animal.'
)

## Button
btn = st.button('Send Prompt')

if btn:
    # st.toast('Entered')
    # time.sleep(3)
    # st.success('Button Entered Success')
    # st.error('Button Entered Error')
    # st.warning('Button Entered Warning')
    if prompt.strip() == '':
        st.warning('Text field cannot be empty.')
    else:
        with st.spinner('Generating Content...'):
            answer = gemini(prompt)
            st.write(answer)
            st.toast('Content Generated.')