 # tower_defense.py
 # Single-file Tower Defense using Tkinter.
 # Save this file and run: python3 tower_defense.py

import tkinter as tk  # GUI library
import math           # Math functions
import random         # Random number generation
import time           # Time tracking
from collections import deque  # Double-ended queue for enemy spawning

WIDTH = 900      # Window width
HEIGHT = 600     # Window height
GRID_W = 15      # Number of grid columns
GRID_H = 10      # Number of grid rows
CELL_W = WIDTH // GRID_W   # Width of each grid cell
CELL_H = HEIGHT // GRID_H  # Height of each grid cell
TICK_MS = 30    # Game tick interval in milliseconds

# Game parameters
START_MONEY = 150  # Initial player money
START_LIVES = 20   # Initial player lives

# Path: grid cells forming the path
PATH_CELLS = [
    # List of grid cells that form the enemy path
    (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),
    (7,3),(7,2),(8,2),(9,2),(10,2),(11,2),
    (11,3),(11,4),(12,4),(13,4),(14,4)
]

def cell_center(cell):
    # Returns the pixel center of a grid cell
    x, y = cell
    cx = x*CELL_W + CELL_W//2
    cy = y*CELL_H + CELL_H//2
    return (cx, cy)

PATH_POINTS = [cell_center(c) for c in PATH_CELLS]  # List of pixel coordinates for the path

# Tower definitions
TOWER_TYPES = {
    # Dictionary of tower types and their properties
    'basic': {
        'name':'Basic Tower',
        'cost': 50,
        'range': 120,
        'dps': 20,   # damage per second
        'rpm': 1.0,  # shots per second
    },
    'sniper': {
        'name':'Sniper Tower',
        'cost': 120,
        'range': 250,
        'dps': 80,
        'rpm': 0.4,
    },
    'fast': {
        'name':'Rapid Tower',
        'cost': 80,
        'range': 100,
        'dps': 30,
        'rpm': 3.0,
    }
}

class Enemy:
    # Represents an enemy that moves along the path
    def __init__(self, hp, speed, cash_reward):
        self.max_hp = hp           # Maximum health
        self.hp = hp               # Current health
        self.speed = speed         # Movement speed (pixels/sec)
        self.reward = cash_reward  # Money awarded when killed
        self.path_index = 0        # Current position on path
        self.x, self.y = PATH_POINTS[0]  # Current pixel position
        self.reached_end = False   # Has the enemy reached the end?
        self.radius = 10           # Drawing radius
        self.slow = 1.0            # Slow effect multiplier
    
    def update(self, dt):
        # Move the enemy along the path based on speed and time delta
        if self.reached_end:
            return
        if self.path_index + 1 >= len(PATH_POINTS):
            self.reached_end = True
            return
        tx,ty = PATH_POINTS[self.path_index+1]
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx,dy)
        if dist < 1e-6:
            self.path_index += 1
            return
        move = self.speed * self.slow * dt
        if move >= dist:
            self.x = tx
            self.y = ty
            self.path_index += 1
        else:
            self.x += dx/dist * move
            self.y += dy/dist * move

class Tower:
    # Represents a tower placed by the player
    def __init__(self, tx, ty, ttype):
        self.tx = tx                # Grid x position
        self.ty = ty                # Grid y position
        self.x = tx*CELL_W + CELL_W//2  # Pixel x position
        self.y = ty*CELL_H + CELL_H//2  # Pixel y position
        self.type = ttype           # Tower type
        spec = TOWER_TYPES[ttype]   # Tower properties
        self.range = spec['range']  # Attack range
        self.cost = spec['cost']    # Cost to place
        self.dps = spec['dps']      # Damage per second
        self.rpm = spec['rpm']      # Shots per second
        self.cooldown = 0.0         # Time until next shot
        self.target = None          # Current target enemy
    
    def update(self, dt, enemies, projectiles):
        # Update tower logic: acquire target, fire if ready
        if self.target is None or self.target.hp <= 0 or self.distance(self.target) > self.range:
            self.target = None
            best = None
            best_dist = None
            for e in enemies:
                if e.reached_end or e.hp <= 0: continue
                d = self.distance(e)
                if d <= self.range:
                    if best is None or d < best_dist:
                        best = e
                        best_dist = d
            self.target = best
        if self.target is None:
            self.cooldown = max(0.0, self.cooldown - dt)
            return
        if self.cooldown <= 0.0:
            self.fire(projectiles, self.target)
            self.cooldown = 1.0 / self.rpm if self.rpm>0 else 1.0
        else:
            self.cooldown -= dt
    
    def distance(self, enemy):
        # Calculate distance to an enemy
        return math.hypot(self.x - enemy.x, self.y - enemy.y)
    
    def fire(self, projectiles, target):
        # Fire a projectile at the target enemy
        if self.rpm > 0:
            damage = self.dps / self.rpm
        else:
            damage = self.dps
        proj = Projectile(self.x, self.y, target, damage, speed=450)
        projectiles.append(proj)

class Projectile:
    # Represents a projectile fired by a tower
    def __init__(self, x, y, target, damage, speed=400):
        self.x = x              # Current x position
        self.y = y              # Current y position
        self.target = target    # Target enemy
        self.damage = damage    # Damage dealt on hit
        self.speed = speed      # Projectile speed
        self.radius = 4         # Drawing radius
        self.alive = True       # Is the projectile active?
    
    def update(self, dt):
        # Move the projectile toward its target
        if not self.alive or self.target is None or self.target.hp <= 0 or self.target.reached_end:
            self.alive = False
            return
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = math.hypot(dx,dy)
        if dist < 1e-6:
            self.hit_target()
            return
        move = self.speed * dt
        if move >= dist:
            self.x = self.target.x
            self.y = self.target.y
            self.hit_target()
        else:
            self.x += dx/dist * move
            self.y += dy/dist * move
    
    def hit_target(self):
        # Apply damage to the target and deactivate projectile
        if self.target and self.target.hp > 0:
            self.target.hp -= self.damage
        self.alive = False

class Game:
    # Main game class: handles UI, game logic, and rendering
    def __init__(self, root):
        # Initialize game state and UI
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='#e3f2fd')
        self.canvas.pack(side='left')
        self.ui_frame = tk.Frame(root, width=300, height=HEIGHT)
        self.ui_frame.pack(side='right', fill='y')
        self.money = START_MONEY
        self.lives = START_LIVES
        self.wave = 0
        self.enemies = []
        self.towers = []
        self.projectiles = []
        self.wave_spawning = False
        self.spawn_queue = deque()
        self.pause = False
        self.placing_tower_type = None
        self.sell_mode = False
        self.selected_tower = None
        self.last_tick = time.time()
        self.create_ui()
        self.draw_map()
        self.root.after(TICK_MS, self.game_tick)
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<Motion>', self.on_motion)
        self.mouse_pos = (0,0)
        self.info_text_id = None
    
    def create_ui(self):
        # Create UI elements (labels, buttons, info)
        tk.Label(self.ui_frame, text="Python Tower Defense", font=('Helvetica',16,'bold')).pack(pady=8)
        self.money_label = tk.Label(self.ui_frame, text=f"Money: ${self.money}", font=('Helvetica',12))
        self.money_label.pack(pady=4)
        self.lives_label = tk.Label(self.ui_frame, text=f"Lives: {self.lives}", font=('Helvetica',12))
        self.lives_label.pack(pady=4)
        self.wave_label = tk.Label(self.ui_frame, text=f"Wave: {self.wave}", font=('Helvetica',12))
        self.wave_label.pack(pady=4)
        tk.Label(self.ui_frame, text="Towers:", font=('Helvetica',12,'underline')).pack(pady=(10,0))
        for k,v in TOWER_TYPES.items():
            btn = tk.Button(self.ui_frame, text=f"{v['name']} (${v['cost']})", command=lambda t=k: self.select_tower(t), width=20)
            btn.pack(pady=3)
        tk.Button(self.ui_frame, text="Sell Mode (click tower to sell)", command=self.toggle_sell_mode, width=20).pack(pady=6)
        tk.Button(self.ui_frame, text="Start Wave", command=self.start_wave, width=20).pack(pady=6)
        tk.Button(self.ui_frame, text="Pause/Resume", command=self.toggle_pause, width=20).pack(pady=6)
        tk.Button(self.ui_frame, text="Fast Forward ×2", command=self.fast_forward, width=20).pack(pady=6)
        tk.Label(self.ui_frame, text="Info:", font=('Helvetica',12,'underline')).pack(pady=(10,0))
        self.info_label = tk.Label(self.ui_frame, text="Place towers to defend the path.\nEnemies follow the blue path.", justify='left')
        self.info_label.pack(padx=4,pady=4)
        self.log_text = tk.Text(self.ui_frame, height=10, width=34, state='disabled')
        self.log_text.pack(pady=6)
        self.add_log("Welcome! Place towers and stop the enemies.")
    
    def add_log(self, s):
        # Add a message to the log window
        self.log_text.configure(state='normal')
        self.log_text.insert('end', s+"\n")
        self.log_text.see('end')
        self.log_text.configure(state='disabled')
    
    def select_tower(self, ttype):
        # Select a tower type to place
        self.placing_tower_type = ttype
        self.sell_mode = False
        self.add_log(f"Selected {TOWER_TYPES[ttype]['name']} to place. Click a non-path tile to place.")
    
    def toggle_sell_mode(self):
        # Toggle sell mode for towers
        self.sell_mode = not self.sell_mode
        self.placing_tower_type = None
        self.add_log("Sell mode ON" if self.sell_mode else "Sell mode OFF")
    
    def start_wave(self):
        # Start a new wave of enemies
        if self.wave_spawning:
            self.add_log("Wave already spawning.")
            return
        self.wave += 1
        self.wave_label.config(text=f"Wave: {self.wave}")
        num = 5 + self.wave*2
        base_hp = 30 + self.wave*10
        base_speed = 40 + min(self.wave*3, 80)
        for i in range(num):
            hp = base_hp + random.randint(-5,10)
            speed = base_speed + random.uniform(-5,10)
            reward = 8 + self.wave//2
            e = Enemy(hp, speed, reward)
            self.spawn_queue.append((time.time() + 0.6*i, e))
        self.wave_spawning = True
        self.add_log(f"Wave {self.wave} started: {num} enemies incoming.")
    
    def toggle_pause(self):
        # Pause or resume the game
        self.pause = not self.pause
        self.add_log("Paused." if self.pause else "Resumed.")
    
    def fast_forward(self):
        # Temporarily double game speed
        self.add_log("Fast-forward activated for 10 seconds.")
        self.ff_end = time.time() + 10.0
        self.fast_forwarding = True
    
    def draw_map(self):
        # Draw the grid, path, and start/end points
        self.canvas.delete('map')
        for i in range(GRID_W):
            x = i * CELL_W
            self.canvas.create_line(x,0,x,HEIGHT,fill='#cfd8dc', tags='map')
        for j in range(GRID_H):
            y = j * CELL_H
            self.canvas.create_line(0,y,WIDTH,y,fill='#cfd8dc', tags='map')
        for (cx,cy) in PATH_POINTS:
            x0 = cx - CELL_W//2
            y0 = cy - CELL_H//2
            x1 = cx + CELL_W//2
            y1 = cy + CELL_H//2
            self.canvas.create_rectangle(x0,y0,x1,y1, fill='#bbdefb', outline='', tags='map')
        pts = []
        for p in PATH_POINTS:
            pts.extend(p)
        self.canvas.create_line(*pts, width=12, fill='#64b5f6', smooth=True, tags='map')
        sx,sy = PATH_POINTS[0]
        ex,ey = PATH_POINTS[-1]
        self.canvas.create_oval(sx-12,sy-12,sx+12,sy+12, fill='#1e88e5', tags='map')
        self.canvas.create_oval(ex-12,ey-12,ex+12,ey+12, fill='#b71c1c', tags='map')
    
    def on_click(self, event):
        # Handle mouse clicks for placing/selling/selecting towers
        gx = event.x // CELL_W
        gy = event.y // CELL_H
        if gx < 0 or gx >= GRID_W or gy < 0 or gy >= GRID_H:
            return
        if self.placing_tower_type is not None:
            if (gx,gy) in PATH_CELLS:
                self.add_log("Cannot place tower on path.")
                return
            for t in self.towers:
                if t.tx==gx and t.ty==gy:
                    self.add_log("Tower already there.")
                    return
            cost = TOWER_TYPES[self.placing_tower_type]['cost']
            if self.money < cost:
                self.add_log("Not enough money.")
                return
            self.money -= cost
            self.update_ui()
            tw = Tower(gx,gy,self.placing_tower_type)
            self.towers.append(tw)
            self.add_log(f"Placed {TOWER_TYPES[self.placing_tower_type]['name']} at ({gx},{gy}).")
            self.placing_tower_type = None
            return
        if self.sell_mode:
            for t in self.towers:
                if t.tx==gx and t.ty==gy:
                    price = t.cost//2
                    self.money += price
                    self.towers.remove(t)
                    self.add_log(f"Sold tower for ${price}.")
                    self.update_ui()
                    return
            self.add_log("No tower to sell here.")
            return
        for t in self.towers:
            if t.tx==gx and t.ty==gy:
                self.selected_tower = t
                self.add_log(f"Selected tower at ({gx},{gy}). DPS: {t.dps}, Range: {t.range}, Sell for ${t.cost//2}")
                return
        self.selected_tower = None
    
    def on_motion(self, event):
        # Track mouse position for UI feedback
        self.mouse_pos = (event.x, event.y)
    
    def update_ui(self):
        # Update UI labels for money, lives, wave
        self.money_label.config(text=f"Money: ${self.money}")
        self.lives_label.config(text=f"Lives: {self.lives}")
        self.wave_label.config(text=f"Wave: {self.wave}")
    
    def spawn_logic(self):
        # Spawn enemies from the queue at the correct time
        now = time.time()
        while self.spawn_queue and self.spawn_queue[0][0] <= now:
            _, e = self.spawn_queue.popleft()
            self.enemies.append(e)
        if not self.spawn_queue:
            self.wave_spawning = False
    
    def game_tick(self):
        # Main game loop: update all entities, redraw, schedule next tick
        now = time.time()
        dt = now - self.last_tick if not self.pause else 0.0
        speed_multiplier = 1.0
        if hasattr(self, 'fast_forwarding') and self.fast_forwarding:
            if time.time() > getattr(self,'ff_end',0):
                self.fast_forwarding = False
            else:
                speed_multiplier = 2.0
        dt *= speed_multiplier
        if not self.pause:
            self.spawn_logic()
        to_remove = []
        for e in list(self.enemies):
            e.update(dt)
            if e.reached_end:
                self.lives -= 1
                to_remove.append(e)
                self.add_log("An enemy reached the end! -1 life.")
            elif e.hp <= 0:
                self.money += e.reward
                to_remove.append(e)
                self.add_log(f"Enemy killed! +${e.reward}")
        for e in to_remove:
            if e in self.enemies:
                self.enemies.remove(e)
        for t in self.towers:
            t.update(dt, self.enemies, self.projectiles)
        for p in list(self.projectiles):
            p.update(dt)
            if not p.alive:
                self.projectiles.remove(p)
        if self.lives <= 0:
            self.add_log("Game over! All lives lost.")
            self.pause = True
            self.lives = 0
        self.redraw()
        self.update_ui()
        self.last_tick = now
        self.root.after(TICK_MS, self.game_tick)
    
    def redraw(self):
        # Redraw all game entities (towers, enemies, projectiles, info)
        self.canvas.delete('entities')
        for t in self.towers:
            x = t.x; y = t.y
            r = 18
            self.canvas.create_oval(x-r,y-r,x+r,y+r, fill='#8bc34a', tags='entities')
            if t is self.selected_tower:
                self.canvas.create_oval(x-t.range,y-t.range,x+t.range,y+t.range, outline='#2e7d32', dash=(4,4), tags='entities')
        for p in self.projectiles:
            self.canvas.create_oval(p.x-p.radius,p.y-p.radius,p.x+p.radius,p.y+p.radius, fill='#ffeb3b', tags='entities')
        for e in self.enemies:
            x = e.x; y = e.y
            r = e.radius
            hp_frac = max(0, e.hp / e.max_hp)
            color = '#ef5350' if hp_frac < 0.4 else '#66bb6a'
            self.canvas.create_oval(x-r,y-r,x+r,y+r, fill=color, tags='entities')
            self.canvas.create_rectangle(x-12,y-18,x+12,y-14, fill='#bdbdbd', tags='entities')
            self.canvas.create_rectangle(x-12,y-18, x-12 + 24*hp_frac, y-14, fill='#76ff03', tags='entities')
        if self.placing_tower_type is not None:
            mx,my = self.mouse_pos
            gx = mx // CELL_W
            gy = my // CELL_H
            if 0 <= gx < GRID_W and 0 <= gy < GRID_H and (gx,gy) not in PATH_CELLS and not any(t.tx==gx and t.ty==gy for t in self.towers):
                px = gx*CELL_W + CELL_W//2
                py = gy*CELL_H + CELL_H//2
                self.canvas.create_oval(px-18,py-18,px+18,py+18, outline='#2e7d32', dash=(3,3), tags='entities')
                rng = TOWER_TYPES[self.placing_tower_type]['range']
                self.canvas.create_oval(px-rng,py-rng,px+rng,py+rng, outline='#2e7d32', dash=(3,3), tags='entities')
        mx,my = self.mouse_pos
        info = ""
        for e in self.enemies:
            if math.hypot(mx-e.x, my-e.y) < max(12, e.radius):
                info = f"Enemy HP: {int(e.hp)}/{int(e.max_hp)}\nSpeed: {int(e.speed)}\nReward: ${e.reward}"
                break
        if self.selected_tower:
            t = self.selected_tower
            info = f"Tower: {TOWER_TYPES[t.type]['name']}\nDPS: {t.dps}\nRange: {t.range}\nSell for ${t.cost//2}"
        if info:
            if self.info_text_id:
                self.canvas.delete(self.info_text_id)
            self.info_text_id = self.canvas.create_text( WIDTH-150, 40, text=info, anchor='ne', font=('Helvetica',10), tags='entities')
        else:
            if self.info_text_id:
                self.canvas.delete(self.info_text_id)
                self.info_text_id = None

def main():
    # Entry point: create window and start game
    root = tk.Tk()
    root.title("Python Tower Defense - Single File")
    game = Game(root)
    root.mainloop()

if __name__ == '__main__':
    main()
