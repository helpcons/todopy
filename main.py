import flet as ft
import sqlite3

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = "Todo App"
        self.task = ''
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name, status)')
        self.main_page()


    # Comunicação com o banco de dados
    def db_execute(self, query, params = []):
        # com o with abrimos uma conexão com o banco de dados
        # executamos o que precisamos e fechamos a conexão
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()


    def tasks_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content= ft.Column(
                controls=[
                    ft.Checkbox(label="Tarefa 1", value=True)
                ]
            )
        )
    

    def set_value(self, e):
        self.task = e.control.value
    

    def add(self, e, input_task):
        pass
    

    def main_page(self):
        input_task = ft.TextField(hint_text='Digite aqui uma tarefa', expand=True)
        input_add = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=lambda e: self.add(e, input_task)
        )

        input_bar = ft.Row(
            controls=[
                input_task,
                input_add
            ]
        )

        tabs = ft.Tabs(
            selected_index=0, # o primeiro elemento sempre selecionado
            tabs=[
                ft.Tab(text="Todos"),
                ft.Tab(text="Em andamento"),
                ft.Tab(text="Finalizados"),
            ]
        )

        tasks = self.tasks_container()

        self.page.add(input_bar, tabs, tasks)

ft.app(target= ToDo)
