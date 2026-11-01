import os
from pathlib import Path

def auditar_projeto():
    raiz = Path(".")
    erros = 0
    avisos = 0

    print("=== Iniciando Verificação do Projeto WDD 130 ===\n")

    # 1. Verificar index.html na raiz
    index_raiz = raiz / "index.html"
    if index_raiz.is_file():
        print("[SUCESSO] index.html encontrado na raiz.")
    else:
        print("[ERRO] index.html NÃO foi encontrado na raiz do projeto.")
        erros += 1

    # 2. Verificar pasta imagens e perfil.jpg
    pasta_imagens = raiz / "imagens"
    if pasta_imagens.is_dir():
        print("[SUCESSO] Pasta 'imagens' encontrada.")
        # Procurar por perfil.jpg ou extensões válidas
        perfil_encontrado = False
        for ext in [".jpg", ".png", ".webp", ".jpeg"]:
            arquivo_perfil = pasta_imagens / f"perfil{ext}"
            if arquivo_perfil.is_file():
                tamanho_kb = arquivo_perfil.stat().st_size / 1024
                print(f"[SUCESSO] Imagem de perfil encontrada: {arquivo_perfil.name} ({tamanho_kb:.1f} KB)")
                if tamanho_kb > 125:
                    print(f"[AVISO] A imagem tem {tamanho_kb:.1f} KB. O recomendado é abaixo de 125 KB.")
                    avisos += 1
                perfil_encontrado = True
                break
        if not perfil_encontrado:
            print("[ERRO] Nenhuma imagem de perfil nomeada 'perfil' (.jpg, .png, .webp) foi encontrada na pasta 'imagens'.")
            erros += 1
    else:
        print("[ERRO] Pasta 'imagens' NÃO encontrada na raiz.")
        erros += 1

    # 3. Verificar pasta wwr
    pasta_wwr = raiz / "wwr"
    if pasta_wwr.is_dir():
        print("[SUCESSO] Pasta 'wwr' encontrada.")
        index_wwr = pasta_wwr / "index.html"
        if index_wwr.is_file():
            print("[SUCESSO] index.html encontrado dentro da pasta 'wwr'.")
        else:
            print("[AVISO] A pasta 'wwr' existe, mas falta o arquivo 'index.html' dentro dela.")
            avisos += 1
    else:
        print("[ERRO] Pasta 'wwr' NÃO encontrada na raiz (necessária para o template do curso).")
        erros += 1

    print("\n========================================")
    print(f"Verificação concluída com {erros} erro(s) e {avisos} aviso(s).")
    if erros == 0:
        print("Tudo pronto! Sua estrutura local atende aos requisitos.")
    else:
        print("Corrija os erros acima antes de enviar para o GitHub.")

if __name__ == "__main__":
    auditar_projeto()