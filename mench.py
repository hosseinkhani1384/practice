import tkinter as tk
from PIL import Image, ImageTk
from random import randint

def generate_player_path():
    path = []
    path.extend([(5, y) for y in range(11, 6, -1)])
    path.extend([(x, 7) for x in range(4, 0, -1)])
    path.extend([(1, y) for y in range(6, 4, -1)])
    path.extend([(x, 5) for x in range(2, 6)])
    path.extend([(5, y) for y in range(4, 0, -1)])
    path.extend([(x, 1) for x in range(6, 8)])
    path.extend([(7, y) for y in range(2, 6)])
    path.extend([(x, 5) for x in range(8, 12)])
    path.extend([(11, y) for y in range(6, 8)])
    path.extend([(x, 7) for x in range(10, 6, -1)])
    path.extend([(7, y) for y in range(8, 12)])
    path.append((6, 11))
    path.extend([(6, y) for y in range(10, 6, -1)])
    return path

def generate_ai_path():
    path = []
    path.extend([(7, y) for y in range(1, 6)])
    path.extend([(x, 5) for x in range(8, 12)])
    path.extend([(11, y) for y in range(6, 8)])
    path.extend([(x, 7) for x in range(10, 6, -1)])
    path.extend([(7, y) for y in range(8, 12)])
    path.extend([(x, 11) for x in range(6, 4, -1)])
    path.extend([(5, y) for y in range(10, 6, -1)])
    path.extend([(x, 7) for x in range(4, 0, -1)])
    path.extend([(1, y) for y in range(6, 4, -1)])
    path.extend([(x, 5) for x in range(2, 6)])
    path.extend([(5, y) for y in range(4, 0, -1)])
    path.append((6, 1))
    path.extend([(6, y) for y in range(2, 6)])
    return path

class GameApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("700x700")
        self.window.title("Game")
        self.window.resizable(False, False)
        self.turn = 0
        self.dice_value = 0
        self.move_allowed = True

        self.player_path = generate_player_path()
        self.ai_path = generate_ai_path()

        self.init_ui()

    def init_ui(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill="both", expand=True)

        self.create_color_buttons()

    def create_color_buttons(self):
        self.red_button = tk.Button(self.main_frame, text="Red", command=lambda: self.set_paths("Red"), bg="Red", fg="white")
        self.red_button.place(relheight=1, relwidth=0.5, rely=0, relx=0)

        self.blue_button = tk.Button(self.main_frame, text="Blue", command=lambda: self.set_paths("Blue"), bg="Blue", fg="white")
        self.blue_button.place(relheight=1, relwidth=0.5, rely=0, relx=0.5)

    def set_paths(self, chosen_color):
        if chosen_color == "Red":
            self.player_route = self.player_path
            self.ai_route = self.ai_path
        else:
            self.player_route = self.ai_path
            self.ai_route = self.player_path
        self.main_frame.destroy()
        self.create_game_board(chosen_color)

    def create_game_board(self, player_color):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill="both", expand=True)
        self.set_background_image("assets/bg.jpg")
        self.create_pieces(player_color)
        self.create_dice_button()
        self.create_turn_label()

    def set_background_image(self, image_path):
        self.bg_image = Image.open(image_path)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.main_frame, image=self.bg_image_tk)
        self.bg_label.place(relheight=1, relwidth=1)
        
    def create_pieces(self, player_color):
        self.create_piece("Player", player_color, self.player_route)
        ai_color = "Blue" if player_color == "Red" else "Red"
        self.create_piece("AI", ai_color, self.ai_route)

    def create_piece(self, text, color, path):
        piece = tk.Button(self.main_frame, border=0, text=text, bg=color, fg="#ffffff")
        piece.pos = 0
        piece.path = path
        piece.place(relheight=1/13, relwidth=1/13)
        self.update_position(piece)
        if text == "Player":
            self.player_piece = piece
            self.player_piece.config(command=self.player_move)
        else:
            self.ai_piece = piece

    def create_dice_button(self):
        self.dice_button = tk.Button(self.main_frame, text="Roll Dice", command=self.roll_dice)
        self.dice_button.place(relheight=1/13, relwidth=1/13, relx=9/13, rely=9/13)

    def create_turn_label(self):
        self.turn_label = tk.Label(self.main_frame, text="Player's Turn", font=("Arial", 16))
        self.turn_label.place(relheight=1/13, relwidth=1/2, relx=0.25, rely=12/13)

    def update_turn_label(self):
        self.turn_label.config(text="Player's Turn" if self.turn == 0 else "AI's Turn")

    def roll_dice(self):
        if self.move_allowed:
            self.dice_value = randint(1, 6)
            self.dice_button.config(text=self.dice_value)
            self.move_allowed = False
            if self.turn == 0:
                self.player_piece.config(state="normal")
            else:
                self.window.after(1000, self.ai_move)

    def player_move(self):
        self.player_piece.config(state="disabled")
        self.move_piece(self.player_piece)
        self.turn = 1
        self.update_turn_label()
        self.window.after(1000, self.ai_roll_dice)

    def ai_roll_dice(self):
        self.dice_value = randint(1, 6)
        self.dice_button.config(text=self.dice_value)
        self.window.after(1000, self.ai_move)

    def ai_move(self):
        self.move_piece(self.ai_piece)
        self.turn = 0
        self.update_turn_label()
        self.move_allowed = True
        self.dice_button.config(state="normal")

    def move_piece(self, piece):
        new_pos = piece.pos + self.dice_value
        if new_pos < len(piece.path):
            piece.pos = new_pos
            self.update_position(piece)
            if self.check_collision(self.player_piece, self.ai_piece):
                self.reset_piece(self.ai_piece if piece == self.player_piece else self.player_piece)
            if self.check_win(piece):
                self.end_game(piece.cget("text"))
            elif self.dice_value == 6:
                if piece == self.player_piece:
                    self.move_allowed = True
                    self.dice_button.config(state="normal")
                else:
                    self.window.after(1000, self.ai_roll_dice)
            else:
                self.turn = 1 if piece == self.player_piece else 0
                self.move_allowed = True
                self.dice_button.config(state="normal")

    def update_position(self, piece):
        relx = piece.path[piece.pos][0] / 13
        rely = piece.path[piece.pos][1] / 13
        piece.place(relx=relx, rely=rely)

    def check_collision(self, piece1, piece2):
        return piece1.path[piece1.pos] == piece2.path[piece2.pos]

    def reset_piece(self, piece):
        piece.pos = 0
        self.update_position(piece)

    def check_win(self, piece):
        return piece.pos == len(piece.path) - 1

    def end_game(self, winner):
        self.main_frame.destroy()
        end_frame = tk.Frame(self.window)
        end_frame.pack(fill="both", expand=True)
        tk.Label(end_frame, text=f"{winner} Wins!", font=("Arial", 32)).pack(expand=True)

if __name__ == "__main__":
    window = tk.Tk()
    app = GameApp(window)
    window.mainloop()
