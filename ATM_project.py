import streamlit as st

st.set_page_config(page_title="Python ATM", layout="centered")

# ---------------- DATABASE ----------------
persons = ["Ravi", "Amisha", "Shelja"]
account_numbers = [6576, 2017, 8052]
pins = [8888, 2020, 1717]
balances = [10000, 20000, 300]

# ---------------- SESSION VARIABLES ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "index" not in st.session_state:
    st.session_state.index = None

# ---------------- LOGIN PAGE ----------------
def login():
    st.title("🏧 Python ATM System")

    account = st.number_input("Enter Account Number", min_value=1, step=1)

    pin = st.number_input("Enter PIN", min_value=0000, max_value=9999, step=1)

    if st.button("Login"):
        if account in account_numbers:
            idx = account_numbers.index(account)

            if pin == pins[idx]:
                st.session_state.logged_in = True
                st.session_state.index = idx
                st.success(f"Login Successful 🎉 Welcome {persons[idx]}")
            else:
                st.error("❌ Incorrect PIN!")
        else:
            st.error("❌ Account Number Not Found!")


# ---------------- ATM MENU ----------------
def atm_menu():
    idx = st.session_state.index
    st.subheader(f"Hello, {persons[idx]} 😊")

    option = st.selectbox(
        "\nSelect an operation:",
        ("Check Balance", "Withdraw", "Deposit", "Change PIN", "Exit")
    )

    # Match Case Logic
    match option:

        case "Check Balance":
            st.info(f"💰 Current Balance: ₹{balances[idx]}")

        case "Withdraw":
            amount = st.number_input("Enter Withdrawal Amount", min_value=1, step=100)

            if st.button("Withdraw"):
                if amount <= balances[idx]:
                    balances[idx] -= amount
                    st.success(f"₹{amount} Withdrawn Successfully ✔")
                    st.info(f"New Balance: ₹{balances[idx]}")
                else:
                    st.error("❌ Insufficient Balance!")

        case "Deposit":
            amount = st.number_input("Enter Deposit Amount (100 - 10000)", step=100)

            if st.button("Deposit"):
                if 100 <= amount <= 10000:
                    balances[idx] += amount
                    st.success(f"₹{amount} Deposited Successfully ✔")
                    st.info(f"New Balance: ₹{balances[idx]}")
                else:
                    st.error("❌ Invalid Deposit Amount!")

        case "Change PIN":
            new_pin = st.number_input("Enter New PIN", min_value=0000, max_value=9999, step=1)
            confirm_pin = st.number_input("Confirm New PIN", min_value=0000, max_value=9999, step=1)

            if st.button("Update PIN"):
                if new_pin == confirm_pin and len(str(int(new_pin))) == 4:
                    pins[idx] = new_pin
                    st.success("🔐 PIN Updated Successfully!")
                else:
                    st.error("❌ PIN Mismatch or Invalid Format!")

        case "Exit":
            st.success("🙏 Thank You for Using Python ATM!")
            st.session_state.logged_in = False  # logout


# ---------------- MAIN APP FLOW ----------------
if st.session_state.logged_in:
    atm_menu()
else:
    login()
