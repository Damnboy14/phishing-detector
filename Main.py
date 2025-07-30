import tkinter as tk

# Backend phishing detection logic
suspicious_keywords = ['login', 'verify', 'update', 'free', 'bonus', 'account', 'bank', 'secure', 'password', 'win']

def detect_phishing(url):
    score = 0
    if len(url) > 75:
        score += 1
    if '@' in url:
        score += 1
    if url.count('//') > 1:
        score += 1
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            score += 1
    if not url.startswith("https"):
        score += 1
    return "Phishing URL Detected" if score >= 3 else "Safe URL"

# Check URL and show result
def check_url():
    url = entry.get()
    if not url.strip():
        result_label.config(text="Please enter a URL", fg="orange", font=("Helvetica", 14, "bold"))
    else:
        result = detect_phishing(url)
        color = "red" if "Phishing" in result else "green"
        result_label.config(text=result, fg=color, font=("Helvetica", 16, "bold"))

# Hover effects
def on_enter(e):
    check_button.config(bg="yellow", fg="black")  # Hover color

def on_leave(e):
    check_button.config(bg="black", fg="black")   # Default color

# Main window
root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("450x220")
root.configure(bg="black")

# Title label
tk.Label(root, text="Enter URL to Check:", font=("Helvetica", 16, "bold"), bg="black").pack(pady=15)

# Entry field
entry = tk.Entry(root, width=40, font=("Helvetica", 14), bg="#f5f5f5", fg="black", bd=2, relief="solid")
entry.pack(pady=10)

# Check button
check_button = tk.Button(root, text="Check", font=("Helvetica", 14, "bold"), bg="black", fg="black", padx=20, pady=5, command=check_url)
check_button.pack(pady=15)

# Bind hover events
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
result_label.pack()

root.mainloop()
