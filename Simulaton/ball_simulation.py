import tkinter as tk
import time
import math

# ball_simulation.py
# Simple bouncing ball simulation using tkinter
# Run: python ball_simulation.py


WIDTH, HEIGHT = 800, 600
GRAVITY = 980.0       # pixels per second^2
DT = 1 / 60.0         # simulation timestep (seconds)
ELASTICITY = 0.78     # coefficient of restitution (0..1)
AIR_DRAG = 0.0        # simple linear drag coefficient (0..1)

class Ball:
    def __init__(self, x, y, vx, vy, radius=20, color="red"):
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
        self.r = radius
        self.color = color

    def step(self, dt):
        # Integrate acceleration -> velocity -> position (simple Euler)
        self.vy += GRAVITY * dt
        # apply simple air drag
        self.vx *= (1.0 - AIR_DRAG * dt)
        self.vy *= (1.0 - AIR_DRAG * dt)
        self.x += self.vx * dt
        self.y += self.vy * dt

    def handle_collisions(self, width, height, elasticity):
        # Left wall
        if self.x - self.r < 0:
            self.x = self.r
            self.vx = -self.vx * elasticity
        # Right wall
        if self.x + self.r > width:
            self.x = width - self.r
            self.vx = -self.vx * elasticity
        # Ceiling
        if self.y - self.r < 0:
            self.y = self.r
            self.vy = -self.vy * elasticity
        # Floor
        if self.y + self.r > height:
            self.y = height - self.r
            self.vy = -self.vy * elasticity
            # small threshold to stop jitter when nearly resting
            if abs(self.vy) < 1.0:
                self.vy = 0.0

class Simulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bouncing Ball Simulation")
        self.resizable(False, False)
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()
        # Create a ball near top-left with some initial velocity
        self.ball = Ball(x=100, y=80, vx=150, vy=0, radius=22, color="blue")
        self.ball_id = None
        self.running = True
        self.last_time = time.time()
        self.bind("<space>", self.toggle_pause)
        self.bind("r", self.reset)
        self.bind("e", self.increase_elasticity)
        self.bind("d", self.decrease_elasticity)
        self.draw()
        self.after(int(DT * 1000), self.update_loop)

    def draw(self):
        self.canvas.delete("all")
        b = self.ball
        x0 = b.x - b.r
        y0 = b.y - b.r
        x1 = b.x + b.r
        y1 = b.y + b.r
        self.canvas.create_oval(x0, y0, x1, y1, fill=b.color, outline="black")
        # Display info
        info = f"vx={b.vx:.1f} vy={b.vy:.1f} elasticity={ELASTICITY:.2f} (space pause, r reset, e/d adjust)"
        self.canvas.create_text(10, 10, anchor="nw", text=info, fill="black", font=("TkDefaultFont", 10))

    def update_loop(self):
        global ELASTICITY
        now = time.time()
        # Use fixed dt for stability; optional small correction for real time
        steps = 1
        for _ in range(steps):
            if self.running:
                self.ball.step(DT)
                self.ball.handle_collisions(WIDTH, HEIGHT, ELASTICITY)
        self.draw()
        self.after(int(DT * 1000), self.update_loop)

    def toggle_pause(self, event=None):
        self.running = not self.running

    def reset(self, event=None):
        global ELASTICITY
        ELASTICITY = 0.78
        self.ball = Ball(x=100, y=80, vx=150, vy=0, radius=22, color="blue")

    def increase_elasticity(self, event=None):
        global ELASTICITY
        ELASTICITY = min(1.0, ELASTICITY + 0.05)

    def decrease_elasticity(self, event=None):
        global ELASTICITY
        ELASTICITY = max(0.0, ELASTICITY - 0.05)

if __name__ == "__main__":
    app = Simulation()
    app.mainloop()