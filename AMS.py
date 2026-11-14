import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MajorMatcherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Major Matcher")
        self.geometry("700x500")
        self.main_view = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_view.pack(fill="both", expand=True, padx=20, pady=20)
        self.title_label = ctk.CTkLabel(
            self.main_view, 
            text="🎯 Major Matcher", 
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(anchor="w", pady=(0, 15))
        self.majors_info = [
            ("Medicine", "Biology: 85+, Chemistry: 80+, Physics: 75+", "🩺"),
            ("Software Engineering", "Math: 80+, Physics: 70+, CS: 85+", "💻"),
            ("Finance", "Math: 90+, Economics: 85+", "📈"),
            ("Mechanical Engineering", "Math: 90+, Physics: 90+, Chemistry: 75+", "⚙️")
        ]
        
        self.create_major_cards()
        
    def create_major_cards(self):
        for major, prereqs, emoji in self.majors_info:
            # Create one card
            card = ctk.CTkFrame(self.main_view, fg_color="#1e1e1e", corner_radius=12)
            card.pack(fill="x", pady=8)
            # The head of the card includes the name
            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=20, pady=(15, 5))
            
            lbl_major = ctk.CTkLabel(
                header, 
                text=f"{emoji}  {major}", 
                font=ctk.CTkFont(size=18, weight="bold")
            )
            lbl_major.pack(side="left")
            
            # Essential requirements department 
            prereq_label = ctk.CTkLabel(
                card, 
                text=f"Prerequisites: {prereqs}", 
                text_color="#888888",
                font=ctk.CTkFont(size=14)
            )
            prereq_label.pack(anchor="w", padx=20, pady=(0, 15))

if __name__ == "__main__":
    app = MajorMatcherApp()
    app.mainloop()
