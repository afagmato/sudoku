import tkinter as tk
from tkinter import messagebox
from main import crear_taulell, omplir_taulell, amagar_caselles, es_valid

class SudokuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cell_size = 60
        self.selected = None
        self.taulell = None
        self.fixades = None

        self._crear_widgets()
        self.nova_partida()

    def _crear_widgets(self):
        controls = tk.Frame(self.root)
        controls.pack(pady=10)

        tk.Label(controls, text="Nivell:").pack(side=tk.LEFT)
        self.nivell = tk.StringVar(value="mitja")
        for text, val in [("Fàcil", "facil"), ("Mitjà", "mitja"), ("Difícil", "dificil")]:
            tk.Radiobutton(controls, text=text, variable=self.nivell, value=val).pack(side=tk.LEFT)

        tk.Button(controls, text="Nova partida", command=self.nova_partida).pack(side=tk.LEFT, padx=10)

        mida = self.cell_size * 9 + 4
        self.canvas = tk.Canvas(self.root, width=mida, height=mida, bg="white")
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self._click)
        self.root.bind("<Key>", self._tecla)


    def nova_partida(self):
        self.taulell = crear_taulell()
        omplir_taulell(self.taulell)
        amagar_caselles(self.taulell, self.nivell.get())
        self.fixades = [[self.taulell[f][c] != 0 for c in range(9)] for f in range(9)]
        self.selected = None
        self._dibuixar()

    def _dibuixar(self):
        self.canvas.delete("all")
        cs = self.cell_size

        for f in range(9):
            for c in range(9):
                x1 = c * cs + 2
                y1 = f * cs + 2
                x2 = x1 + cs
                y2 = y1 + cs

                if self.selected == (f, c):
                    color = "#b3d9ff"
                elif self.fixades[f][c]:
                    color = "#f0f0f0"
                else:
                    color = "white"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#cccccc")

                num = self.taulell[f][c]
                if num != 0:
                    color_text = "black" if self.fixades[f][c] else "#1a6bbf"
                    self.canvas.create_text(x1 + cs//2, y1 + cs//2, text=str(num),
                                            font=("Arial", 20, "bold"), fill=color_text)

        for i in range(10):
            gruix = 3 if i % 3 == 0 else 1
            self.canvas.create_line(2, i*cs+2, 9*cs+2, i*cs+2, width=gruix)
            self.canvas.create_line(i*cs+2, 2, i*cs+2, 9*cs+2, width=gruix)

    def _click(self, event):
        cs = self.cell_size
        c = (event.x - 2) // cs
        f = (event.y - 2) // cs
        if 0 <= f <= 8 and 0 <= c <= 8 and not self.fixades[f][c]:
            self.selected = (f, c)
            self._dibuixar()

    def _tecla(self, event):
        if self.selected is None:
            return
        f, c = self.selected
        if event.char in "123456789":
            num = int(event.char)
            if es_valid(self.taulell, f, c, num):
                self.taulell[f][c] = num
                self._dibuixar()
                if all(self.taulell[f][c] != 0 for f in range(9) for c in range(9)):
                    messagebox.showinfo("Sudoku", "Enhorabona! Has completat el sudoku!")
            else:
                messagebox.showwarning("Sudoku", "Moviment no vàlid!")
        elif event.keysym == "BackSpace":
            self.taulell[f][c] = 0
            self._dibuixar()

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuUI(root)
    root.mainloop()
