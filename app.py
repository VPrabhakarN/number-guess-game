import streamlit as st
import random
import time

# ---------- Page Setup ----------
st.set_page_config(
    page_title="Guess Game 🎯",
    page_icon="🎯",
    layout="centered"
)

# ---------- Initialize Game ----------
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0

def reset_game():
    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0

# ---------- Clean Styling ----------
st.markdown("""
<style>
.title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    color: #2563eb;
}
.card {
    padding: 25px;
    border-radius: 18px;
    background: #f3f4f6;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}
.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI Header ----------
st.markdown('<div class="title">🎯 Guess the Number</div>', unsafe_allow_html=True)
st.caption("Can you guess the secret number between **1 and 100?**")
st.divider()

# ---------- Game Card ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<h4 class="center">🎮 Game Panel</h4>', unsafe_allow_html=True)
    st.markdown(f"<p class='center'><b>Attempts:</b> {st.session_state.tries}</p>",
                unsafe_allow_html=True)

    guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=100,
        step=1
    )

    col1, col2 = st.columns(2)

    with col1:
        guess_btn = st.button("🚀 Guess", use_container_width=True)

    with col2:
        st.button("🔁 New Game", on_click=reset_game, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Game Logic ----------
if guess_btn:
    st.session_state.tries += 1

    with st.spinner("Checking your guess..."):
        time.sleep(0.5)

    if guess == st.session_state.num:
        st.balloons()
        st.success(
            f"🎉 You nailed it in **{st.session_state.tries} tries!**"
        )
        st.button("Play Again", on_click=reset_game)

    elif guess > st.session_state.num:
        st.error("📉 Too high — try a smaller number.")
    else:
        st.warning("📈 Too low — try a bigger number.")

st.divider()
st.markdown("<p class='center'>Built with ❤️ using Streamlit</p>",
            unsafe_allow_html=True)
 