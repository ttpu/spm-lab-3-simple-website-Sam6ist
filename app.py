from flask import Flask, render_template_string, request

app = Flask(__name__)

# ALU (Arithmetic Logic Unit)
class ALU:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

alu = ALU()

# Xotira
class Memory:
    def __init__(self, size):
        self.size = size
        self.memory = [0] * size

    def write(self, address, value):
        if 0 <= address < self.size:
            self.memory[address] = value

    def read(self, address):
        if 0 <= address < self.size:
            return self.memory[address]
        return None

memory = Memory(10)  # 10 ta xotira joyi

# I/O Qurilmalari
class InputDevice:
    def get_input(self, prompt):
        return input(prompt)

class OutputDevice:
    def display_output(self, output):
        print("Natija:", output)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Protsessor Simulyatori</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            input, select, button {
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                background-color: #5cb85c;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #4cae4c;
            }
            a {
                display: inline-block;
                margin-top: 10px;
                text-decoration: none;
                color: #337ab7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Protsessor Simulyatori</h1>
            <form action="/calculate" method="POST">
                <input type="number" name="a" placeholder="Birinchi raqam" required>
                <input type="number" name="b" placeholder="Ikkinchi raqam" required>
                <select name="operation">
                    <option value="add">Qo'shish</option>
                    <option value="subtract">Ayirish</option>
                </select>
                <button type="submit">Hisoblash</button>
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = int(request.form['a'])
    b = int(request.form['b'])
    operation = request.form['operation']

    if operation == 'add':
        result = alu.add(a, b)
    elif operation == 'subtract':
        result = alu.subtract(a, b)
    else:
        result = 'Noto\'g\'ri operatsiya!'

    # Xotiraga yozish (masalan, natijani saqlash)
    memory.write(0, result)  # Natijani 0-indeksga yozamiz

    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Natija</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Natija</h1>
            <p>Hisoblangan natija: {result}</p>
            <p>Xotiradan olingan natija: {memory.read(0)}</p>
            <a href="/">Orqaga qaytish</a>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
