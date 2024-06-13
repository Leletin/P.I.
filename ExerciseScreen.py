from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ExerciseScreen(Screen):
    def __init__(self, **kwargs):
        super(ExerciseScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        label = Label(text="Exercícios Físicos Diários", font_size=40, size_hint=(1, 0.2))
        layout.add_widget(label)

        exercise_button = Button(text="Iniciar Exercício", size_hint=(1, 0.2))
        exercise_button.bind(on_press=self.start_exercise)
        layout.add_widget(exercise_button)

        back_button = Button(text="Voltar", size_hint=(1, 0.2), background_color=(0.7, 0.7, 0.7, 1), color=(1, 1, 1, 1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def start_exercise(self, instance):
        print("Iniciando exercício...")

        game_screen = self.manager.get_screen('GameScreen')
        game_screen.update_bars_from_exercise()

        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'GameScreen'

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'GameScreen'
