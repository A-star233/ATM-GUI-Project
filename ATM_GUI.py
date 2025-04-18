from tkinter import*
from tkinter import simpledialog, messagebox

# Initial balance and PIN
balance = 8000
pin = 1111

# Colors for dark theme
BG_COLOR = "#2c3e50"
FG_COLOR = "#ecf0f1"
BTN_COLOR = "#34495e"
BTN_TEXT = "#ffffff"

# Setup main window
root = Tk()
root.title("ATM Machine")
root.geometry("350x400")
root.configure(bg=BG_COLOR)

# --- Login Screen ---
def check_pin():
    global entry
    try:
        entered_pin = int(entry.get())
        if entered_pin == pin:
            entry.delete(0,END)
            show_main_menu()
        else:
            messagebox.showerror("Error", "Incorrect Password")
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")

# --- Main Menu ---
def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="💳 Welcome to ATM", font=('Arial', 16, 'bold'), bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)

    menu_frame = Frame(root, bg=BG_COLOR)
    menu_frame.pack()

    Button(menu_frame, text="1. Check Balance", command=check_balance, bg=BTN_COLOR, fg=BTN_TEXT, width=25).pack(pady=5)
    Button(menu_frame, text="2. Deposit Amount", command=deposit_amount, bg=BTN_COLOR, fg=BTN_TEXT, width=25).pack(pady=5)
    Button(menu_frame, text="3. Withdraw Amount", command=withdraw_amount, bg=BTN_COLOR, fg=BTN_TEXT, width=25).pack(pady=5)
    Button(menu_frame, text="4. Convert Currency", command=currency_menu, bg=BTN_COLOR, fg=BTN_TEXT, width=25).pack(pady=5)
    Button(menu_frame, text="5. Exit", command=root.quit, bg=BTN_COLOR, fg=BTN_TEXT, width=25).pack(pady=10)

# --- Functional Options ---
def check_balance():
    messagebox.showinfo("Balance", f"Your balance is Rs. {balance}")

def deposit_amount():
    global balance
    amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
    if amount is None:
        return
    if amount <= 0:
        messagebox.showerror("Error", "Invalid deposit amount")
    else:
        balance += amount
        messagebox.showinfo("Success", f"Rs.{amount} deposited.\nUpdated balance: Rs.{balance}")

def withdraw_amount():
    global balance
    amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
    if amount is None:
        return
    if amount <= 0:
        messagebox.showerror("Error", "Invalid withdrawal amount")
    elif amount > balance:
        messagebox.showwarning("Error", "Insufficient balance")
    else:
        balance -= amount
        messagebox.showinfo("Success", f"Rs.{amount} withdrawn.\nRemaining balance: Rs.{balance}")

# --- Currency Conversion ---
def currency_menu():
    win = Toplevel(root)
    win.title("Currency Conversion")
    win.geometry("300x400")
    win.configure(bg=BG_COLOR)

    currencies = {
        "USD Dollar ($)": 86.7,
        "Chinese Yuan (¥)": 11.93,
        "Pakistani Rupee (PKR)": 3.18,
        "EURO (€)": 90.49,
        "Japanese Yen (JPY)": 0.58,
        "British Pound (GBP)": 105.24,
        "Australian Dollar (AUD)": 56.30,
        "Canadian Dollar (CAD)": 63.75,
        "Swiss Franc (CHF)": 95.12,
    }

    Label(win, text="🌐 Currency Options", font=('Arial', 14), bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

    def convert_currency(name, rate):
        global balance
        if balance < 5:
            messagebox.showerror("Error", "Not enough balance to use this service (Rs. 5 charge)")
            return

        balance -= 5
        option = messagebox.askquestion(
            "Conversion Type",
            f"Convert:\nYes → Balance to {name}\nNo → {name} to INR"
        )

        if option == "yes":
            converted = balance / rate
            messagebox.showinfo("Converted", f"Rs.{balance} = {name} {converted:.2f}")
        else:
            foreign_amt = simpledialog.askfloat("Input", f"Enter amount in {name}:")
            if foreign_amt:
                inr = foreign_amt * rate
                messagebox.showinfo("Converted", f"{foreign_amt} {name} = INR Rs.{inr:.2f}")

    for name, rate in currencies.items():
        Button(win, text=name, command=lambda n=name, r=rate: convert_currency(n, r),
                  bg=BTN_COLOR, fg=BTN_TEXT, width=30).pack(pady=3)

    Label(win, text="*Rs. 5 charged per conversion", fg="red", bg=BG_COLOR).pack(pady=10)

# --- Initial Login UI ---
Label(root, text="🔐 Enter your Password:", font=('Arial', 13), bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
entry = Entry(root, show="*", font=('Arial', 12), width=20, justify='center')
entry.pack(pady=5)
Button(root, text="Login", command=check_pin, bg=BTN_COLOR, fg=BTN_TEXT, width=20).pack(pady=15)

root.mainloop()
