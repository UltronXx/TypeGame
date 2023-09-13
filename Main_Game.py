import customtkinter as ctk


class App(ctk.CTk):
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
        self.background = ctk.CTkFrame(
            master=self,
            height=200,
            width=200,
            fg_color="#0295A9",
            corner_radius=0
        )
        self.background.grid(row=0, column=0, sticky="news")
        self.background.grid_columnconfigure(index=0, weight=1)
        self.background.grid_rowconfigure(index=2, weight=1)

        # Top Info frame
        self.info_frame = ctk.CTkFrame(
            master=self.background,
            height=40,
            width=200,
            fg_color="#0295A9"
        )
        self.info_frame.grid(row=0, column=0, pady=(60, 30))

        self.words_label = ctk.CTkLabel(
            master=self.info_frame,
            text="Words:",
            text_color="white",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.words_label.grid(row=0, column=0, padx=6)

        self.count_button = ctk.CTkButton(
            master=self.info_frame,
            height=35,
            width=40,
            text="0",
            fg_color="#12ADC1",
            hover_color="#12ADC1",
            text_color="white",
            corner_radius=10,
            font=("Cascadia Mono SemiBold", 15)
        )
        self.count_button.grid(row=0, column=1, padx=(0, 6))

        self.slash = ctk.CTkLabel(
            master=self.info_frame,
            text="/",
            text_color="white",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.slash.grid(row=0, column=2)

        self.total_words_button = ctk.CTkButton(
            master=self.info_frame,
            height=35,
            width=40,
            text="0",
            fg_color="#12ADC1",
            hover_color="#12ADC1",
            text_color="white",
            corner_radius=10,
            font=("Cascadia Mono SemiBold", 15)
        )
        self.total_words_button.grid(row=0, column=3, padx=(6, 250))

        self.change_button = ctk.CTkButton(
            master=self.info_frame,
            text_color="#121212",
            text="Change",
            height=40,
            width=100,
            corner_radius=10,
            fg_color="#FDD037",
            hover_color="#FCE186",
            font=("Cascadia Mono Bold", 13)
        )
        self.change_button.grid(row=0, column=4, padx=(250, 6))

        self.sentence = ctk.CTkTextbox(
            master=self.background,
            height=150,
            width=1050,
            fg_color="#028395",
            text_color="white",
            corner_radius=14,
            font=("Cascadia Mono SemiBold", 15)
        )
        self.sentence.grid(row=1, column=0)

        # Keyboard frame
        self.keyboard_frame = ctk.CTkFrame(
            master=self.background,
            height=200,
            width=200,
            corner_radius=24,
            fg_color="#0295A9"
        )
        self.keyboard_frame.grid(row=2, column=0)

        # Buttons
        self.button_q = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="Q",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_q.grid(row=0, column=0, padx=(12, 6), pady=(12, 6))

        self.button_w = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="W",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_w.grid(row=0, column=2, padx=(6, 6), pady=(12, 6))

        self.button_e = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="E",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_e.grid(row=0, column=4, padx=(6, 6), pady=(12, 6))

        self.button_r = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="R",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_r.grid(row=0, column=6, padx=(6, 6), pady=(12, 6))

        self.button_t = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="T",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_t.grid(row=0, column=8, padx=(6, 6), pady=(12, 6))

        self.button_y = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="Y",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_y.grid(row=0, column=10, padx=(6, 6), pady=(12, 6))

        self.button_u = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="U",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_u.grid(row=0, column=12, padx=(6, 6), pady=(12, 6))

        self.button_i = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="I",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_i.grid(row=0, column=14, padx=(6, 6), pady=(12, 6))

        self.button_o = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="O",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_o.grid(row=0, column=16, padx=(6, 6), pady=(12, 6))

        self.button_p = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="P",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_p.grid(row=0, column=18, padx=(6, 6), pady=(12, 6))

        self.button_ = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=" ",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#12ADC1",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_.grid(row=0, column=20, padx=(6, 6), pady=(12, 6))

        self.button__ = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=" ",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#0295A9",
            hover_color="#0295A9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button__.grid(row=0, column=22, padx=(6, 12), pady=(12, 6))

        self.button_a = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="A",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_a.grid(row=1, column=0, columnspan=3, padx=(12, 6), pady=(6, 6))

        self.button_s = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="S",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_s.grid(row=1, column=2, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_d = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="D",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_d.grid(row=1, column=4, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_f = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="F",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_f.grid(row=1, column=6, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_g = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="G",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_g.grid(row=1, column=8, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_h = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="H",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_h.grid(row=1, column=10, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_j = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="J",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_j.grid(row=1, column=12, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_k = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="K",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_k.grid(row=1, column=14, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_l = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="L",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_l.grid(row=1, column=16, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_colon = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=";",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_colon.grid(row=1, column=18, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_aps = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="'",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_aps.grid(row=1, column=20, columnspan=3, padx=(6, 6), pady=(6, 6))

        self.button_z = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="Z",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_z.grid(row=2, column=0, columnspan=5, padx=(12, 6), pady=(6, 6))

        self.button_x = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="X",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_x.grid(row=2, column=2, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_c = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="C",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_c.grid(row=2, column=4, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_v = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="V",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_v.grid(row=2, column=6, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_b = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="B",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_b.grid(row=2, column=8, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_n = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="N",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_n.grid(row=2, column=10, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_m = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text="M",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_m.grid(row=2, column=12, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_comma = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=",",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_comma.grid(row=2, column=14, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_fullstop = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=".",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_fullstop.grid(row=2, column=16, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button___ = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=" ",
            height=60,
            width=60,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#12ADC1",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button___.grid(row=2, column=18, columnspan=5, padx=(6, 6), pady=(6, 6))

        self.button_space = ctk.CTkButton(
            master=self.keyboard_frame,
            text_color="white",
            text=" ",
            height=60,
            width=350,
            corner_radius=12,
            fg_color="#12ADC1",
            hover_color="#6CDAE9",
            font=("Cascadia Mono SemiBold", 15)
        )
        self.button_space.grid(row=3, column=6, columnspan=10, padx=(6, 6), pady=(6, 12))


if __name__ == "__main__":
    App().mainloop()
