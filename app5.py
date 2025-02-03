import streamlit as st


def main() :
    # Step 1 : Get name from user
    name = st.text_input('Submit your name :')
    print(name)
    st.text(name)

    # Step 2 : Limit the number of letters user can submit
    address = st.text_input('Submit your address (Max. 20 letter) :', max_chars = 20) # max_chars : limiting the maximum letter usage
    st.text(address)

    # Step 3 : Get multiple-row input from user
    message = st.text_area('Submit your message :', height = 200) # height : modifying the height of the input box
    st.text(message)

    # Step 4 : Getting personal information such as password
    password = st.text_input('Submit your password :', type = 'password') # type : changing the type of input into specific form
    st.text(password)

    # Step 5 : Getting the integer
    st.number_input('Submit your age :', min_value = 0, max_value = 150) # min_value/max_value : limit min/max value; noting data type 

    # Step 6 : Getting the double
    st.number_input('Submit your height', min_value = 0.0, max_value = 250.0, step = 0.5) # step : noting the interval between two values

    # Step 7 : Getting the date
    date = st.date_input('Submit the date :')
    print(type(date))
    print(date.weekday())
    st.text(f'Today is {date.strftime("%A")}.')
    
    # Step 8 : Getting the time
    time = st.time_input('Submit the time :')
    print(time)
    print(type(time))
    st.text(f'Now it\'s {time.strftime("%I:%M %p")}.')

    # Step 9 : Allow user to choose color
    color = st.color_picker('Choose your favorite color :')
    print(color)


if __name__ == '__main__' :
    main()