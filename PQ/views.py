
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Carro, Parqueadero, Reserva, Factura, Empleado, RegistroAcceso
from .forms import ClienteForm, CarroForm, ParqueaderoForm, ReservaForm, FacturaForm, EmpleadoForm, RegistroAccesoForm
from django import forms

def home(request):
    return render(request, 'home.html')



# Vistas para Cliente
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/registrar/registrar_cliente.html', {'form': form})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/actualizar_cliente.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})

# Vistas para Carro
def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carros/listar_carros.html', {'carros': carros})

from django.shortcuts import render
from .models import Cliente

def registrar_carro(request):
    clientes = Cliente.objects.all() 
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm()

    return render(request, 'carros/registrar/registrar_carro.html', {'form': form, 'clientes': clientes})

def actualizar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'carros/actualizar_carro.html', {'form': form})

def eliminar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    if request.method == 'POST':
        carro.delete()
        return redirect('listar_carros')
    return render(request, 'carros/eliminar_carro.html', {'carro': carro})

# Vistas para Parqueadero
def listar_parqueaderos(request):
    parqueaderos = Parqueadero.objects.all()
    return render(request, 'parqueaderos/listar_parqueaderos.html', {'parqueaderos': parqueaderos})

def registrar_parqueadero(request):
    if request.method == 'POST':
        form = ParqueaderoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parqueaderos')
    else:
        form = ParqueaderoForm()

    return render(request, 'parqueaderos/registrar/registrar_parqueadero.html', {'form': form})
# Vistas para Reserva
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

def registrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        clientes = Cliente.objects.all()
        carros = Carro.objects.all()
        form = ReservaForm()

    return render(request, 'reservas/registrar/registrar_reserva.html', {'form': form, 'clientes': clientes, 'carros': carros})

# Vistas para Factura
def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'Factura/listar_facturas.html', {'facturas': facturas})

def registrar_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()

    
    reservas = Reserva.objects.all()  
    return render(request, 'Factura/registrar/registrar_factura.html', {'form': form, 'reservas': reservas})
# Vistas para Empleado
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'Empleado/listar_empleados.html', {'empleados': empleados})

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_empleados') 
    else:
        form = EmpleadoForm() 
    return render(request, 'Empleado/registrar/registrar_empleado.html', {'form': form})

# Vistas para Registro de Acceso
def listar_registros_acceso(request):
    registros = RegistroAcceso.objects.all()
    return render(request, 'Acceso/listar_registros_acceso.html', {'registros': registros})

def registrar_registro_acceso(request):
    if request.method == 'POST':
        form = RegistroAccesoForm(request.POST)
        if form.is_valid():
           #aqui lo agregamos :)
            form.save()
            return redirect('listar_registros_acceso')  # Redirigir después de guardar
    else:
        form = RegistroAccesoForm()

    return render(request, 'Acceso/registrar/registrar_registro_acceso.html', {'form': form})
    