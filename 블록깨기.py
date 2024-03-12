import tkinter as tk
import random

# 게임 설정
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 5, 5
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 10
BALL_RADIUS = 10
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 20
BALL_SPEED = 5
PADDLE_SPEED = 20
BLOCK_COLOR = "#3498db"
PADDLE_COLOR = "#2ecc71"
BALL_COLOR = "#e74c3c"

class BlockBreaker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - PADDLE_HEIGHT - 20,
                                                   WIDTH//2 + PADDLE_WIDTH//2, HEIGHT - 20, fill=PADDLE_COLOR)
        self.ball = self.canvas.create_oval(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS,
                                            WIDTH//2 + BALL_RADIUS, HEIGHT//2 + BALL_RADIUS, fill=BALL_COLOR)

        self.blocks = []
        for i in range(ROWS):
            for j in range(COLS):
                x1 = j * BLOCK_WIDTH
                y1 = i * BLOCK_HEIGHT
                x2 = x1 + BLOCK_WIDTH
                y2 = y1 + BLOCK_HEIGHT
                self.blocks.append(self.canvas.create_rectangle(x1, y1, x2, y2, fill=BLOCK_COLOR))

        self.canvas.focus_set()
        self.canvas.bind("<Left>", self.move_paddle_left)
        self.canvas.bind("<Right>", self.move_paddle_right)

        self.dx = BALL_SPEED
        self.dy = BALL_SPEED
        self.running = True
        self.update()

    def move_paddle_left(self, event):
        self.canvas.move(self.paddle, -PADDLE_SPEED, 0)

    def move_paddle_right(self, event):
        self.canvas.move(self.paddle, PADDLE_SPEED, 0)

    def update(self):
        if not self.running:
            return

        self.canvas.move(self.ball, self.dx, self.dy)

        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle)

        if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
            self.dx *= -1
        if ball_pos[1] <= 0:
            self.dy *= -1
        if ball_pos[3] >= HEIGHT:
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill="white", font=("Arial", 30))
        
        if ball_pos[1] <= paddle_pos[3] and ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            self.dy *= -1

        for block in self.blocks:
            block_pos = self.canvas.coords(block)
            if ball_pos[1] <= block_pos[3] and ball_pos[3] >= block_pos[1] and ball_pos[0] <= block_pos[2] and ball_pos[2] >= block_pos[0]:
                self.dy *= -1
                self.canvas.delete(block)
                self.blocks.remove(block)

        if not self.blocks:
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="You Win!", fill="white", font=("Arial", 30))

        self.after(20, self.update)

if __name__ == "__main__":
    game = BlockBreaker()
    game.mainloop()
