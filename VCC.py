import VirGPT
import VirSave
import VirStar

from tkinter import messagebox
import tkinter as tk
import threading

startest = VirSave.load("stars", "str")

if startest:
    star = int(startest)
else:
    star = 0

stardishtest = VirSave.load("dish", "str")

if stardishtest:
    stardish = stardishtest
else:
    stardish = ""

root = tk.Tk()
root.title('VCC')

chaos = 0

ing1 = VirSave.load("ing1", "str")
ing2 = VirSave.load("ing2", "str")

menu = tk.Menu(root, tearoff=0)

def show_star():
    global star, stardish
    rep = ['i'] * star
    starstring = ""
    for r in rep:
        starstring = starstring + '⭐'
    if stardish:
        messagebox.showinfo('StarBoard', f'{stardish}: {starstring}')
    else:
        messagebox.showinfo('StarBoard', 'Nothing to see here...')

menu.add_command(label='Star Board', command=show_star)

def handle(value):
    global chaos
    chaos = value

def popup(event):
    menu.post(event.x_root, event.y_root)

entry = tk.Entry(root)
entry.pack()


def cook(a, bc):
    global chaos, star, stardish
    master_prompt = f"""
Create an outlandish and creative dish name

RULES:
- Output ONLY the dish name
- NO explanation
- NO extra text
- NO punctuation after the name
- STOP immediately after the name

INPUT:
Ingredients: {a} and {bc}
Chaos level: {chaos}

"""
    chaos = 0

    print(master_prompt)

    output = VirGPT.askAI(master_prompt)
    print(output)

    stars = VirStar.test(output)
    if stars >= star:
        star = stars
        stardish = output
    print(star)
    VirSave.save(star, "stars")
    VirSave.save(stardish, "dish")

    outp.config(text=output)

    b.config(state='normal')

def finish_cook(a, b):
    cook(a, b)

def update_ui():
    global ing1, ing2

    if ing1 and ing2:
        outp.config(text=f"{ing1} + {ing2}")
        b.config(text='Cook')

    elif ing1:
        outp.config(text=ing1)

    else:
        outp.config(text='Create anything!')

    print(ing1 + ', ' + ing2)


def stuff():
    global ing1, ing2

    if not ing1 and not ing2:
        ing1 = entry.get()

        VirSave.save(ing1, "ing1")

        outp.config(text=ing1)

    elif ing1 and not ing2:
        ing2 = entry.get()

        VirSave.save(ing2, "ing2")

        outp.config(text=f'{ing1} + {ing2}')

        b.config(text='Cook')

    elif ing1 and ing2:
        outp.config(text='Thinking...')

        root.update()
        b.config(state="disabled")
        threading.Thread(
            target=finish_cook,
            args=(ing1, ing2),
            daemon=True
        ).start()

        ing1 = ""
        ing2 = ""

        VirSave.save("", "ing1")
        VirSave.save("", "ing2")

        b.config(text='Send')

    entry.delete(0, tk.END)

    print(ing1 + ', ' + ing2)


cs = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    label="Chaos Level",
    command=handle
)

cs.pack()

b = tk.Button(root, text='Send', command=stuff)
b.pack()

outp = tk.Label(root, text='Create anything!')
outp.pack()

update_ui()

root.bind('<Button-3>', popup)

root.mainloop()