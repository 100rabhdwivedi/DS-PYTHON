import streamlit as st
import random

st.set_page_config(page_title="Stone Paper Scissors", page_icon="🎮", layout="centered")

st.title("🪨 📄 ✂️ Stone – Paper – Scissors")
st.write("### First to score 5 points wins!")

# Initialize state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "last_user_choice" not in st.session_state:
    st.session_state.last_user_choice = None
if "last_comp_choice" not in st.session_state:
    st.session_state.last_comp_choice = None
if "last_result" not in st.session_state:
    st.session_state.last_result = ""

choices = {
    "Stone": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

def play(user_choice):

    # stop playing if game already ended
    if st.session_state.user_score == 5 or st.session_state.comp_score == 5:
        return

    comp_choice = random.choice(list(choices.keys()))

    # save choices for stable UI display
    st.session_state.last_user_choice = user_choice
    st.session_state.last_comp_choice = comp_choice

    # Game Logic
    if user_choice == comp_choice:
        st.session_state.last_result = "⚖️ It's a Draw!"
    elif (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Stone" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Stone"):
        st.session_state.user_score += 1
        st.session_state.last_result = "🔥 You won this round!"
    else:
        st.session_state.comp_score += 1
        st.session_state.last_result = "🤖 Computer won this round!"

# Disable game buttons when game ends
game_over = st.session_state.user_score == 5 or st.session_state.comp_score == 5

st.write("## Choose your move:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Stone", disabled=game_over):
        play("Stone")

with col2:
    if st.button("📄 Paper", disabled=game_over):
        play("Paper")

with col3:
    if st.button("✂️ Scissors", disabled=game_over):
        play("Scissors")

# Stable UI (does NOT flicker now)
st.write("---")
st.write("## 🎯 Last Round Result")

if st.session_state.last_user_choice:
    st.write(f"### You chose: {choices[st.session_state.last_user_choice]}")
    st.write(f"### Computer chose: {choices[st.session_state.last_comp_choice]}")
    st.write(f"## {st.session_state.last_result}")

# Scoreboard
st.write("---")
st.write("## 📊 Scoreboard")
st.write(f"### You: {st.session_state.user_score} | Computer: {st.session_state.comp_score}")

# Winner message
if st.session_state.user_score == 5:
    st.success("🎉 YOU WON THE GAME! 👑")
elif st.session_state.comp_score == 5:
    st.error("🤖 COMPUTER WON THE GAME!")

# Reset button
st.write("---")
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.last_user_choice = None
    st.session_state.last_comp_choice = None
    st.session_state.last_result = ""
    st.rerun()
