import keyboard

to_press = ["a", "b", "c", "d"]
iterator = 0

def key_presses(self):
    while iterator < len(to_press):
        keyboard.wait(to_press[iterator])
        print(f"You pressed {to_press[iterator]}")
        iterator += 1
