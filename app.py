import streamlit as st
from datetime import datetime

# --- Demo dataset: 10 Indian meals with macros ---
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

# --- Demo exercises dataset ---
exercises = [
    {"type": "Cardio", "name": "Running 30 min"},
    {"type": "Strength", "name": "Push-ups 3x12"},
    {"type": "Strength", "name": "Squats 3x15"},
    {"type": "Flexibility", "name": "Yoga 20 min"},
    {"type": "HIIT", "name": "Burpees 3x10"},
]

# --- App UI ---
st.set_page_config(page_title="FitBharat Planner", layout="wide")
st.title("💪 FitBharat Planner")
st.markdown("A simple Indian meal & workout planner demo.")

# Sidebar: User info
with st.sidebar:
    st.header("👤 User Profile")
    name = st.text_input("Name", "Fitness Enthusiast")
    age = st.number_input("Age", 10, 80, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)", 40, 150, 70)
    height = st.number_input("Height (cm)", 140, 220, 170)

# Tab layout
tab1, tab2 = st.tabs(["🍽️ Meals", "💪 Workouts"])

with tab1:
    st.header("Today's Meal Plan")
    for meal in meals:
        st.subheader(f"{meal['meal_type']}: {meal['name']}")
        st.write(f"Calories: {meal['calories']} kcal | Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}g")

with tab2:
    st.header("Today's Workout Plan")
    for ex in exercises:
        st.write(f"• {ex['type']}: {ex['name']}")

# Daily calorie tracker
st.sidebar.header("📊 Calorie Tracker")
daily_calories = st.sidebar.number_input("Calories Consumed Today", min_value=0, value=0)
st.sidebar.metric("Calories", daily_calories)
