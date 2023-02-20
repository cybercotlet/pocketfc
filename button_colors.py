import streamlit as st

class ButtonColors:
    @staticmethod
    def color():
        st.markdown(
            """
        <style>
        span[role="checkbox"] {
        border-bottom-color: #414141 !important;
        border-top-color: #414141 !important;
        border-right-color: #414141 !important;
        border-left-color: #414141 !important;
        background-color: #414141 !important;
        }
        span[aria-label="Set Plays, close by backspace"] {
        background-color: #47C129 !important;
        }
        span[aria-label="Analysis, close by backspace"] {
        background-color: #47C129 !important;
        }
        span[aria-label="Marking, close by backspace"] {
        background-color: #47C129 !important;
        }
        span[aria-label="Countering, close by backspace"] {
        background-color: #47C129 !important;
        }
        span[aria-label="Pressuring, close by backspace"] {
        background-color: #47C129 !important;
        }
        span[aria-label="Line Control, close by backspace"] {
        background-color: #47C129 !important;
        }
        span[aria-label="MiniGame, close by backspace"] {
        background-color: #47C129 !important;
        }

        span[aria-label="Shooting, close by backspace"] {
        background-color: #DA3A13 !important;
        }
        span[aria-label="Sliding, close by backspace"] {
        background-color: #DA3A13 !important;
        }
        span[aria-label="Passing, close by backspace"] {
        background-color: #DA3A13 !important;
        }
        span[aria-label="Heading, close by backspace"] {
        background-color: #DA3A13 !important;
        }
        span[aria-label="Freestyling, close by backspace"] {
        background-color: #DA3A13 !important;
        }
        span[aria-label="Dribbling, close by backspace"] {
        background-color: #DA3A13 !important;
        }
        span[aria-label="Place Kicks, close by backspace"] {
        background-color: #DA3A13 !important;
        }

        span[aria-label="Weights, close by backspace"] {
        background-color: #2173C7 !important;
        }
        span[aria-label="Agility, close by backspace"] {
        background-color: #2173C7 !important;
        }
        span[aria-label="Aerobics, close by backspace"] {
        background-color: #2173C7 !important;
        }
        span[aria-label="Kicking, close by backspace"] {
        background-color: #2173C7 !important;
        }
        span[aria-label="Stretching, close by backspace"] {
        background-color: #2173C7 !important;
        }
        span[aria-label="Running, close by backspace"] {
        background-color: #2173C7 !important;
        }
        span[aria-label="Sprinting, close by backspace"] {
        background-color: #2173C7 !important;
        }

        span[aria-label="Spa, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Judo, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="PK Practice, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Oil Therapy, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Meditation, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Visualising, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Meeting, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Gaming, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Signing, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="MiniCamp, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        span[aria-label="Karaoke, close by backspace"] {
        background-color: #F9C900 !important;
        color: #414141 !important;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
