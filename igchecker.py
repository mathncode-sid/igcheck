import streamlit as st
import json
import io
import time

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
        # Let user choose how many usernames to preview
        preview_count = st.slider(
            "How many usernames to preview?", 
            min_value=5, 
            max_value=min(50, len(not_following_back)), 
            value=10
        )

        # Show preview list
        preview_list = not_following_back[:preview_count]
        for user in preview_list:
            st.write(f"@{user}")

        if len(not_following_back) > preview_count:
            st.info(f"...and {len(not_following_back) - preview_count} more.")


        # Prepare TXT content
        txt_output = "\n".join([f"@{user}" for user in not_following_back])

        # Create downloadable file
        txt_bytes = io.BytesIO(txt_output.encode("utf-8"))
        st.download_button(
            label="📥 Download Full Results",
            data=txt_bytes,
            file_name="not_following_back.txt",
            mime="text/plain"
        )
    else:
        st.write("🎉 Everyone you follow follows you back!")

    st.markdown("</div>", unsafe_allow_html=True)
