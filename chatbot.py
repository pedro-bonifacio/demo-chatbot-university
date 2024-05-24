import streamlit as st
import time
import random

site_name = "Speed Scapes"

chatbot_responses = [
    "Do you need help choosing the perfect car wallpaper for your home?",
    "Our exclusive NFT car art pieces are one-of-a-kind! Would you like to know more?",
    "Having trouble with your order? Let me help you with that.",
    "Looking for a specific type of car wallpaper? I can help you find it!",
    "Interested in our latest collections? I can show you what's new!",
    "Need assistance with our NFT marketplace? I can guide you through the process.",
    f"Thank you for reaching out to {site_name} support chatbot! How can I make your experience better?",
    "Our wallpapers are designed to enhance any space. Do you have any questions about installation?",
    "Curious about our special offers and discounts? I can provide you with the latest deals!"
]


def display_user_msg(message: str):
    """
    Display user message in chat message container
    """
    with st.chat_message("user", avatar="😎"):
        st.markdown(message)
    st.session_state.chat_history.append({"role": "user", "content": message})


def display_history_messages():
    # Display chat messages from history on app rerun
    avatar_dict = {'assistant': '🤖', 'user': '😎'}
    for message in st.session_state.chat_history:
        with st.chat_message(message['role'], avatar=avatar_dict[message['role']]):
            st.markdown(message['content'])


def simulate_typing(message: str):
    """
    Simulate typing
    """
    message_placeholder = st.empty()

    # Simulate stream of response with milliseconds delay
    for i in range(len(message)):
        time.sleep(0.02)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(message[:i] + "▌")

    message_placeholder.markdown(message)


def display_assistant_msg(message: str):
    """
    Display assistant message
    """
    with st.chat_message("assistant", avatar="🤖"):
        simulate_typing(message)

    st.session_state.chat_history.append({"role": "assistant", "content": message})


def show_legal_disclaimer():
    st.title("Legal Disclaimer")
    st.write("This chatbot is for informational purposes only and does not provide legal, financial, or medical "
             "advice. By proceeding, you acknowledge that you are talking to a robot and that any information "
             "provided by the chatbot should not be considered professional advice and should be used at your own "
             "discretion.")

    proceed = st.button("Proceed")
    do_not_proceed = st.button("Do Not Proceed")

    if proceed:
        st.session_state['accepted_legal'] = True
        st.rerun()
    elif do_not_proceed:
        st.warning("You have chosen not to proceed.")
        st.session_state['accepted_legal'] = False
        return
    else:
        return


def app():
    st.title(f'🤖 | {site_name} Support Chatbot')

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    display_history_messages()

    if not st.session_state.chat_history:
        display_assistant_msg(message=f"Hello and welcome to {site_name}! 🚗✨ How can we assist you today? Whether "
                                      "you have questions about our car wallpapers, need help with your NFT "
                                      "purchases, or anything else, we're here to help. Let's get you on the fast "
                                      "track to a better experience!")

    if prompt := st.chat_input("Type your request..."):
        # [*] Request & Response #
        display_user_msg(message=prompt)

        assistant_response = random.choice(chatbot_responses)

        display_assistant_msg(message=assistant_response)


if __name__ == "__main__":
    choice = st.session_state.get("accepted_legal", False)

    if choice:
        app()
    else:
        show_legal_disclaimer()
