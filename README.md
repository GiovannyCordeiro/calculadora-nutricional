## Setup do projeto

- Instale todas as dependencias e ambiente virtual com o comando `poetry install`
- Para executar comandos adequadamente do projeto execute o ambinte virtual com o comando `poetry shell`

> É muito importante executar o ambiente virtual com o comando `poetry shell`
> caso contrario pode ser que a execução dos comandos não executem adequadamente.


## Requisitos para trabalho

- Utilizar os esquemas de branch do [git flow](https://www.alura.com.br/artigos/git-flow-o-que-e-como-quando-utilizar)
- Utilizar [commits semanticos (ou também chamado de Padrões de commits)](https://github.com/iuricode/padroes-de-commits)

- Desenvolvimento de três funcionalidades
  - [x] Menu principal no terminal | Feito por Bianca
  - [x] Calculo do IMC (indicie de massa corporal) | Feito por Bianca
  - [x] Calculo do TMB (Taixa de metabolismo basal) | Feito por Giovanny
  - [ ] Calculo do GET (Gasto energetico total)| A fazer por Viviane
  - [ ] Desenvolvimento de testes para cada modulo respectivo | Em progresso por todos!

- Utilização de 3 artefatos (bibliotecas, APIs e etc)
  - [x] Taskipy: Ferramenta responsavel por facilitar o processo de rodar comandos! | Feito por Giovanny
  - [x] Ruff (linter): Linter para manter o padrao no código | Feito por Giovanny
  - [x] Pytest: Biblioteca para realizar testes do código | Feito por Giovanny

- O software precisa realizar uma operação com arquivos do usuário (cliente) do software.
- [x] O Historico do peso do paciênte deve ser registrado em um documento. | Feito por Bianca

## Workflow do trabalho

Por favor, quando forem desenvolver suas respectivas funcionalidades, criem um branch
chamada `develop-seu-nome` para seguir o modelo do [git flow](https://www.alura.com.br/artigos/git-flow-o-que-e-como-quando-utilizar).

Faça commits pequenos para cada alteração no projeto e nomeei-os seguindo o [commits semanticos](https://github.com/iuricode/padroes-de-commits)

Sempre que começar o trabalho rode os seguintes comandos:
1. `git fetch origin`: Para atualizar a referencia da branch main
2. `git rebase origin/main`: Para atualizar a sua branch de desenvolvimento atual

# Rodar o projeto

- Execute o ambiente virtual com `poetry shell`
- Para rodar o projeto execute o comando `task run`