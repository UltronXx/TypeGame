import customtkinter as ctk
import keyboard


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Type Game")
        self.geometry("600x300")

        # Move from letter to letter
        self.iterator = 1
        self.length_of_text = 0

        self.sentence = ctk.CTkTextbox(
            master=self,
            height=150,
            width=1050,
            fg_color="#028395",
            text_color="black",
            corner_radius=14,
            font=("Cascadia Mono SemiBold", 15)
        )
        self.sentence.pack()

        self.button_a = ctk.CTkButton(
            master=self,
            text="a",
            height=40,
            width=100,
            corner_radius=12,
            command=lambda: self.key_press(self.button_a.cget("text"))
        )
        self.button_a.pack(pady=6)

        self.button_b = ctk.CTkButton(
            master=self,
            text="b",
            height=40,
            width=100,
            corner_radius=12,
            command=lambda: self.key_press(self.button_b.cget("text"))
        )
        self.button_b .pack(pady=6)

        self.button_space = ctk.CTkButton(
            master=self,
            text=" ",
            height=40,
            width=180,
            corner_radius=12,
            command=lambda: self.key_press(self.button_space.cget("text"))
        )
        self.button_space.pack(pady=6)

        self.sentence.insert("end", "aaba bbba ababa")
        self.length_of_text = len(self.sentence.get("0.0", "end"))



    def change_color(self, value: str):
        self.sentence.tag_add(tagName="mytag", index1="1.0", index2=value)
        self.sentence.tag_config(tagName="mytag", foreground="white")

    def key_press(self, key_text):
        typed = "1." + str(self.iterator)
        previous = "1." + str(self.iterator - 1)
        current_letter = self.sentence.get(index1=previous, index2=typed)

        if self.is_correct_letter(pressed=key_text, current_letter=current_letter):
            if not self.is_end_of_text():
                self.change_color(value=typed)
                self.iterator += 1

    def is_correct_letter(self, pressed, current_letter):
        if pressed == current_letter:
            return True
        return False

    def is_end_of_text(self):
        if self.iterator < self.length_of_text:
            return False
        return True

    def key_presses(self):
        while self.iterator < self.length_of_text:
            typed = "1." + str(self.iterator)
            previous = "1." + str(self.iterator - 1)
            current_letter = self.sentence.get(index1=previous, index2=typed)

            keyboard.wait(current_letter)
            print(f"You pressed {current_letter}")
            self.iterator += 1


if __name__ == "__main__":
    app = App()
    app.mainloop()
    app.key_presses()

