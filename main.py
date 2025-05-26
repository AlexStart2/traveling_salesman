from src.gui.main_window import App
import matplotlib.pyplot as plt

if __name__ == "__main__":
    app = App()
    def on_closing():
        plt.close('all')
        app.quit()

    app.protocol("WM_DELETE_WINDOW", on_closing)

    app.mainloop()



