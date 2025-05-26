import customtkinter as ct
from .meniu import build_menu, run_algorithms, show_results_graph, reset_results
from collections import deque




info_autor_open = False


class App(ct.CTk):

    def __init__(self):
        super().__init__()
        self.title("AVE Application")
        self.geometry("800x600")
        
        # ── STATUS BAR ───────────────────────────────
        self.status = ct.CTkLabel(self, text="🔹 Ready", anchor="w")
        self.status.pack(side="bottom", fill="x", padx=5, pady=5)
        self.status_history = deque(maxlen=10)
        
        # ── LEFT PANEL ───────────────────────────────
        left_panel = ct.CTkFrame(self)
        left_panel.pack(side="left", fill="y", padx=10, pady=10)
        
        # Menu dropdown
        self.menu_opt = build_menu(
            left_panel,
            on_reset_results=self.reset_results,
            on_show_graph=self.show_graph,
            on_show_author=self.show_author_info
        )
        
        ct.CTkLabel(left_panel, text="").pack(pady=5)
        
        # Label + Entry for N
        self.size_label = ct.CTkLabel(left_panel, text="Number of cities:")
        self.size_label.pack(anchor="w", pady=(10, 2))
        
        self.size_entry = ct.CTkEntry(left_panel, width=80)
        self.size_entry.pack(anchor="w", pady=(0, 10))
        self.size_entry.insert(0, "8")  # Default value for N



        
        self.run_button = ct.CTkButton(
            left_panel, text="Run algorithm", command=self.run_tests
        )
        self.run_button.pack(anchor="w", pady=(0, 10))

    def update_status(self,msg: str):
        self.status_history.append(msg)
        self.status.configure(text="\n".join(msg for msg in self.status_history))
        self.status.update_idletasks()

    def run_tests(self):
        n = self.size_entry.get()
        # Simulate test execution
        run_algorithms(self, self.size_entry)

        self.update_status("✅ Tests finished.")

    def show_graph(self):
        show_results_graph(self)
        self.update_status("📊 Graphic displayed.")


    def close_info_autor(self, window):
        global info_autor_open
        info_autor_open = False
        window.destroy
        

    def show_author_info(self):
        global info_autor_open

        if info_autor_open:
            return
        
        info_autor_open = True
        # Create a toplevel window for the author info
        author_window = ct.CTkToplevel(self)
        author_window.title("Author Information")
        author_window.geometry("300x200")  # Adjust size as needed
        author_window.protocol("WM_DELETE_WINDOW", self.close_info_autor(author_window))

        # Add author information (replace with your details)
        author_label = ct.CTkLabel(author_window,font=ct.CTkFont("Arial",15), text="...")
        author_label.place(relx=0.5, rely=0.5, anchor="center")
        # ... (Add other author details like email, etc.) ...
        self.update_status("ℹ️ Info Author")

    def reset_results(self):
        reset_results()
        self.update_status("🔄 Results reset.")
        
