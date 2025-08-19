# Instagram Follower Checker

This is a simple **Streamlit web app** that helps you analyze your Instagram followers and following data.  
It shows you who does not follow you back, who you do not follow back, and provides summary statistics with visualizations.

---

## Features

- Upload your Instagram `followers_1.json` and `following.json` files.
- Identify:
  - People you follow but who do not follow you back.
  - People who follow you but you do not follow back.
- Preview results with an adjustable slider.
- Download full results in both **TXT** and **CSV** formats.
- View quick statistics:
  - Number of followers
  - Number of accounts you are following
  - Number of people not following you back
  - Number of people you do not follow back
- Interactive bar chart visualization using Streamlit’s built-in charting.

---

## How It Works

1. **Download your Instagram data:**
   - Open the Instagram app or go to [Instagram.com](https://www.instagram.com).
   - Go to your **Profile** → tap the **Menu (☰)** → select **Your activity**.
   - Scroll down and select **Download your information**.
   - Choose **JSON** as the format (not HTML).
   - Select **Followers and Following** (or "Connections") as the data type.
   - Tap **Request Download** and wait for Instagram to prepare the file.
   - Once ready, download the ZIP file and extract it.
   - You will find:
     - `followers_1.json` (your followers)
     - `following.json` (your following)

2. **Run the app:**
   - Clone this repository.
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the Streamlit app:
     ```bash
     streamlit run igchecker.py
     ```

3. **Upload your files:**
   - Upload `followers_1.json` in the "Upload your followers JSON" section.
   - Upload `following.json` in the "Upload your following JSON" section.
   - The app will analyze the data and display results.

---

## Project Structure

```
├── igchecker.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Documentation
```

---

## Example Output

- A preview list of usernames who do not follow you back.
- A preview list of usernames you do not follow back.
- Download buttons for TXT and CSV files containing the full results.
- Quick statistics of your Instagram connections.
- A bar chart comparing mutuals, not following back, and those you do not follow back.

---

## Requirements

- Python 3.8+
- Streamlit
- Pandas

These are listed in `requirements.txt`.

---

## Notes

- This tool does not connect to Instagram’s API. It works entirely offline using the JSON files you download from Instagram.
- Your data stays on your machine; nothing is uploaded to any external server.
- Use this tool for personal analysis only.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it under the terms of the license.
