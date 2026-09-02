import streamlit as st

MENU = {
    "いきなりまんじゅう": 250,
    "肉まん": 160,
    "チョコ": 150,
    "いちご": 150,
    "抹茶": 150,
    "ソーダ（白）": 150,
    "やぶれ（黒）": 150,
    "柏餅": 150
}

st.set_page_config(
    page_title="饅頭注文アプリ",
    page_icon="🍡",
    layout="centered"
)

st.title("🍡 饅頭注文アプリ")

st.write("---")

total_qty = 0
total_price = 0
orders = []

for item, price in MENU.items():

    col1, col2 = st.columns([5, 2])

    with col1:
        st.write(f"{item}（{price}円）")

    with col2:
        qty = st.number_input(
            label="数量",
            min_value=0,
            max_value=99,
            value=0,
            step=1,
            key=item,
            label_visibility="collapsed"
        )

    if qty > 0:
        amount = qty * price
        total_qty += qty
        total_price += amount

        orders.append(
            f"{item}　{qty}個　{amount:,}円"
        )

st.write("---")

st.subheader(f"合計個数：{total_qty}個")

st.markdown(
    f"<h2 style='color:red;'>合計金額：{total_price:,}円</h2>",
    unsafe_allow_html=True
)

st.write("---")

st.divider()

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("🔄 リセット", use_container_width=True):
        for item in MENU.keys():
            st.session_state[item] = 0
        st.rerun()

with col_btn2:
    confirm = st.button(
        "✅ 注文確定",
        use_container_width=True
    )
    
if confirm:

    if total_qty == 0:
        st.warning("数量を入力してください。")
    else:
        st.success("注文を受け付けました")

        st.write("### 注文内容")

        for order in orders:
            st.write(order)

        st.write("---")
        st.write(f"合計個数：{total_qty}個")
        st.write(f"合計金額：{total_price:,}円")
