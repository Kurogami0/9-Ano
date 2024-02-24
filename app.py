from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dados iniciais da turma e meta de arrecadação
turma_info = {
    'meta_arrecadacao': 10000,
    'arrecadado': 0,
}

@app.route('/')
def index():
    return render_template('index.html', turma=turma_info)

@app.route('/doar', methods=['POST'])
def doar():
    valor_doacao = float(request.form.get('valor', 0))
    
    # Atualiza o total arrecadado
    turma_info['arrecadado'] += valor_doacao
    
    # Redireciona de volta para a página inicial
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
