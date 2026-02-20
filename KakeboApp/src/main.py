import flet as ft

from Database.database_connector import DatabaseConnector
from controllers.controller_create_mwd import ControllerCreateMWD


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )

def probar_creacion():
    # 1. Preparar la Base de Datos
    print("Conectando y creando tablas...")
    db = DatabaseConnector()
    db.create_tables()

    # 2. INICIALIZAR EL CONTROLADOR
    # Pasamos una fecha de 2026. El controlador usará el año 2026.
    print("Inicializando controlador para el año 2026...")
    
    controlador = ControllerCreateMWD()

    # 3. EJECUTAR LA CREACIÓN
    # Llamamos a create_year, que a su vez llama a meses y semanas
    print("Ejecutando creación en cascada (Año -> Meses -> Semanas)...")
    controlador.create_year()

    print("\n¡Proceso finalizado!")
    print("-" * 30)

    # 4. VERIFICACIÓN RÁPIDA
    # Comprobamos si hay datos en las tablas
    db.cursor.execute("SELECT COUNT(*) FROM years")
    anios = db.cursor.fetchone()[0]
    
    db.cursor.execute("SELECT COUNT(*) FROM months")
    meses = db.cursor.fetchone()[0]
    
    db.cursor.execute("SELECT COUNT(*) FROM weeks")
    semanas = db.cursor.fetchone()[0]

    print(f"Resultados en la BD:")
    print(f"- Años creados: {anios}")
    print(f"- Meses creados: {meses} (Deberían ser 12)")
    print(f"- Semanas creadas: {semanas} (Deberían ser ~52)")

if __name__ == "__main__":
    probar_creacion()


ft.run(main)
