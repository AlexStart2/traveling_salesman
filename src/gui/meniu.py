import matplotlib.pyplot as plt
import customtkinter as ct
import os
from tkinter import messagebox
from src.algorithms.backtracking import tsp_backtracking
from src.algorithms.hill_climbing import hill_climbing_tsp
from src.algorithms.genetic_algorithm import genetic_tsp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from src.algorithms.simanneal.simanneal_impl import run_simanneal

RESULTS_FILE = "rezultate.txt"
template = "size,bt_time,bt_cost,hc_time,hc_cost,sm_time,sm_cost,ga_time,ga_cost"
results_ready = False


def generate_cities(n):
    import random
    cities = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                row.append(random.randint(1, 100))
        cities.append(row)
    
    return cities


def reset_results():
    global results_ready
    if os.path.exists(RESULTS_FILE):
        os.remove(RESULTS_FILE)

    results_ready = False


time_frame = None
cost_frame = None

def show_results_graph(app):
    global time_frame, cost_frame

    if not os.path.exists(RESULTS_FILE):
        messagebox.showerror("Error", "There are no saved results!")
        return False

    # citim datele
    sizes, bt_times, bt_costs, hc_times, hc_costs = [], [], [], [], []
    sm_times, sm_costs = [], []
    ga_times, ga_costs = [], []
    with open(RESULTS_FILE) as f:
        next(f)
        for line in f:
            n, bt_t, bt_c, hc_t, hc_c,sm_t,sm_c,ga_t,ga_c = line.strip().split(",")
            sizes.append(int(n))
            bt_times.append(float(bt_t))
            bt_costs.append(float(bt_c))
            hc_times.append(float(hc_t))
            hc_costs.append(float(hc_c))
            sm_times.append(float(sm_t))
            sm_costs.append(float(sm_c))
            ga_times.append(float(ga_t))
            ga_costs.append(float(ga_c))


    if time_frame:
        for w in time_frame.winfo_children(): w.destroy()
    if cost_frame:
        for w in cost_frame.winfo_children(): w.destroy()


    time_frame = ct.CTkFrame(app)
    time_frame.place(relx=0.32, rely=0.03, relwidth=0.63, relheight=0.45)

    cost_frame = ct.CTkFrame(app)
    cost_frame.place(relx=0.32, rely=0.50, relwidth=0.63, relheight=0.45)

    # ─── grafic Timp ──────────────────────────────────────────────────────────
    fig1, ax1 = plt.subplots(figsize=(5,2.5))
    ax1.plot(sizes, bt_times, marker='o', label='Backtracking')
    ax1.plot(sizes, hc_times, marker='s', label='Hill Climbing')
    ax1.plot(sizes, sm_times, marker='^', label='Simulated Annealing')
    ax1.plot(sizes, ga_times, marker='x', label='Genetic Algorithm')
    ax1.set_xlabel("Number of cities")
    ax1.set_ylabel("Time (s)")
    ax1.set_title("Execution Time")
    ax1.legend()
    ax1.grid(True)
    fig1.tight_layout()

    canvas1 = FigureCanvasTkAgg(fig1, master=time_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="top", fill="both", expand=1)

    toolbar1 = NavigationToolbar2Tk(canvas1, time_frame)
    toolbar1.update()
    toolbar1.pack(side="bottom", fill="x")

    # ─── grafic Cost ──────────────────────────────────────────────────────────
    fig2, ax2 = plt.subplots(figsize=(5,2.5))
    ax2.plot(sizes, bt_costs, marker='o', label='Backtracking')
    ax2.plot(sizes, hc_costs, marker='s', label='Hill Climbing')
    ax2.plot(sizes, sm_costs, marker='^', label='Simulated Annealing')
    ax2.plot(sizes, ga_costs, marker='x', label='Genetic Algorithm')
    ax2.set_xlabel("Number of cities")
    ax2.set_ylabel("Cost")
    ax2.set_title("Best Cost")
    ax2.legend()
    ax2.grid(True)
    fig2.tight_layout()

    canvas2 = FigureCanvasTkAgg(fig2, master=cost_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="top", fill="both", expand=1)

    toolbar2 = NavigationToolbar2Tk(canvas2, cost_frame)
    toolbar2.update()
    toolbar2.pack(side="bottom", fill="x")

    return True





def run_algorithms(app, entry):

    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE) as f:
            header = f.readline().strip()
            if header != template:
                messagebox.showerror("Eroare", "The results file does not have the correct format!")
                return
            
    
            
    val = entry.get()
    if not val.isdigit():
        messagebox.showerror("Eroare", "Please enter a valid number for N!")
        return
    n = int(val)
    if n < 1:
        messagebox.showerror("Eroare", "N must be a positive number!")
        return
    
    cities = generate_cities(n)

    bt_time, _, (bt_cost, _) = tsp_backtracking(cities, stop_type='time')


    app.update_status(f"Hill Climbing solved")
    _, sm_cost, sm_time = run_simanneal(cities)
    app.update_status(f"Backtracking solved")
    _, hc_cost, hc_time = hill_climbing_tsp(cities)
    app.update_status(f"Simulated Annealing solved")
    ga_time, ga_cost, _ = genetic_tsp(cities)
    app.update_status(f"Genetic Algorithm solved")

    # Daca fisierul nu exista, adauga header
    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "w") as f:
            f.write(f"{template}\n")

    # Append rezultate
    with open(RESULTS_FILE, "a") as f:
        f.write(f"{n},{bt_time:.6f},{bt_cost},{hc_time:.6f},{hc_cost},{sm_time},{sm_cost},{ga_time},{ga_cost}\n")


def build_menu(app, on_reset_results, on_show_graph, on_show_author):

    def _handle_selection(choice):
        if choice == "Reset Results":
            on_reset_results()
        elif choice == "Show Chart":
            on_show_graph()
        elif choice == "Info Author":
            on_show_author()
        elif choice == "Exit":
            app.quit()
        # re‑seteaza textul afisat
        menu.set("Choose an option")

    menu = ct.CTkOptionMenu(
        app,
        values=["Reset Results", "Show Chart", "Info Author", "Exit"],
        command=_handle_selection,
        width=200
    )
    menu.set("Choose an option")
    menu.pack(side="top", fill="x", padx=5, pady=5)

    return menu