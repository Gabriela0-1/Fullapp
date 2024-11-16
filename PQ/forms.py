from django import forms
from .models import Cliente, Carro, Parqueadero, Reserva, Factura, Empleado, RegistroAcceso

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'carro']
        widgets = {
            'carro': forms.Select(attrs={'class': 'form-control'})  
        }

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'placa']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'})  
        }

class ParqueaderoForm(forms.ModelForm):
    class Meta:
        model = Parqueadero
        fields = ['nombre', 'ubicacion', 'capacidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'})
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'carro', 'fecha_inicio', 'fecha_final', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),  
            'carro': forms.Select(attrs={'class': 'form-control'}),   
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  
            'fecha_final': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  
            'estado': forms.Select(attrs={'class': 'form-control'}),  
        } 

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['reserva', 'fecha', 'monto']
        widgets = {
            'reserva': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'})
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'ubicacion', 'telefono', 'correo'] 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),  
            'apellido': forms.TextInput(attrs={'class': 'form-control'}), 
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),  
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),  
            'correo': forms.EmailInput(attrs={'class': 'form-control'})   
        }
        
class RegistroAccesoForm(forms.ModelForm):
    class Meta:
        model = RegistroAcceso
        fields = ['parqueadero', 'carro', 'reserva', 'empleado', 'cliente', 'fecha_entrada', 'fecha_salida']
        widgets = {
            'parqueadero': forms.Select(attrs={'class': 'form-control'}),
            'carro': forms.Select(attrs={'class': 'form-control'}),
            'reserva': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
