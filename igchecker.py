import streamlit as st
import json
import io
import time
import pandas as pd

st.set_page_config(page_title="Instagram Follower Checker", page_icon="📸", layout="centered")

st.title("📸 Instagram Follower Checker")

st.markdown("""
### 📥 How to Download Your Instagram Data

1. Open the **Instagram app** or go to [Instagram.com](https://www.instagram.com).
2. Go to your **Profile** → tap the **☰ menu** → select **Your activity**.
3. Scroll down and select **Download your information**.
4. Choose **JSON** as the format (not HTML).
5. Select **Followers and Following** (or "Connections") as the data type.
6. Tap **Request Download** and wait for Instagram to prepare the file (you’ll get a notification/email when ready).
7. Download the ZIP file, extract it, and you’ll find:
   - `followers_1.json` (your followers)
   - `following.json` (your following)
8. Upload those two files here to check who isn’t following you back 🚀.

---
""")


# File upload widgets
followers_file = st.file_uploader("Upload your followers JSON", type=["json"])
following_file = st.file_uploader("Upload your following JSON", type=["json"])

def extract_usernames_from_followers(file):
    data = json.load(file)
    usernames = []
    for entry in data:
        if "string_list_data" in entry:
            for s in entry["string_list_data"]:
                if "value" in s:
                    usernames.append(s["value"])
    return set(usernames)

def extract_usernames_from_following(file):
    data = json.load(file)
    usernames = []
    for entry in data.get("relationships_following", []):
        if "string_list_data" in entry:
            for s in entry["string_list_data"]:
                if "value" in s:
                    usernames.append(s["value"])
    return set(usernames)

if followers_file and following_file:
    with st.spinner("Analyzing your files... ⏳"):
        time.sleep(2)  # simulate loading
        followers = extract_usernames_from_followers(followers_file)
        following = extract_usernames_from_following(following_file)
        not_following_back = sorted(following - followers)

    st.markdown("<div class='result'>", unsafe_allow_html=True)
    st.subheader("🚫 People not following you back:")

    if not_following_back:
        # Slider for "not following back"
        preview_count = st.slider(
            "How many usernames to preview (not following you back)?", 
            min_value=5, 
            max_value=min(50, len(not_following_back)), 
            value=10
        )

        preview_list = not_following_back[:preview_count]
        for user in preview_list:
            st.write(f"@{user}")

        if len(not_following_back) > preview_count:
            st.info(f"...and {len(not_following_back) - preview_count} more.")

        # TXT output
        txt_output = "\n".join([f"@{user}" for user in not_following_back])
        txt_bytes = io.BytesIO(txt_output.encode("utf-8"))
        st.download_button(
            label="📥 Download Full Results (TXT)",
            data=txt_bytes,
            file_name="not_following_back.txt",
            mime="text/plain"
        )

        # CSV output
        df = pd.DataFrame({"Not Following Back": not_following_back})
        st.download_button(
            label="📥 Download Full Results (CSV)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="not_following_back.csv",
            mime="text/csv"
        )
    else:
        st.write("🎉 Everyone you follow follows you back!")

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- EXTRA FEATURES --------------------

    # People you don’t follow back
    you_dont_follow_back = sorted(followers - following)

    if you_dont_follow_back:
        st.subheader("🔄 People you don’t follow back:")

        # Slider for "you don’t follow back"
        preview_count2 = st.slider(
            "How many usernames to preview (you don’t follow back)?", 
            min_value=5, 
            max_value=min(50, len(you_dont_follow_back)), 
            value=10
        )

        preview_list2 = you_dont_follow_back[:preview_count2]
        for user in preview_list2:
            st.write(f"@{user}")

        if len(you_dont_follow_back) > preview_count2:
            st.info(f"...and {len(you_dont_follow_back) - preview_count2} more.")

        # TXT output
        txt_output2 = "\n".join([f"@{user}" for user in you_dont_follow_back])
        txt_bytes2 = io.BytesIO(txt_output2.encode("utf-8"))
        st.download_button(
            label="📥 Download Full Results (TXT)",
            data=txt_bytes2,
            file_name="you_dont_follow_back.txt",
            mime="text/plain"
        )

        # CSV output
        df2 = pd.DataFrame({"You Don’t Follow Back": you_dont_follow_back})
        st.download_button(
            label="📥 Download Full Results (CSV)",
            data=df2.to_csv(index=False).encode("utf-8"),
            file_name="you_dont_follow_back.csv",
            mime="text/csv"
        )

    # Summary stats
    st.markdown("### 📊 Quick Stats")
    st.write(f"Followers: {len(followers)}")
    st.write(f"Following: {len(following)}")
    st.write(f"Not following back: {len(not_following_back)}")
    st.write(f"You don’t follow back: {len(you_dont_follow_back)}")

    # Visualization using Streamlit's built-in charting
    st.markdown("### 📊 Visualization")
    chart_data = pd.DataFrame({
        "Category": ["Mutual", "Not Following Back", "You Don’t Follow Back"],
        "Count": [
            len(followers & following),
            len(not_following_back),
            len(you_dont_follow_back)
        ]
    })
    st.bar_chart(chart_data.set_index("Category"))

