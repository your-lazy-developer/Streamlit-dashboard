import streamlit as st
import math

st.title("📚 Semester Credit Tracker")

total_credits = 0
course_count = 0

st.write("Enter credits one by one (enter 0 to stop)")

# Input as a string so user can enter multiple values like: 3,4,2,5
credits_input = st.text_input(
    "Enter credits separated by commas (example: 3,4,2,5)"
)

if st.button("Calculate"):
    st.success("You're on track 🚀")
    if credits_input:
        credits_list = credits_input.split(",")

        for item in credits_list:
            try:
                credits = int(item.strip())

                if credits == 0:
                    break
                elif credits < 0:
                    st.error("Invalid Input")
                    continue
                else:
                    total_credits += credits
                    course_count += 1

            except:
                st.error(f"Invalid value: {item}")

        rshr = math.ceil((total_credits * 2.5) + math.pi)

        st.write(f"{'Total Courses':<20} {course_count}")
        st.write(f"{'Total Credits':<20} {total_credits}")
        st.write(f"{'Study Hours/Week':<20} {rshr}")