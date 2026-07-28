from flask import Flask, render_template, request, redirect, url_for
import json

# Inicializo o Flask para criar o servidor
app = Flask(__name__)

# Defino o arquivo onde vou salvar os dados (meu "banco de dados" simples)
ARQUIVO_BANCO = "produtos.json"


def carregar_produtos():
    """
    Tenta abrir e carregar a lista de produtos do arquivo JSON.
    Se o arquivo ainda não existir, captura o erro e retorna uma lista vazia.
    """
    try:
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se for a primeira execução e o arquivo não existir, começo do zero
        return []


def salvar_produtos(lista_produtos):
    """
    Pega a lista de produtos atualizada e grava no arquivo JSON.
    """
    with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
        json.dump(lista_produtos, arquivo, indent=4, ensure_ascii=False)


# -------------------------------------------------------------
# MINHAS ROTAS WEB (Comunicação com o navegador)
# -------------------------------------------------------------

# Rota 1: Página Inicial (Agora com busca!)
@app.route("/")
def pagina_inicial():
    # 1. Pega a palavra que o usuário digitou no campo de busca (se houver)
    termo_busca = request.args.get("busca", "").strip().lower()

    # 2. Carrega todos os produtos do arquivo JSON
    todos_produtos = carregar_produtos()

    # 3. Se o usuário pesquisou algo, filtra a lista; senão, mantém todos os produtos
    if termo_busca:
        produtos_exibidos = [
            p for p in todos_produtos 
            if termo_busca in p["nome"].lower()
        ]
    else:
        produtos_exibidos = todos_produtos

    # 4. Passa a lista (filtrada ou completa) e o termo pesquisado para o HTML
    return render_template("index.html", produtos=produtos_exibidos, termo=termo_busca)


# Rota 2: Ação de Cadastrar
@app.route("/cadastrar", methods=["POST"])
def cadastrar_produto():
    # 1. Pega o que o usuário digitou no formulário
    nome_input = request.form.get("nome")
    preco_input = float(request.form.get("preco"))

    # 2. Carrega a lista que já existe
    produtos = carregar_produtos()

    # 3. Cria o dicionário do novo produto
    novo_item = {
        "nome": nome_input,
        "preco": preco_input
    }

    # 4. Adiciona o novo item na lista e salvo no JSON
    produtos.append(novo_item)
    salvar_produtos(produtos)

    # 5. Volta para a página inicial para mostrar a lista atualizada
    return redirect(url_for("pagina_inicial"))


# Rota 3: Ação de Deletar (recebe o índice do item pela URL)
@app.route("/deletar/<int:indice>")
def deletar_produto(indice):
    # 1. Carrega os produtos salvos
    produtos = carregar_produtos()

    # 2. Valida se o índice recebido realmente existe na lista
    if 0 <= indice < len(produtos):
        # Remove o item da posição indicada e salvo de volta no arquivo
        produtos.pop(indice)
        salvar_produtos(produtos)

    # 3. Recarrega a tela principal
    return redirect(url_for("pagina_inicial"))


# -------------------------------------------------------------
# EXECUÇÃO DO PROGRAMA
# -------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)