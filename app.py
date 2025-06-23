from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data['expression']
        
        # Validate expression
        if not re.match(r'^[0-9+\-*/.() ]+$', expression):
            return jsonify({'error': 'Expressão inválida!'}), 400
            
        # Evaluate expression
        try:
            result = eval(expression)
            if not isinstance(result, (int, float)):
                return jsonify({'error': 'Resultado inválido!'}), 400
            return jsonify({'result': result})
        except ZeroDivisionError:
            return jsonify({'error': 'Divisão por zero não é permitida!'}), 400
        except Exception as e:
            return jsonify({'error': 'Erro ao calcular a expressão!'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 