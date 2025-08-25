# Fitmaxx-AI-2.0


A lightweight nutrition + workout planner with Indian meals built in.


## ⭐ Features
- Profile sidebar (age, gender, height, weight, goal, activity).
- Auto BMR/TDEE + macro targets.
- 50+ Indian meals (Breakfast/Lunch/Dinner/Snack) with macros.
- One‑click daily plan generator based on your calorie target.
- Weekly workout templates by goal & level.
- Calorie tracker + food log.
- Export meal/workout plan as CSV.
- No API keys or secrets required.


## 🧰 Tech
- Python, Streamlit, Pandas, NumPy


## ▶️ Run locally
```bash
# 1) Clone
git clone https://github.com/<your-username>/fitbharat.git
cd fitbharat


# 2) Create venv (optional)
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


# 3) Install deps
pip install -r requirements.txt


# 4) Launch
streamlit run app.py
