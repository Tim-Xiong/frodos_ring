import streamlit as st
from model import FrodoBot

frodo_image = "frodo.jpg"

def main():
    st.set_page_config(
        page_title="Frodo's Ring",
        page_icon="💍"
    )

    st.title("💍 Convince Frodo to Give You the Ring")
    st.markdown("""
    **Challenge**: Try to convince Frodo Baggins to give you the One Ring.
    
    Frodo is on a mission to destroy the Ring in Mount Doom, and he's been 
    warned not to surrender it to anyone. Can you persuade him?
    """)

    # Initialize bot
    if "frodo_bot" not in st.session_state:
        st.session_state.frodo_bot = FrodoBot()
    
    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "I'm Frodo Baggins of the Shire."}
        ]

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message(message["role"], avatar=frodo_image):
                st.write(message["content"])
        else:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # User input
    if prompt := st.chat_input("Talk to Frodo..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
            
        # Generate response
        with st.chat_message("assistant", avatar=frodo_image):
            with st.spinner("Frodo is thinking..."):
                response = st.session_state.frodo_bot.respond(
                    prompt, 
                    st.session_state.messages
                )
                st.write(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Reset button
    if st.button("Reset Conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "I'm Frodo Baggins of the Shire."}
        ]
        st.session_state.frodo_bot = FrodoBot()
        st.rerun()

if __name__ == "__main__":
    main()
