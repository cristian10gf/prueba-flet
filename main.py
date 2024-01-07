import flet as ft
from check_box import CustomCheckBox

# Colores constantes
BG = '#041955'
FG = '#3450a1'
PINK= '#eb06ff'
FWG = '#97b4ff'
RED = '#ff0000'

# Variables
usuario = "Usuario"
categories = ['Bussines', 'Family', 'Friends']
Tasks_N = [20, 10, 5]
list_tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6', 'Task 7', 'Task 8', 'Task 9', 'Task 10', 'Task 11', 'Task 12', 'Task 13', 'Task 14', 'Task 15', 'Task 16', 'Task 17', 'Task 18', 'Task 19', 'Task 20']


# Función principal
def main(page: ft.Page):

    # Función para cambiar el tamaño de la ventana
    def shrink(e):
        if page_2.controls[0].width == 400:
            page_2.controls[0].width = 120
            page_2.controls[0].scale = ft.transform.Scale(0.8, alignment=ft.alignment.center_right)
        else:
            page_2.controls[0].width = 400
            page_2.controls[0].scale = ft.transform.Scale(1, alignment=ft.alignment.center_right)
        page.update()
 

    # Tareas
    tasks = ft.Column(height=400, scroll='auto', controls=[])
    for i in range(len(list_tasks)):
        tasks.controls.append(
            ft.Container(
                bgcolor=BG, height=50, width=400, border_radius=25,padding=ft.padding.only(left=20, top=5),
                #content=CustomCheckBox(PINK,label=f'{list_tasks[i]}', size=30),
                content=ft.Checkbox(label=f'{list_tasks[i]}', ),
                animate=ft.animation.Animation(600,ft.AnimationCurve.DECELERATE),
                animate_scale=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE)
            )
        )

    

    categorias_card = ft.Row(scroll='auto')
    for i in range(len(categories)):
        categorias_card.controls.append(
            ft.Container(
                bgcolor=BG, height=110, width=170, border_radius=20,padding=15,
                content=ft.Column(controls=[
                    ft.Text(f'{Tasks_N[i]} Tasks'), 
                    ft.Text(f'{categories[i]}'),
                    ft.Container(
                        width=160, height=5, bgcolor='white12', border_radius=20, 
                        padding=ft.padding.only(right=50),
                        content=ft.Container(bgcolor=PINK)
                    )
                ])
            )
        )



    controls_firs_page = ft.Container(
        content=ft.Column(controls=[
            # Navbar
            ft.Row(controls=[
                ft.Container(content=ft.Icon(ft.icons.MENU), on_click= lambda e: shrink(e)),
                ft.Row(controls=[ft.Icon(ft.icons.SEARCH), ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED)])
            ], alignment='spaceBetween'),
            
            # espacio
            ft.Container(height=20),

            # inicio
            ft.Text(value=f"Bienvenido {usuario}"),
            ft.Text(value="CATEGORIES"),
            
            # categorias
            ft.Container(
                padding=ft.padding.only(top=10,bottom=20),
                content=categorias_card                    
            ),

            ft.Container(height=20),
            ft.Text("TODAY'S TASKS"),
            
            # tareas
            ft.Stack(
                controls=[
                    tasks, 
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD, bgcolor=PINK, bottom=2, right=20,
                        on_click= lambda _: page.go('/create_task')
                    )
                ]
            )
        ]) 
    )

    # paginas del contenedor principal___________________________________________
    page_1 = ft.Container()

    page_2 = ft.Row(alignment='end',
        controls=[
            ft.Container(
                width=400, 
                height=850, 
                bgcolor=FG, 
                border_radius=35, 
                padding=ft.padding.only(20,50,20,50),
                content=ft.Column(controls=[controls_firs_page])
            )
        ]
    )


    # ventanas      _________________________________________________________________
    main_contenedor = ft.Container(
        width=400, 
        height=850,                      
        bgcolor=BG, 
        border_radius=35, 
        content=ft.Stack(controls= [page_1, page_2])             
    )

    create_task_contenedor = ft.Container(
        content=ft.Container(on_click=lambda _: page.go('/'),
            height=40,width=40, bgcolor=RED, border_radius=10,
            content=ft.Text('x'), 
        )
    )
    
   
    # configuración de la página ___________________________________________________

    page.add(main_contenedor)
    
        # ventanas enrutador
    pages = {
        '/': ft.View("/", [main_contenedor]),
        '/create_task': ft.View("/create_task", [create_task_contenedor])
    }

    # Función para cambiar de página
    def route_change(route):
        page.views.clear()
        page.views.append(pages[page.route])

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target= main)