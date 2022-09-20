import pandas as pd
import plotly.express as px
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode, GridOptionsBuilder
from button_colors import ButtonColors

st.set_page_config(page_title="Nintendo Football Club Combo Cards Dashboard",
                   layout="wide"
                  )

df = pd.read_excel(
    io="NPFC.xlsx",
    engine="openpyxl",
    sheet_name="combo_cards",
    skiprows=2,
    usecols="A:L",
    nrows=125
)
cols = ["Kicking", "Speed", "Stamina", "Tech", "Toughness", "Jump", "Willpower"]
for col in cols:
    df[col] = df[col].apply(lambda x: int(x) if x == x else 0)
df["Card3"] = df["Card3"].apply(lambda x: str(x) if x == x else "")    

green_card_lst = [
    "Set Plays",
    "Analysis",
    "Marking",
    "Countering",
    "Pressuring",
    "Line Control",
    "MiniGame"
]
red_card_lst = [
    "Shooting",
    "Sliding",
    "Passing",
    "Heading",
    "Freestyling",
    "Dribbling",
    "Place Kicks"
]
blue_card_lst = [
    "Weights",
    "Agility",
    "Aerobics",
    "Kicking",
    "Stretching",
    "Running",
    "Sprinting"
]
yellow_card_lst = [
    "Spa",
    "Judo",
    "PK Practice",
    "Oil Therapy",
    "Meditation",
    "Visualising",
    "Gaming",
    "Signing",
    "MiniCamp"
]

# ------------ SIDE BAR ------------
st.sidebar.image("./logo.png", width=200) # Adding logo
st.sidebar.header("Filter by Cards:")
green_cards = st.sidebar.multiselect(
    "TACTICAL",
    default=green_card_lst,
    options=green_card_lst
)

red_cards = st.sidebar.multiselect(
    "TECHNICAL",
    default=red_card_lst,
    options=red_card_lst
)
blue_cards = st.sidebar.multiselect(
    "PHYSICAL",
    default=blue_card_lst,
    options=blue_card_lst
)
yellow_cards = st.sidebar.multiselect(
    "SUPPORT",
    default=yellow_card_lst,
    options=yellow_card_lst
)

only_3_card_combo = st.sidebar.checkbox("Show only three cards combos")
only_2_card_combo = st.sidebar.checkbox("Show only two cards combos")

if only_3_card_combo:
    only_3_card_combo = []
else:
    only_3_card_combo = [""]

if only_2_card_combo:
    df = df.loc[df["Card3"] == ""] # Remove all non empty rows
    df = df.drop("Card3", axis=1) # Remove column Card3 from data frame
    df_selection = df.query(
    "(Card1 == @green_cards | Card1 == @red_cards | Card1 == @blue_cards | Card1 == @yellow_cards) &"
    "(Card2 == @green_cards | Card2 == @red_cards | Card2 == @blue_cards | Card2 == @yellow_cards)"
    )
else:
    df_selection = df.query(
    "(Card1 == @green_cards | Card1 == @red_cards | Card1 == @blue_cards | Card1 == @yellow_cards) &"
    "(Card2 == @green_cards | Card2 == @red_cards | Card2 == @blue_cards | Card2 == @yellow_cards) &"
    "(Card3 == @green_cards | Card3 == @red_cards | Card3 == @blue_cards | Card3 == @yellow_cards |"
    " Card3 == @only_3_card_combo)"
    )

st.sidebar.image("./logo_bottom.png", width=200) # Adding logo
st.sidebar.caption("Created by cybercotlet")
ButtonColors.color()

# ------------ MAIN PAGE ------------
st.header("Combo Cards Dashboard")
# --- Table configuration ---
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)
gd.configure_selection(selection_mode="single")
gd_options = gd.build()
table = AgGrid(df_selection, gridOptions=gd_options,
                height=None,
                update_mode=GridUpdateMode.SELECTION_CHANGED,
                allow_unsafe_jscode=True
)
sel_row = table["selected_rows"]
col1, col2 = st.columns(2)
combo_name = ""
with col1:
    # --- Chart configuration ---
    do_not_display_col = ["_selectedRowNodeInfo", "Card1", "Card2", "Card3", "Combo Name", "Total Point Gain"]
    if bool(sel_row):
        sel_dict = sel_row[0]
        x_axis = []
        y_axis = []
        for key, value in sel_dict.items():
            if key not in do_not_display_col:
                x_axis.append(key)
                y_axis.append(value)
            elif key == "Combo Name":
                combo_name = value

        fig = px.bar(x=x_axis, 
                    y=y_axis, 
                    title=f"<b>Combo Name: {combo_name}</b>", 
                    template="plotly_white")
        st.plotly_chart(fig)
with col2:
    gk_only = ["Desperate Saves", "Titanic Goalie", "Super Save", "Goalie Runs Up"]
    if combo_name in gk_only:
        st.header("GK ONLY COMBO")
