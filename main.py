import customtkinter as ctk


class Game(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configurations
        # Window height and width (Size)
        self.height, self.width = str(650), str(1300)

        self.title("Type Game")
        self.geometry(f"{self.width}x{self.height}")

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        # Game Container
        self.game_frame = ctk.CTkFrame(
            master=self,
            height=200,
            width=200,
            fg_color="#0295A9",
            corner_radius=0
        )
        self.game_frame.grid(row=0, column=0, sticky="news")
        self.game_frame.grid_columnconfigure(index=0, weight=1)
        self.game_frame.grid_rowconfigure(index=2, weight=2)

        # Sign Up/Sign In
        self.game_name = ctk.CTkLabel(
            master=self.game_frame,
            text="TypeGame",
            text_color="white",
            font=("Cascadia Mono Bold", 35)
        )
        self.game_name.grid(row=0, column=0, pady=(60, 0))

        self.game_version = ctk.CTkLabel(
            master=self.game_frame,
            text="Version 1.0.0",
            text_color="white",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.game_version.grid(row=1, column=0)

        self.signup_frame = ctk.CTkFrame(
            master=self.game_frame,
            height=300,
            width=250,
            fg_color="#02AFC7",
            corner_radius=20
        )
        self.signup_frame.grid(row=2, column=0)

        self.hello_there = ctk.CTkLabel(
            master=self.signup_frame,
            text="Hello, there!",
            text_color="white",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.hello_there.grid(row=0, column=0, padx=0, pady=(20, 25))

        self.username = ctk.CTkEntry(
            master=self.signup_frame,
            placeholder_text="Username",
            height=35,
            width=200,
            corner_radius=10,
            border_width=0,
            font=("Cascadia Mono Bold", 13)
        )
        self.username.grid(row=1, column=0)

        self.level = ctk.CTkEntry(
            master=self.signup_frame,
            placeholder_text="Level",
            height=35,
            width=200,
            corner_radius=10,
            border_width=0,
            font=("Cascadia Mono Bold", 13)
        )
        self.level.grid(row=2, column=0, padx=30, pady=(10, 20))

        self.start_button = ctk.CTkButton(
            master=self.signup_frame,
            text_color="#121212",
            text="Start",
            height=35,
            width=100,
            corner_radius=12,
            fg_color="#FDD037",
            hover_color="#FCE186",
            font=("Cascadia Mono Bold", 13)
        )
        self.start_button.grid(row=3, column=0, pady=(20, 25))

        self.designer = ctk.CTkLabel(
            master=self.game_frame,
            text="Designed by Ultron",
            text_color="white",
            font=("Cascadia Mono SemiBold", 13)
        )
        self.designer.grid(row=3, column=0, pady=(0, 60))


if __name__ == "__main__":
    # Run game app
    app = Game()
    app.mainloop()
