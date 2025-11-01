import streamlit as st

# --- Data Section ---
person = ['Ravi', 'Amisha', 'Shelja']
mobile = [9354594339, 9873270017, 8020000052]
current_balance = [10000, 20000, 300]

# --- App Header ---
st.title("🏧 Simple ATM System")
st.subheader("Welcome to the Demo ATM App")

# --- User Input ---
user = st.text_input("Enter your Name")

if st.button("Login"):
    if user in person:
        a = person.index(user)
        st.success(f"Welcome {person[a]}!")
        st.write(f"📱 Mobile No: {mobile[a]}")

        # --- Option Menu ---
        option = st.selectbox(
            "Select an Option:",
            ["Select", "Account Statement", "Withdraw Funds", "Deposit Funds", "Change PIN", "Exit"]
        )

        if option == "Account Statement":
            st.info(f"Your Current Balance is ₹{current_balance[a]}")

        elif option == "Withdraw Funds":
            Withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0)
            if st.button("Withdraw"):
                if Withdraw_amount <= current_balance[a]:
                    current_balance[a] -= Withdraw_amount
                    st.success(f"₹{Withdraw_amount} withdrawn successfully!")
                    st.info(f"Updated Balance: ₹{current_balance[a]}")
                else:
                    st.error("Insufficient Balance!")

        elif option == "Deposit Funds":
            deposit = st.number_input("Enter amount to deposit:", min_value=0)
            if st.button("Deposit"):
                current_balance[a] += deposit
                st.success(f"₹{deposit} deposited successfully!")
                st.info(f"Updated Balance: ₹{current_balance[a]}")

        elif option == "Change PIN":
            st.warning("Change PIN option is not working right now.")

        elif option == "Exit":
            st.write("Thank you for using the ATM!")
    else:
        st.error("You are not our account holder.")
