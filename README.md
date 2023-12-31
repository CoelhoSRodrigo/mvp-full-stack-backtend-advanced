# MVP PUC-Rio Doghouses - Back-end

Projeto de MVP do módulo Desenvolvimento Back-end Avaçando da **Pós-Graduação em Desenvolvimento Full Stack**, do Departamento de Informática da PUC-Rio.

Aluno: **Rodrigo dos Santos Coelho** (*https://www.linkedin.com/in/rodrigoscoelho/*)

---
##  Vídeo Youtube

https://www.youtube.com/watch?v=SL4zf5Aanl0

---
## Primeiros passos

Para executar este projeto é necessário que todas as libs Python descritas no arquivo `requirements.txt` sejam instaladas. 
Após clonar o repositório do GitHub (*https://github.com/CoelhoSRodrigo/mvp-full-stack-backtend-advanced/*), é necessário ir ao diretório raiz, pelo terminal do Visual Studio Code, para que possa executar os comandos descritos abaixo.

```
python3 -m venv env  (Linux ou macOS)
python -m venv env  (Windows)
```
```
source env/bin/activate (Linux ou macOS)
.\env\Scripts\Activate.ps1 (Windows)

```

> O primeiro comando `python3 -m venv env`, iremos utilizar para a criação do ambiente virtual, já o segundo comando, `source env/bin/activate`, será para ativá-lo.

> Não é necessário digitar o `(env)` nos comandos abaixo, uma vez que ele apenas está listado para lembrar que está sendo executado com o ambiente virtual criado e ativo.

```
(env) pip install -r requirements.txt
```

> O comando acima instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env) flask run --host 0.0.0.0 --port 5000 --reload
```

> O comando acima instala o framework Flask. Pelo fato de estarmos utilizando o parâmetro `--reload`, o servidor web reiniciará automaticamente após uma mudança no código fonte. 

> Caso esteja o utilizando o macOS, pode ser que o AirPlay Receiver, ou outtra aplicação do sistema operacional, já esteja utilizando a portal 5000, sendo assim mude para a porta 5001 ao invés de 5000 no comando do `flask run --host 0.0.0.0 --port 5000 --reload`, caso receba algum alerta do sistema operacional.


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
