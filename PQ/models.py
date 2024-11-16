from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    carro = models.ForeignKey('Carro', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Carro(models.Model):
    
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
     

    def __str__(self):
        return self.placa

class Parqueadero(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Reserva de {self.cliente} para el carro {self.carro} desde {self.fecha_inicio} hasta {self.fecha_final}"
    

    def __str__(self):
        return f"Reserva de {self.cliente} - {self.carro}"

class Factura(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} - Monto: {self.monto}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)  
    ubicacion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        
        return f"{self.nombre} {self.apellido}"  

class RegistroAcceso(models.Model):
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Acceso de {self.cliente} con {self.carro} en {self.parqueadero}"

