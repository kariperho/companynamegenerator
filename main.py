import flet as ft
import random
import json

with open("names.json", "r", encoding="utf-8") as file:
        names_file = json.load(file)

width = 400
height = 200

prefixes = names_file["prefix"]
suffixes = names_file["suffix"]

comp_name = "Name will appear here"
new_name = ft.TextField(width=(width * 0.60), align=ft.Alignment.CENTER, text_align=ft.TextAlign.CENTER, value=comp_name, bgcolor=ft.Colors.random())

def main(page:ft.Page):
    page.title = "Karppa's Name Generator"
    page.window.width = width
    page.window.height = height
   
    page.add(new_name)
    page.add(ft.Button("Generate!", on_click=generate, align=ft.alignment.Alignment(0,0)))

def generate():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    comp_name = prefix + suffix

    new_name.value=comp_name
    new_name.bgcolor=ft.Colors.random()
    new_name.update()

ft.run(main)
