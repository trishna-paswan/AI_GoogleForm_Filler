# main.py

import tkinter as tk
from tkinter import filedialog, messagebox
from extract_data import get_personal_data_from_pdf
from form_filler import fill_google_form

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        data = get_personal_data_from_pdf(file_path)
        for key in entries:
            if data.get(key):
                entries[key].delete(0, tk.END)
                entries[key].insert(0, data[key])

def submit_form():
    data = {key: entries[key].get() for key in entries}
    form_url = url_entry.get()
    if not form_url:
        messagebox.showerror("Error", "Please enter Google Form URL")
        return
    fill_google_form(data, form_url)
    messagebox.showinfo("Success", "Form submitted successfully!")

root = tk.Tk()
root.title("AI Google Form Filler")
root.geometry("400x400")

entries = {}
fields = ["Name", "Email", "Phone", "DOB", "Address"]

for field in fields:
    label = tk.Label(root, text=field)
    label.pack()
    entry = tk.Entry(root, width=50)
    entry.pack()
    entries[field] = entry

tk.Button(root, text="Upload Resume (PDF)", command=browse_file).pack(pady=10)

tk.Label(root, text="Google Form URL").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Button(root, text="Submit Form", command=submit_form).pack(pady=20)

root.mainloop()

'''
🚀 How to Run

pip install -r requirements.txt
python main.py

'''
