import flet as ft

def main(page: ft.Page):
    page.bgcolor= ft.colors.PINK_100
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    btn = ft.ElevatedButton("Click me!")
    t = ft.Text(value="LOGIN", color="Pink", size=22)
    email_field = ft.TextField(hint_text='Username or Email', width=300)
    pass_field = ft.TextField(hint_text ='Password', width=300)
    print(email_field.value)
    btn = ft.ElevatedButton("Submit")

    page.add(ft.Row(controls=[ft.Column(controls=[t,email_field, pass_field,btn])], alignment=ft.MainAxisAlignment.CENTER))
    page.add(btn)

ft.app(target=main)