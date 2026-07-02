import streamlit as st
from translator import translate_text, get_languages
from utils import copy_text



# Page Configuration

st.set_page_config(
    page_title="AI Translator App",
    page_icon="🌐",
    layout="wide"
)
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown("""

""", unsafe_allow_html=True)

# Center Logo
st.image("assets/logo.png", width=120)

# Center Title
st.markdown(
    """
    <h1 style='text-align:center;
                font-size:60px;
                font-weight:bold;
                color:#4F8BF9;'>
        AI Translator
    </h1>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    """
    <p style='text-align:center;
                color:#9CA3AF;
                font-size:24px;'>
        Translate text into 100+ languages instantly
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<center><h4 style='color:gray;'></h4></center>",
    unsafe_allow_html=True
)



# Initialize session state

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Auto Detect"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"


# Languages

languages = get_languages()
languages = {name.title(): code for name, code in languages.items()}

languages = {"Auto Detect": "auto", **languages}

# Auto Detect add kardiya
languages = {"Auto Detect": "auto", **languages}


# Select Languages
left, center, right = st.columns([2,1,2])

with center:
    if st.button("🔄 Swap Languages"):
        temp = st.session_state.source_lang
        st.session_state.source_lang = st.session_state.target_lang
        st.session_state.target_lang = temp
        st.rerun()
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
    "Source Language",
    list(languages.keys())[1:],
    key="source_lang"
)

with col2:
    target_language = st.selectbox(
    "Target Language",
    list(languages.keys())[1:],
    key="target_lang"
)


# Text Input

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something here..."
)


# Translate Button

if st.button("🌍 Translate", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = translate_text(
    text,
    languages[source_language],
    languages[target_language]
)

        st.session_state["translated"] = translated
        st.success("✅ Translation Completed")


# Show Translation

if "translated" in st.session_state:

    st.markdown("## ✅ Translated Text")

    st.text_area(
        "Output",
        st.session_state["translated"],
        height=180
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📋 Copy"):
            copy_text(st.session_state["translated"])
            st.success("Copied Successfully!")

    with col2:
        st.download_button(
            label="⬇ Download",
            data=st.session_state["translated"],
            file_name="translation.txt",
            mime="text/plain"
        )
        st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:16px;">
        
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray">
Made with ❤️ using Python & Streamlit <br>
👨‍💻 Developed by <b>Prem Prakash Mishra</b>
</div>
""",
unsafe_allow_html=True
)