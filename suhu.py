def konversi_suhu(nilai, unit):
    if unit == 'C':
        fahrenheit = (nilai * 9/5) + 32
        return fahrenheit
    elif unit == 'F':
        celsius = (nilai - 32) * 5/9
        return celsius

suhu1 = konversi_suhu(99, 'C')
print("99 C = ", suhu1, "Fahrenheit")

suhu2 = konversi_suhu(98, 'F')
print("98 F = ",suhu2, "Celsius")