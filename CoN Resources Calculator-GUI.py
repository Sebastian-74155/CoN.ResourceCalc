import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

SPEEDS = {"1x (default)": 1, "4x": 4, "10x": 10}


def calculate(resources, rate, speed, real_hours, real_minutes, start=None):
    """Return (end_datetime, in_game_hours, final_resources, days_later)."""
    start = start or datetime.now()
    real_td = timedelta(hours=real_hours, minutes=real_minutes)
    in_game_hours = real_td.total_seconds() / 3600 * speed
    final = resources + rate * in_game_hours
    end = start + real_td
    days_later = (end.date() - start.date()).days
    return end, in_game_hours, final, days_later


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conflict of Nations - Resources Calculator")
        self.resizable(False, False)

        self.speed_var = tk.StringVar(value="1x (default)")
        self.res_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.hours_var = tk.StringVar(value="0")
        self.minutes_var = tk.StringVar(value="0")
        self.clock_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Enter your values and press Calculate.")
        self.detail_var = tk.StringVar()

        self._build()
        self._tick()
        self.bind("<Return>", lambda e: self.on_calculate())

    def _build(self):
        pad = {"padx": 10, "pady": 5}
        frm = ttk.Frame(self, padding=15)
        frm.grid(row=0, column=0)

        ttk.Label(frm, text="Resources Calculator",
                  font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=(0, 2))
        ttk.Label(frm, textvariable=self.clock_var,
                  foreground="gray").grid(row=1, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(frm, text="Game speed:").grid(row=2, column=0, sticky="w", **pad)
        ttk.Combobox(frm, textvariable=self.speed_var, values=list(SPEEDS),
                     state="readonly", width=14).grid(row=2, column=1, columnspan=2, sticky="w", **pad)

        ttk.Label(frm, text="Current resources:").grid(row=3, column=0, sticky="w", **pad)
        res_entry = ttk.Entry(frm, textvariable=self.res_var, width=17)
        res_entry.grid(row=3, column=1, columnspan=2, sticky="w", **pad)

        ttk.Label(frm, text="Production per in-game hour:").grid(row=4, column=0, sticky="w", **pad)
        ttk.Entry(frm, textvariable=self.rate_var, width=17).grid(row=4, column=1, columnspan=2, sticky="w", **pad)

        ttk.Label(frm, text="Real-time wait:").grid(row=5, column=0, sticky="w", **pad)
        wait = ttk.Frame(frm)
        wait.grid(row=5, column=1, columnspan=2, sticky="w", **pad)
        ttk.Spinbox(wait, from_=0, to=9999, textvariable=self.hours_var, width=5).pack(side="left")
        ttk.Label(wait, text="h ").pack(side="left")
        ttk.Spinbox(wait, from_=0, to=59, textvariable=self.minutes_var, width=4).pack(side="left")
        ttk.Label(wait, text="min").pack(side="left")

        btns = ttk.Frame(frm)
        btns.grid(row=6, column=0, columnspan=3, pady=10)
        ttk.Button(btns, text="Calculate", command=self.on_calculate).pack(side="left", padx=5)
        ttk.Button(btns, text="Clear", command=self.on_clear).pack(side="left", padx=5)

        ttk.Separator(frm).grid(row=7, column=0, columnspan=3, sticky="ew", pady=5)
        ttk.Label(frm, textvariable=self.result_var, font=("Segoe UI", 11, "bold"),
                  wraplength=360, justify="center").grid(row=8, column=0, columnspan=3, pady=(5, 2))
        ttk.Label(frm, textvariable=self.detail_var, foreground="gray",
                  justify="center").grid(row=9, column=0, columnspan=3)

        res_entry.focus()

    def _tick(self):
        self.clock_var.set("Current time: " + datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self._tick)

    @staticmethod
    def _num(text):
        return float(text.strip().replace(",", ""))

    def on_calculate(self):
        try:
            resources = self._num(self.res_var.get())
            rate = self._num(self.rate_var.get())
            hours = self._num(self.hours_var.get() or "0")
            minutes = self._num(self.minutes_var.get() or "0")
            if hours < 0 or minutes < 0:
                raise ValueError
        except ValueError:
            self.result_var.set("Please enter valid, non-negative numbers.")
            self.detail_var.set("")
            return

        speed = SPEEDS[self.speed_var.get()]
        end, ig_hours, final, days_later = calculate(resources, rate, speed, hours, minutes)

        when = end.strftime("%H:%M")
        if days_later == 1:
            when += " (next day)"
        elif days_later > 1:
            when += f" (+{days_later} days)"

        self.result_var.set(f"At {when}, your resources will be {final:,.0f}")
        self.detail_var.set(f"{ig_hours:,.1f} in-game hours will have passed\n"
                            f"Gain: +{final - resources:,.0f}")

    def on_clear(self):
        self.res_var.set("")
        self.rate_var.set("")
        self.hours_var.set("0")
        self.minutes_var.set("0")
        self.result_var.set("Enter your values and press Calculate.")
        self.detail_var.set("")


if __name__ == "__main__":
    App().mainloop()