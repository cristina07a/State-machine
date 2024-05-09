import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        self.title("Chestionar Mario")

        welcome_message = "Bun venit la un chestionar despre Mario!\nDaca raspunzi gresit la o intrebare, atunci pierzi!"
        self.welcome_label = tk.Label(self, text=welcome_message)
        self.welcome_label.pack(pady=20)

        self.start_button = tk.Button(self, text="Incepe", command=self.start_game)
        self.retry_button = tk.Button(self, text="Ia-o de la inceput", command=self.start_game)        
        self.start_button.pack()

        self.question_label = tk.Label(self, text="")
        self.answer_buttons = []

        self.normal_button = tk.Radiobutton(self, text="Normal", command= self.show_normal)
        self.medium_button = tk.Radiobutton(self, text="Mediu", command= self.show_medium)
        self.yes_button = tk.Button(self, text="Da", command= self.select_difficulty)
        self.no_button = tk.Button(self, text="Nu", command= self.unable_to_play)
 

        self.questions = {
            "normal": [
                ("Care este numele fratelui lui Mario?", [("a) Luigi", False), ("b) Yoshi", False), ("c) Bowser", True)]),
                ("Care este numele printesei pe care Mario o salveaza?", [("a) Daisy", False), ("b) Peach", True), ("c) Rosalina", False)]),
                ("Care este numele rivalului principal al lui Mario?", [("a) Wario", False), ("b) Bowser", True), ("c) Waluigi", False)]),
                ("Prin ce mijloc de transport poti calatori pe harta?", [("a) Avion", False), ("b) Warp pipe", True), ("c) Nava", False)]),
                ("Ce se intampla la finalul nivelului in unele jocuri Mario?", [("a) Mario saruta printesa", True), ("b) Il înfrange pe Bowser", False), ("c) Primesc o stea de aur", False)]),
                ("In ce an a fost lansat primul joc Mario?", [("a) 1983", False), ("b) 1985", True), ("c) 1990", False)])
            ],
            "medium": [
                ("Cate locuri sunt disponibile in total pe podiumul de la finalul unei curse in Super Mario Kart?", [("a) 3", False), ("b) 4", True), ("c) 5", False)]),
                ("Care a fost anul lansarii Super Mario Kart?", [("a) 1991", False), ("b) 1992", True), ("c) 1993", False)]),
                ("Cine este cel mai rapid personaj in Super Mario Kart?", [("a) Mario", False), ("b) Luigi", False), ("c) Yoshi", True)]),
                ("Cate piste sunt disponibile in total in Super Mario Kart?", [("a) 16", False), ("b) 20", False), ("c) 24", True)]),
                ("Care este numele celui mai dificil nivel de dificultate (SMK)?", [("a) 50cc", False), ("b) 100cc", False), ("c) 150cc", True)]),
                ("Care a fost anul lansarii Super Mario Kart?", [("a) 1991", False), ("b) 1992", True), ("c) 1993", False)])
            ]
        }
    
    def start_game(self):
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()
        self.retry_button.pack_forget()
        self.question_label.config(text="In primul rand, ai jucat vreodata ceva Mario?")
        self.question_label.pack(pady=(20, 0)) #afisare question_label
        self.yes_button.pack()
        self.no_button.pack()
        self.current_question = 0
        self.difficulty = ""


    def unable_to_play(self):
        self.question_label.config(text="Din pacate, nu poti participa daca nu ai jucat\nmacar un joc Mario!")
        self.yes_button.pack_forget()
        self.no_button.pack_forget()

    def select_difficulty(self):
        self.yes_button.pack_forget()
        self.no_button.pack_forget() 
        self.question_label.config(text="Alege dificultatea:")
        self.normal_button.pack();
        self.medium_button.pack();
    
    def show_normal(self):
        self.normal_button.pack_forget()
        self.medium_button.pack_forget()

        self.difficulty = "normal"
        self.display_question() 

    def show_medium(self):
        self.normal_button.pack_forget()
        self.medium_button.pack_forget()

        self.difficulty = "medium"
        self.display_question()



    def display_question(self):
        self.question_label.config(text=self.questions[self.difficulty][self.current_question][0])
        answers = self.questions[self.difficulty][self.current_question][1]
        
        # eliminare butoane anterioare
        for button in self.answer_buttons:
            button.destroy()
        self.answer_buttons = []

        # creare butoane pentru raspunsuri
        for i, answer in enumerate(answers):
            text, is_correct = answer
            button = tk.Radiobutton(self, text=text, command=lambda is_correct=is_correct: self.check_answer(is_correct))
            button.pack()
            self.answer_buttons.append(button)

    def check_answer(self, is_correct):
        if is_correct:
            self.current_question += 1
            if self.current_question < len(self.questions[self.difficulty]):
                self.display_question()
            else:
                self.question_label.config(text="Felicitari! Ai raspuns corect la toate intrebarile de la dificultatea "+ self.difficulty +" !")
                for button in self.answer_buttons:
                    button.destroy() 
        else:
            self.question_label.config(text="Raspuns gresit! Ai pierdut.")
            for button in self.answer_buttons:
                button.destroy()
            self.retry_button.pack()


app = Application()
app.mainloop()