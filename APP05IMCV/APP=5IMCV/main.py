import flet as ft

def calcular_imc(txtPeso, txtAltura, lblIMC, page):
    try:
        peso = float(txtPeso.value)
        altura = float(txtAltura.value)
        imc = peso / (altura**2)
        lblIMC.value = f"Tu IMC es de: {imc:.2f}"
        page.update()
        
        # Función para cerrar el cuadro de diálogo y actualizar la página
        def cerrar_dialogo(e):
            page.dialog.open = False
            page.update()
        
        # Validación del IMC
        if imc < 18.5:
            dialog = ft.AlertDialog(
                title=ft.Text("Bajo peso"),
                content=ft.Text("Tu IMC indica que tienes bajo peso"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        elif 18.5 <= imc < 24.9:
            dialog = ft.AlertDialog(
                title=ft.Text("Peso normal"),
                content=ft.Text("Tu IMC indica que tienes un peso normal"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        elif 25 <= imc < 30:
            dialog = ft.AlertDialog(
                title=ft.Text("Sobrepeso"),
                content=ft.Text("Tu IMC indica que tienes sobrepeso"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        else:
            dialog = ft.AlertDialog(
                title=ft.Text("Obesidad"),
                content=ft.Text("Tu IMC indica que tienes obesidad, acude a tu médico"),
                actions=[
                    ft.TextButton(text="Cerrar", on_click=cerrar_dialogo)
                ]
            )
        
        page.dialog = dialog
        page.dialog.open = True
        page.update()

    except ValueError:
        # Manejo de error cuando los datos ingresados no son válidos
        def cerrar_error(e):
            page.dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            title="Error",
            content="Por favor, ingresa valores numéricos válidos.",
            actions=[
                ft.TextButton(text="Cerrar", on_click=cerrar_error)
            ]
        )
        page.dialog = dialog
        page.dialog.open = True
        page.update()

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor = "blue"
    
    txtPeso = ft.TextField(label="Ingresa tu peso")
    txtAltura = ft.TextField(label="Ingresa tu altura")
    lblIMC = ft.Text("Tu IMC es de: ")
    
    img = ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def on_calcular(e):
        calcular_imc(txtPeso, txtAltura, lblIMC, page)
    
    def limpiar(e):
        txtPeso.value = ""
        txtAltura.value = ""
        lblIMC.value = "Tu IMC es de: "
        page.update()
        
    btnCalcular = ft.ElevatedButton(text="Calcular", on_click=on_calcular)
    btnLimpiar = ft.ElevatedButton(text="Limpiar", on_click=limpiar)
    
    page.add(
        ft.Column(
            controls=[
                txtPeso, txtAltura, lblIMC
            ], alignment="CENTER"
        ),
        ft.Row(
            controls=[img],
            alignment="CENTER"
        ),
        ft.Row(
            controls=[btnCalcular, btnLimpiar],
            alignment="CENTER"
        )
    )
        
ft.app(target=main,view=ft.AppView.WEB_BROWSER)

