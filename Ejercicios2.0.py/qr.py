import qrcode
texto = "https://docs.google.com/forms/d/1460tCI0lMzcXrWmXYh1LSJf5KTzrYp8WKiyJFqLYv3A/edit "
img = qrcode.make(texto)
img.save("Qr_futuros_usuarios.png")