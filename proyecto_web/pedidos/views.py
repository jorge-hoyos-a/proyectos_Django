from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, Linea_Pedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/autenticacion/login_usuario")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)   # Damos de alta un pedido
    carro = Carro(request)  # Cogemos el carro
    lineas_pedido = list()  # Lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #Recorremos el carro con sus items
        lineas_pedido.append(Linea_Pedido(
            producto_id = key, 
            cantidad = value["cantidad"],
            user = request.user,
            pedido =pedido
        ))
        
        # Guardar los datos del pedido en la tabla correspondiente en la bbdd
    Linea_Pedido.objects.bulk_create(lineas_pedido) # Crea registros en BBDD en paquete
    
    enviar_mail(
        pedido= pedido,
        lineas_pedido= lineas_pedido,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email
    )
    
    messages.success(request, "El pedido se ha creado correctamente")
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombreusuario")
    })
    
    mensaje_texto = strip_tags(mensaje)
    from_email = "correo_electronico_tienda@email.com"
    to_email = kwargs.get("email_usuario")
    
    send_mail(asunto, mensaje_texto, from_email,[to_email], html_message=mensaje)