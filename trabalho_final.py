# Vitor Manoel Alves da Silva

import json

senha_mestre = "senha123"
cofre = {}

def autenticar():
    senha = input("Digite a senha mestre: ")
    return senha == senha_mestre

def criar_cofre():
    cofre = {}
    print("Novo cofre criado.")
    return cofre

def carregar_cofre():
    if not cofre:
        print("Nenhum cofre encontrado.")
    else:
        print("Cofre carregado.")

def salvar_cofre():
    with open('cofre.json', 'w') as file:
        json.dump(cofre, file)
    print("Cofre salvo.")

def cadastrar_entrada():
    descricao = input("Digite a descrição: ")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    
    if descricao and login and senha:
        cofre[descricao] = [login, senha]
        print("Entrada cadastrada.")
    else:
        print("Erro: Descrição, login e senha são obrigatórios.")

def listar_entradas():
    for descricao, dados in cofre.items():
        print("-----------------------------------")
        print(f"{descricao.upper()}:")
        print(f"Login: {dados[0]}")
        print(f"Senha: {dados[1]}")
    print("-----------------------------------")

def atualizar_entrada():
    descricao = input("Digite a descrição da entrada a ser atualizada: ")
    
    if descricao in cofre:
        novo_descricao = input("Digite a nova descrição (ou pressione Enter para manter): ")
        novo_login = input("Digite o novo login (ou pressione Enter para manter): ")
        nova_senha = input("Digite a nova senha (ou pressione Enter para manter): ")

        if novo_descricao and novo_descricao != descricao:
            cofre[novo_descricao] = cofre.pop(descricao)
            descricao = novo_descricao

        if novo_login:
            cofre[descricao][0] = novo_login

        if nova_senha:
            cofre[descricao][1] = nova_senha

        print("Entrada atualizada.")
    else:
        print("Entrada não encontrada.")

def apagar_entrada():
    descricao = input("Digite a descrição da entrada a ser apagada: ")
    
    if descricao in cofre:
        del cofre[descricao]
        print("Entrada apagada.")
    else:
        print("Entrada não encontrada.")

if autenticar():
    while True:
        print("\nMenu:")
        print("1. Criar novo cofre")
        print("2. Carregar cofre")
        print("3. Salvar cofre")
        print("4. Cadastrar nova entrada")
        print("5. Listar entradas")
        print("6. Atualizar entrada")
        print("7. Apagar entrada")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cofre = criar_cofre()
        elif escolha == "2":
            carregar_cofre()
        elif escolha == "3":
            salvar_cofre()
        elif escolha == "4":
            cadastrar_entrada()
        elif escolha == "5":
            listar_entradas()
        elif escolha == "6":
            atualizar_entrada()
        elif escolha == "7":
            apagar_entrada()
        elif escolha == "8":
            salvar_cofre()
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")
else:
    print("Senha mestre incorreta. Encerrando o programa.")
