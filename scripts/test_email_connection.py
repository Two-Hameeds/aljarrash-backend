import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aljarrashc@gmail.com', 'Aljarrash@1234')
    print("Login successful")
except Exception as e:
    print("Error:", e)
finally:
    server.quit()