import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- Demo dataset: Meals ---
meals = [
    {"meal_type": "Breakfast", "name": "Poha with Peanuts", "calories": 350, "protein": 10, "carbs": 60, "fat": 8},
    {"meal_type": "Breakfast", "name": "Upma with Vegetables", "calories": 320, "protein": 9, "carbs": 55, "fat": 7},
    {"meal_type": "Lunch", "name": "Paneer Curry with Roti", "calories": 600, "protein": 25, "carbs": 80, "fat": 20},
    {"meal_type": "Lunch", "name": "Dal with Rice", "calories": 550, "protein": 20, "carbs": 90, "fat": 10},
    {"meal_type": "Dinner", "name": "Grilled Fish with Veggies", "calories": 500, "protein": 35, "carbs": 40, "fat": 15},
    {"meal_type": "Dinner", "name": "Chole with Bhature", "calories": 650, "protein": 20, "carbs": 100, "fat": 18},
    {"meal_type": "Snack", "name": "Fruit Salad", "calories": 150, "protein": 2, "carbs": 35, "fat": 0},
    {"meal_type": "Snack", "name": "Roasted Chana", "calories": 200, "protein": 10, "carbs": 30, "fat": 5},
    {"meal_type": "Snack", "name": "Masala Corn", "calories": 180, "protein": 5, "carbs": 30, "fat": 5},
    {"meal_type": "Snack", "name": "Sprouts Salad", "calories": 120, "protein": 8, "carbs": 20, "fat": 2},
]

# --- Demo exercises ---
exercises = [
    {"type": "Cardio", "name": "Running 30 min"},
    {"type": "Strength", "name": "Push-ups 3x12"},
    {"type": "Strength", "name": "Squats 3x15"},
    {"type": "Flexibility", "name": "Yoga 20 min"},
    {"type": "HIIT", "name": "Burpees 3x10"},
]

# --- Sidebar: User Info ---
st.sidebar.header("👤 Profile")
name = st.sidebar.text_input("Name", "Fitness Enthusiast")
age = st.sidebar.number_input("Age", 10, 80, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.sidebar.number_input("Weight (kg)", 40, 150, 70)
height = st.sidebar.number_input("Height (cm)", 140, 220, 170)
daily_calories = st.sidebar.number_input("Calories Consumed Today", min_value=0, value=0)

# --- Health calculations ---
bmi = weight / ((height/100)**2)
bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) if gender=="Male" else 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
tdee = bmr * 1.55  # moderate activity

# --- Main Header ---
st.markdown("<h1 style='text-align:center; color:#2E86AB;'>💪 FitBharat Planner</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center; color:#555;'>Welcome, {name}!</h3>", unsafe_allow_html=True)

# --- Metrics Cards ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("BMI", f"{bmi:.1f}")
col2.metric("BMR", f"{bmr:.0f} kcal")
col3.metric("TDEE", f"{tdee:.0f} kcal")
col4.metric("Calories Today", f"{daily_calories}/{int(tdee)} kcal")

# --- Tabs: Meals & Workouts ---
tab1, tab2, tab3 = st.tabs(["🍽️ Meals", "💪 Workouts", "📈 Progress"])

with tab1:
    st.header("Today's Meal Plan")
    for meal in meals:
        st.markdown(f"""
        <div style='background:#f0f4f8; padding:15px; border-radius:12px; margin-bottom:10px;'>
            <h4>{meal['meal_type']}: {meal['name']}</h4>
            <p>Calories: {meal['calories']} kcal | Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}g</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("Today's Workout Plan")
    for ex in exercises:
        st.markdown(f"""
        <div style='background:#fff3e6; padding:12px; border-radius:12px; margin-bottom:8px;'>
            <b>{ex['type']}</b>: {ex['name']}
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.header("Progress & Suggestions")

    # --- BMI Graph ---
    df_bmi = pd.DataFrame({
        "Metric": ["BMI", "Weight (kg)"],
        "Value": [bmi, weight]
    })
    fig, ax = plt.subplots()
    ax.bar(df_bmi["Metric"], df_bmi["Value"], color=["#4ECDC4","#FF6B6B"])
    ax.set_ylim(0, max(df_bmi["Value"])*1.2)
    st.pyplot(fig)

    # --- Suggested Actions ---
    st.subheader("💡 Suggested Actions")
    if bmi > 25:
        st.success("✅ Try 30 min walking today")
    else:
        st.info("✅ Maintain balanced diet")
    if daily_calories < tdee:
        st.info("✅ Add a healthy snack to reach TDEE")
    else:
        st.warning("⚠️ Calories exceeded today!")
    st.info("💧 Drink 8 glasses of water daily")
    st.info("📝 Log your meals consistently for best results")

# --- Footer ---
st.markdown("---")
st.markdown("<h5 style='text-align:center; color:#888;'>FitBharat Planner Demo</h5>", unsafe_allow_html=True)
