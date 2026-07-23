import sys
import os
import csv
from datetime import datetime, date
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def resource_path(file_name):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, file_name)


TODO_FILE = resource_path("todo_list.csv")
tasks = []  # daftar tugas: setiap item = {"title", "done", "priority", "due_date"}


# =========================
# Penyimpanan data (CSV)
# =========================
def save_tasks():
    try:
        with open(TODO_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            for t in tasks:
                writer.writerow([t["title"], t["done"], t["priority"], t["due_date"]])
    except Exception as e:
        messagebox.showerror("Error", f"Tidak bisa menyimpan file: {e}")


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return
    try:
        with open(TODO_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 4:
                    due_date = row[3].strip()
                    if due_date:
                        try:
                            datetime.strptime(due_date, "%Y-%m-%d")
                        except ValueError:
                            try:
                                dt = datetime.strptime(due_date, "%m/%d/%y")
                                due_date = dt.strftime("%Y-%m-%d")
                            except ValueError:
                                due_date = ""
                    priority = row[2] if row[2] in ("Low", "Medium", "High") else "Medium"
                    tasks.append({
                        "title": row[0],
                        "done": row[1] == "True",
                        "priority": priority,
                        "due_date": due_date
                    })
    except Exception as e:
        messagebox.showerror("Error", f"Tidak bisa memuat file: {e}")


# =========================
# Filter, pencarian, dan pengurutan
# =========================
FILTER_MAP = {
    "Semua": None,
    "Hari Ini": "today",
    "Terlambat": "overdue",
    "Prioritas Tinggi": "high",
}
SORT_MAP = {
    "Tanpa Urutan": None,
    "Tenggat Waktu": "due",
    "Prioritas": "priority",
}


def get_filtered_sorted_tasks(filter_type=None, sort_by=None, search_text=""):
    filtered = list(tasks)
    today_str = date.today().strftime("%Y-%m-%d")

    if filter_type == "today":
        filtered = [t for t in filtered if t["due_date"] == today_str]
    elif filter_type == "overdue":
        filtered = [t for t in filtered if t["due_date"] and t["due_date"] < today_str and not t["done"]]
    elif filter_type == "high":
        filtered = [t for t in filtered if t["priority"] == "High"]

    if search_text:
        filtered = [t for t in filtered if search_text.lower() in t["title"].lower()]

    if sort_by == "due":
        filtered.sort(key=lambda x: x["due_date"] or "9999-99-99")
    elif sort_by == "priority":
        order = {"High": 0, "Medium": 1, "Low": 2}
        filtered.sort(key=lambda x: order.get(x["priority"], 3))

    return filtered


def current_view():
    """Daftar tugas yang sedang tampil di tabel saat ini (sesuai filter/sort/cari aktif)."""
    return get_filtered_sorted_tasks(
        FILTER_MAP.get(filter_var.get()),
        SORT_MAP.get(sort_var.get()),
        search_var.get()
    )


# =========================
# Refresh tampilan (Treeview + Dashboard)
# =========================
def refresh_treeview(*args):
    for row in tree.get_children():
        tree.delete(row)

    for t in current_view():
        due_display = t["due_date"] if t["due_date"] else "—"
        tags = []
        if t["done"]:
            tags.append("done")
        elif t["priority"] == "High":
            tags.append("high")
        elif t["priority"] == "Medium":
            tags.append("medium")
        elif t["priority"] == "Low":
            tags.append("low")

        if t["due_date"] and not t["done"]:
            due_dt = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
            if due_dt < date.today():
                tags.append("overdue")

        tree.insert("", "end", values=(
            t["title"],
            "✅" if t["done"] else "❌",
            t["priority"],
            due_display
        ), tags=tags)

    refresh_dashboard()


def refresh_dashboard():
    total = len(tasks)
    done_count = sum(1 for t in tasks if t["done"])
    pending_count = total - done_count
    today_str = date.today().strftime("%Y-%m-%d")
    overdue_count = sum(
        1 for t in tasks
        if t["due_date"] and t["due_date"] < today_str and not t["done"]
    )

    total_label_val.set(f"Total Tugas: {total}")
    done_label_val.set(f"Selesai: {done_count}")
    pending_label_val.set(f"Belum Selesai: {pending_count}")
    overdue_label_val.set(f"Terlambat: {overdue_count}")


# =========================
# Aksi tombol
# =========================
def add_task():
    title = title_entry.get().strip()
    if not title:
        messagebox.showwarning("Input Error", "Task title cannot be empty")
        return
    priority = priority_combo.get()
    due_date = due_entry.get().strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid due date format. Use YYYY-MM-DD")
            return
    tasks.append({"title": title, "done": False, "priority": priority, "due_date": due_date})
    save_tasks()
    refresh_treeview()
    title_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)


def remove_task():
    selected = tree.selection()
    if not selected:
        return
    idx = tree.index(selected[0])
    removed = current_view()[idx]
    tasks[:] = [t for t in tasks if t is not removed]
    save_tasks()
    refresh_treeview()
    messagebox.showinfo("🗑️ Removed", f"Removed task: {removed['title']}")


def mark_done():
    selected = tree.selection()
    if not selected:
        return
    idx = tree.index(selected[0])
    target = current_view()[idx]
    for t in tasks:
        if t is target:
            t["done"] = True
            break
    save_tasks()
    refresh_treeview()


def clear_all_tasks():
    if messagebox.askyesno("⚠️ Clear All", "Are you sure you want to remove all tasks?"):
        tasks.clear()
        save_tasks()
        refresh_treeview()


def export_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV file", "*.csv"), ("Text file", "*.txt")])
    if not file_path:
        return
    try:
        if file_path.endswith(".csv"):
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                for t in tasks:
                    writer.writerow([t["title"], t["done"], t["priority"], t["due_date"]])
        else:
            with open(file_path, "w") as f:
                for t in tasks:
                    f.write(f"{t['title']} | {'Done' if t['done'] else 'Pending'} | {t['priority']} | {t['due_date'] or '—'}\n")
        messagebox.showinfo("💾 Exported", f"Tasks exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Export failed: {e}")


# =========================
# GUI Setup
# =========================
root = tk.Tk()
root.title("ToDoMate 📝")
root.geometry("950x600")
root.configure(bg="#f0f4f8")

style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass
style.configure("Treeview", rowheight=28, font=("Segoe UI", 10))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ---- Tab Dashboard ----
dashboard_tab = tk.Frame(notebook, bg="#f0f4f8")
notebook.add(dashboard_tab, text="📊 Dashboard")

total_label_val = tk.StringVar(value="Total Tugas: 0")
done_label_val = tk.StringVar(value="Selesai: 0")
pending_label_val = tk.StringVar(value="Belum Selesai: 0")
overdue_label_val = tk.StringVar(value="Terlambat: 0")

tk.Label(dashboard_tab, text="Ringkasan Tugas", font=("Segoe UI", 18, "bold"), bg="#f0f4f8").pack(pady=(40, 20))
tk.Label(dashboard_tab, textvariable=total_label_val, font=("Segoe UI", 14), bg="#f0f4f8").pack(pady=5)
tk.Label(dashboard_tab, textvariable=done_label_val, font=("Segoe UI", 14), bg="#f0f4f8", fg="#2e7d32").pack(pady=5)
tk.Label(dashboard_tab, textvariable=pending_label_val, font=("Segoe UI", 14), bg="#f0f4f8", fg="#ef6c00").pack(pady=5)
tk.Label(dashboard_tab, textvariable=overdue_label_val, font=("Segoe UI", 14), bg="#f0f4f8", fg="#c62828").pack(pady=5)

# ---- Tab To-Do List ----
todo_tab = tk.Frame(notebook, bg="#f0f4f8")
notebook.add(todo_tab, text="📝 To-Do List")

input_frame = tk.Frame(todo_tab, bg="#f0f4f8")
input_frame.pack(fill="x", padx=10, pady=10)

tk.Label(input_frame, text="Judul:", bg="#f0f4f8").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(input_frame, width=30)
title_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Prioritas:", bg="#f0f4f8").grid(row=0, column=2, sticky="w")
priority_combo = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], width=10, state="readonly")
priority_combo.set("Medium")
priority_combo.grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Tenggat (YYYY-MM-DD):", bg="#f0f4f8").grid(row=0, column=4, sticky="w")
due_entry = tk.Entry(input_frame, width=15)
due_entry.grid(row=0, column=5, padx=5)

tk.Button(input_frame, text="➕ Tambah", command=add_task).grid(row=0, column=6, padx=5)

control_frame = tk.Frame(todo_tab, bg="#f0f4f8")
control_frame.pack(fill="x", padx=10, pady=(0, 10))

tk.Label(control_frame, text="Filter:", bg="#f0f4f8").pack(side="left")
filter_var = tk.StringVar(value="Semua")
filter_combo = ttk.Combobox(control_frame, textvariable=filter_var, values=list(FILTER_MAP.keys()), width=15, state="readonly")
filter_combo.pack(side="left", padx=5)
filter_combo.bind("<<ComboboxSelected>>", refresh_treeview)

tk.Label(control_frame, text="Urutkan:", bg="#f0f4f8").pack(side="left", padx=(10, 0))
sort_var = tk.StringVar(value="Tanpa Urutan")
sort_combo = ttk.Combobox(control_frame, textvariable=sort_var, values=list(SORT_MAP.keys()), width=15, state="readonly")
sort_combo.pack(side="left", padx=5)
sort_combo.bind("<<ComboboxSelected>>", refresh_treeview)

tk.Label(control_frame, text="Cari:", bg="#f0f4f8").pack(side="left", padx=(10, 0))
search_var = tk.StringVar()
search_entry = tk.Entry(control_frame, textvariable=search_var, width=20)
search_entry.pack(side="left", padx=5)
search_var.trace_add("write", refresh_treeview)

columns = ("title", "done", "priority", "due_date")
tree = ttk.Treeview(todo_tab, columns=columns, show="headings", selectmode="browse")
tree.heading("title", text="Judul")
tree.heading("done", text="Status")
tree.heading("priority", text="Prioritas")
tree.heading("due_date", text="Tenggat")
tree.column("title", width=350)
tree.column("done", width=80, anchor="center")
tree.column("priority", width=100, anchor="center")
tree.column("due_date", width=120, anchor="center")
tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))

tree.tag_configure("done", foreground="#9e9e9e")
tree.tag_configure("high", foreground="#c62828")
tree.tag_configure("medium", foreground="#ef6c00")
tree.tag_configure("low", foreground="#2e7d32")
tree.tag_configure("overdue", background="#ffcdd2")

button_frame = tk.Frame(todo_tab, bg="#f0f4f8")
button_frame.pack(fill="x", padx=10, pady=(0, 10))

tk.Button(button_frame, text="✅ Tandai Selesai", command=mark_done).pack(side="left", padx=5)
tk.Button(button_frame, text="🗑️ Hapus", command=remove_task).pack(side="left", padx=5)
tk.Button(button_frame, text="⚠️ Hapus Semua", command=clear_all_tasks).pack(side="left", padx=5)
tk.Button(button_frame, text="💾 Export", command=export_tasks).pack(side="left", padx=5)

load_tasks()
refresh_treeview()
root.mainloop()

