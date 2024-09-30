from flask import Flask, request, render_template_string
from flask_mail import Mail, Message

app = Flask(__name__)

# ===============Configuração do servidor de email==============================
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'talisfilipe74@outlook.com'
app.config['MAIL_PASSWORD'] = '#Hullodigital2024'  # Substitua pela sua senha
app.config['MAIL_DEFAULT_SENDER'] = 'talisfilipe74@outlook.com'

mail = Mail(app)

# ===============Rota para exibir o formulário (apenas para teste local)====================
@app.route('/')
def index():
    return render_template_string('''
    <form action="/send_email" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <input type="submit" value="Enviar">
    </form>
    ''')

# ====================Rota para enviar o email==============================
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    msg = Message(subject=f"Novo Contato de {name}",
                sender=email,
                recipients=['talisfilipe74@outlook.com'],
                body=f"Nome: {name}\nEmail: {email}\n\nMensagem:\n{message}")

    try:
        mail.send(msg)
        return "Mensagem enviada com sucesso!", 200
    except Exception as e:
        return f"Falha ao enviar a mensagem: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)