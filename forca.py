import flet as ft
import string
import random

def main(page: ft.Page):
    page.bgcolor = ft.colors.BROWN_600

    available_words = ['python', 'flet', 'programador', 'guerra']
    choiced_word = random.choice(available_words).upper()

    def validate(e):
        for pos, letter in enumerate(choiced_word):
            if e.control.content.value == letter:
                word.controls[pos] = guess(letter=letter)
                word.update()
        if e.control.content.value not in choiced_word:
            victim.data += 1
            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    title=ft.Text(value='Game Over'),
                    open=True,
                )
                page.update()
            victim.src = f'images/hangman_{victim.data}.png'
            victim.update()

        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.GREY, ft.colors.GREY]
        )
        e.control.update()
                
                
                

    def guess(letter):
        return ft.Container(
                width=50,
                height=50,
                bgcolor=ft.colors.AMBER_500,
                border_radius=ft.border_radius.all(5),
                content=ft.Text(
                    value=letter,
                    color=ft.colors.WHITE,
                    size=30,    
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD,
                )
        )


    victim = ft.Image(
        data = 0,
        src='images/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
        )
    
    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            guess('_') for letter in choiced_word
            ]
    )

    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding= ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word,


            ]
        )
    )

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        image_src=('images/keyboard.png'),
        image_repeat = ft.ImageRepeat.NO_REPEAT,
        image_fit= ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                    ),
                    gradient = ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
                    ),
                    on_click=validate,
                ) for letter in string.ascii_uppercase
            ]
        )
    )
                        

    scene = ft.Image(col=12, src = 'images/scene.png')

    layout = ft.ResponsiveRow(
        columns= 12,
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(layout)



if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')