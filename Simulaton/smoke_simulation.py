import sys
import math
import numpy as np
import pygame

"""
smoke_simulation.py

A simple 2D smoke (stable fluids) simulation using Jos Stam's algorithm (semi-Lagrangian advection
with diffusion and projection). Uses numpy for computation and pygame for visualization & input.

Controls:
 - Left mouse button:  add smoke density
 - Right mouse button drag: add velocity
 - C: clear
 - Esc / window close: quit

Requirements: numpy, pygame
    pip install numpy pygame
"""


# Grid / simulation parameters
GRID_W = 120          # number of cells horizontally
GRID_H = 80           # number of cells vertically
CELL_SIZE = 7         # pixels per cell
DT = 0.1              # time step
DIFF = 0.0001         # diffusion rate for velocity
VISC = 0.0001         # viscosity for velocity projection diffusion (unused separate here)
DENS_DECAY = 0.998    # slight decay to keep simulation bounded
SOLVER_ITERS = 20     # iterations for linear solver

SCREEN_W = GRID_W * CELL_SIZE
SCREEN_H = GRID_H * CELL_SIZE

# Helper: index mapping if using 1D arrays (not used; keep grid 2D)
def in_bounds(i, j):
    return 0 <= i < GRID_W and 0 <= j < GRID_H

# Simulation fields
dens = np.zeros((GRID_H, GRID_W), dtype=np.float32)     # smoke density
dens_prev = np.zeros_like(dens)

u = np.zeros_like(dens)     # velocity x
v = np.zeros_like(dens)     # velocity y
u_prev = np.zeros_like(dens)
v_prev = np.zeros_like(dens)


def add_source(x, s, dt):
    x += dt * s


def set_bnd(b, x):
    # b = 0 for scalar, 1 for x-velocity, 2 for y-velocity
    # reflect velocity on boundaries
    hx, wy = GRID_W, GRID_H
    if b == 1:
        x[:, 0] = -x[:, 1]
        x[:, -1] = -x[:, -2]
    else:
        x[:, 0] = x[:, 1]
        x[:, -1] = x[:, -2]

    if b == 2:
        x[0, :] = -x[1, :]
        x[-1, :] = -x[-2, :]
    else:
        x[0, :] = x[1, :]
        x[-1, :] = x[-2, :]

    # corners
    x[0, 0] = 0.5 * (x[1, 0] + x[0, 1])
    x[0, -1] = 0.5 * (x[1, -1] + x[0, -2])
    x[-1, 0] = 0.5 * (x[-2, 0] + x[-1, 1])
    x[-1, -1] = 0.5 * (x[-2, -1] + x[-1, -2])


def lin_solve(b, x, x0, a, c):
    for _ in range(SOLVER_ITERS):
        x[1:-1, 1:-1] = (x0[1:-1, 1:-1] + a * (
            x[1:-1, 2:] + x[1:-1, 0:-2] + x[2:, 1:-1] + x[0:-2, 1:-1]
        )) / c
        set_bnd(b, x)


def diffuse(b, x, x0, diff, dt):
    a = dt * diff * (GRID_W - 2) * (GRID_H - 2)
    lin_solve(b, x, x0, a, 1 + 4 * a)


def advect(b, d, d0, u, v, dt):
    H, W = d.shape
    dt0x = dt * (W - 2)
    dt0y = dt * (H - 2)
    for j in range(1, H - 1):
        for i in range(1, W - 1):
            x = i - dt0x * u[j, i]
            y = j - dt0y * v[j, i]
            if x < 0.5:
                x = 0.5
            if x > W - 1.5:
                x = W - 1.5
            i0 = int(math.floor(x))
            i1 = i0 + 1
            if y < 0.5:
                y = 0.5
            if y > H - 1.5:
                y = H - 1.5
            j0 = int(math.floor(y))
            j1 = j0 + 1
            s1 = x - i0
            s0 = 1 - s1
            t1 = y - j0
            t0 = 1 - t1
            d[j, i] = (s0 * (t0 * d0[j0, i0] + t1 * d0[j1, i0]) +
                       s1 * (t0 * d0[j0, i1] + t1 * d0[j1, i1]))
    set_bnd(b, d)


def project(u, v, p, div):
    H, W = u.shape
    div[1:-1, 1:-1] = -0.5 * (
        u[1:-1, 2:] - u[1:-1, 0:-2] +
        v[2:, 1:-1] - v[0:-2, 1:-1]
    ) / W
    p.fill(0)
    set_bnd(0, div)
    set_bnd(0, p)
    lin_solve(0, p, div, 1, 4)
    u[1:-1, 1:-1] -= 0.5 * W * (p[1:-1, 2:] - p[1:-1, 0:-2])
    v[1:-1, 1:-1] -= 0.5 * H * (p[2:, 1:-1] - p[0:-2, 1:-1])
    set_bnd(1, u)
    set_bnd(2, v)


def step():
    # velocity step
    add_source(u, u_prev, DT)
    add_source(v, v_prev, DT)
    u_prev.fill(0)
    v_prev.fill(0)

    u_temp = u.copy()
    v_temp = v.copy()
    diffuse(1, u_temp, u, VISC, DT)
    diffuse(2, v_temp, v, VISC, DT)
    advect(1, u, u_temp, u_temp, v_temp, DT)
    advect(2, v, v_temp, u_temp, v_temp, DT)
    p = np.zeros_like(u)
    div = np.zeros_like(u)
    project(u, v, p, div)

    # density step
    add_source(dens, dens_prev, DT)
    dens_prev.fill(0)
    dens_temp = dens.copy()
    diffuse(0, dens_temp, dens, DIFF, DT)
    advect(0, dens, dens_temp, u, v, DT)
    dens *= DENS_DECAY  # small decay to prevent runaway accumulation


def screen_pos_to_cell(pos):
    x, y = pos
    i = int(x / CELL_SIZE)
    j = int(y / CELL_SIZE)
    # clamp to interior (we keep 1-cell boundary for solver)
    i = max(1, min(GRID_W - 2, i))
    j = max(1, min(GRID_H - 2, j))
    return i, j


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("2D Smoke Simulation - GitHub Copilot")
    clock = pygame.time.Clock()

    running = True
    prev_mouse = None

    # Small initial buoyancy: smoke moves upward a bit via a background velocity
    # (optional)
    # v[:, :] = -0.02

    while running:
        dt_ms = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    dens.fill(0)
                    u.fill(0)
                    v.fill(0)
                if event.key == pygame.K_ESCAPE:
                    running = False

        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pressed[0] or mouse_pressed[2]:
            i, j = screen_pos_to_cell(mouse_pos)
            if mouse_pressed[0]:
                # add density
                dens_prev[j, i] += 200.0 * DT  # source amount
            if mouse_pressed[2]:
                # add velocity based on mouse motion
                if prev_mouse is not None:
                    dx = mouse_pos[0] - prev_mouse[0]
                    dy = mouse_pos[1] - prev_mouse[1]
                    fx = dx * 5.0 * DT
                    fy = dy * 5.0 * DT
                    u_prev[j, i] += fx
                    v_prev[j, i] += fy
        prev_mouse = mouse_pos

        # perform simulation step(s)
        step()

        # render density field to screen (map density to grayscale / color)
        screen.fill((0, 0, 0))
        # Convert density to surface by drawing rects; for speed, compute a pygame surface from array
        dens_clamped = np.clip(dens, 0.0, 255.0)
        # create an RGB array (H x W x 3) with colors for smoke (gray-ish)
        # scale to 0-255 range (density already roughly in that range)
        img = np.empty((GRID_H, GRID_W, 3), dtype=np.uint8)
        # smoke color: white-ish with slight tint
        img[:, :, 0] = np.minimum(dens_clamped * 0.7, 255).astype(np.uint8)  # R
        img[:, :, 1] = np.minimum(dens_clamped * 0.7, 255).astype(np.uint8)  # G
        img[:, :, 2] = np.minimum(dens_clamped * 0.8, 255).astype(np.uint8)  # B
        # upscale image to screen size using pygame.surfarray (requires transpose)
        surf = pygame.surfarray.make_surface(np.transpose(img, (1, 0, 2)))
        surf = pygame.transform.scale(surf, (SCREEN_W, SCREEN_H))
        screen.blit(surf, (0, 0))

        # optional: draw velocity vectors (downsampled)
        if False:
            step_v = 6
            for j in range(1, GRID_H - 1, step_v):
                for i in range(1, GRID_W - 1, step_v):
                    x = i * CELL_SIZE + CELL_SIZE // 2
                    y = j * CELL_SIZE + CELL_SIZE // 2
                    vx = u[j, i]
                    vy = v[j, i]
                    pygame.draw.line(screen, (255, 50, 50), (x, y), (x + vx * 20, y + vy * 20), 1)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()