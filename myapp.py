import random
import streamlit as st

st.set_page_config(page_title="今日のアドバイス", page_icon="✨")

st.title("✨ 今日の診断 ✨")
st.write("質問に答えると、今日のあなたを診断します。")

# サイドバー
st.sidebar.header("設定")
name = st.sidebar.text_input("名前（ニックネームでもOK）", "")
mood = st.sidebar.selectbox("今の気分は？", ["めっちゃ元気", "ふつう", "ちょっと疲れた", "しんどい…"])
coffee = st.sidebar.slider("今日のカフェイン摂取量（杯）", 0, 10, 1)

st.divider()

st.subheader("Q1. いま一番したいことは？")
q1 = st.radio(
    "",
    ["寝たい", "ゲームしたい", "勉強 / 仕事を進めたい", "おいしいもの食べたい", "とりあえずスマホいじりたい"],
)

st.subheader("Q2. どっち派？")
q2 = st.selectbox(
    "",
    ["インドア", "アウトドア", "その日の気分", "決められない"],
)

st.subheader("Q3. いまの一言を選ぶなら？")
q3 = st.text_input("自由に書いてOK（空欄でも大丈夫）", "")

if st.button("診断する！"):
    if not name:
        name = "あなた"

    # 適当だけどそれっぽい診断ロジック
    score = 0

    if mood == "めっちゃ元気":
        score += 2
    elif mood == "ふつう":
        score += 1
    else:
        score -= 1

    if coffee >= 4:
        score += 1
    if "寝" in q1:
        score -= 1
    if "勉強" in q1 or "仕事" in q1:
        score += 1
    if q2 == "インドア":
        score -= 1
    elif q2 == "アウトドア":
        score += 1

    # 結果パターン
    results = [
        "今日は **ゆるっとモード**。無理せず、やれたらラッキーくらいの気持ちでいこう。",
        "今日は **コツコツ職人モード**。小さなタスクをサクサク片付けると気持ちよさそう。",
        "今日は **チャレンジモード**。ちょっとだけ難しそうなことに手を出してみると良い日。",
        "今日は **ごほうびデー**。自分に何か一つご褒美をあげてみて。",
    ]

    if score <= -1:
        result = results[0]
    elif score == 0:
        result = results[1]
    elif score == 1:
        result = results[2]
    else:
        result = results[3]

    st.success(f"{name} さんの今日の診断結果")
    st.markdown(result)

    if q3:
        st.caption(f"メモ：『{q3}』って思ってる自分も、ちゃんと大事にしてあげてね。")

    # おまけメッセージ
    tips = [
        "水を一杯飲んで、深呼吸してから次の行動を決めるのがおすすめ。",
        "5分だけタイマーをかけて、やることを一つだけやってみよう。",
        "スマホを裏返して置いてみると、ちょっとだけ集中しやすくなるかも。",
        "散歩しながら考えると、意外といいアイデアが出たりするよ。",
    ]
    st.write("💡 なんかいい感じになるヒント：")
    st.write(random.choice(tips))
else:
    st.info("左のサイドバーをいじって、下のボタンを押すと診断が始まるよ。")
