# Import to use Streamlit Library
import streamlit as st

# Basic Setting to operate Streamlit app
# Main Function -> Define it without having the inner code
def main() :
    # Methods of st : Those that display the content
    st.title('Hello, this is Streamlit here!')
    st.subheader('Are you a newbie to Streamlit?')
    st.text('Let me help you to get started with Streamlit!')
    st.success('Your attempt has been successful!')
    st.info('Let me give you some notice!')
    st.warning('Are you sure?')
    st.error('Hey, something went wrong!')

    name = 'John'
    # print() : This prints the message in the Terminal, not on the web page
    print(f'Hey, my name is {name}.')
    # You can use st.text() to display the message on the web page
    st.text(f'Hey, my name is {name}.')

    st.write('You can write the message here.')


if __name__ == '__main__' :
    main()



    