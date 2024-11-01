from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preços dos serviços
service_prices = {
    'barra': 20,
    'ajustar_cintura': 30,
    'zipper': 10,
    'trocar_botao': 5,
}

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Processar o formulário
        nome_cliente = request.form['nome_cliente']
        cpf_cliente = request.form['cpf_cliente']
        data_servico = request.form['data_servico']
        data_entrega = request.form['data_entrega']
        servico_principal = request.form['servico_principal']
        servicos_extras = request.form.getlist('servicos_extras[]')

        # Calcular o preço total
        total = service_prices[servico_principal]
        total += sum(service_prices[servico] for servico in servicos_extras)

        # Aqui você pode salvar os dados em um banco de dados ou processá-los como precisar

        # Redirecionar ou renderizar uma página de confirmação (opcional)
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html', service_prices=service_prices)

if __name__ == '__main__':
    app.run(debug=True)
