import streamlit as st
import time
import random

site_name = "Speedy Scenes"

chatbot_responses = [
    "Precisa de ajuda para escolher o papel de parede perfeito para o seu carro?",
    "Nossas exclusivas peças de arte de carros NFT são únicas! Gostaria de saber mais?",
    "Está com dificuldades com o seu pedido? Deixe-me ajudá-lo com isso.",
    "Procurando por um tipo específico de papel de parede de carro? Posso ajudá-lo a encontrar.",
    "Interessado em nossas últimas coleções? Posso mostrar o que há de novo!",
    "Precisa de assistência com nosso mercado de NFT? Posso orientá-lo no processo.",
    f"Obrigado por entrar em contato com o suporte do {site_name} chatbot! Como posso melhorar sua experiência?",
    "Nossos papéis de parede são projetados para realçar qualquer espaço. Tem alguma dúvida sobre a instalação?",
    "Curioso sobre nossas ofertas especiais e descontos? Posso fornecer as últimas promoções!"
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
    st.title("Aviso Legal")
    st.write("Este chatbot é apenas para fins informativos e não fornece conselhos legais, financeiros ou médicos. Ao "
             "prosseguir, você reconhece que está conversando com um sistema de inteligência artificial e que "
             "qualquer informação fornecida pelo chatbot não deve ser considerada como aconselhamento profissional e "
             "deve ser usada a seu próprio critério.")

    proceed = st.button("Confirmar")
    do_not_proceed = st.button("Recusar")

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
    st.title(f'🤖 | {site_name} Chatbot')

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    display_history_messages()

    if not st.session_state.chat_history:
        display_assistant_msg(message=f"Olá e bem-vindo ao {site_name}! 🚗✨ Como podemos ajudá-lo hoje? Se você tiver perguntas sobre nossos papéis de parede de carros, precisar de ajuda com suas compras de NFT ou qualquer outra coisa, estamos aqui para ajudar. Vamos colocá-lo na pista rápida para uma melhor experiência!")

    if prompt := st.chat_input("Escreva a sua pergunta..."):
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
