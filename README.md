# 📚 API de Gestão de Alunos e Disciplinas 🎓

Bem-vindo à API de Gestão de Alunos e Disciplinas! Esta API permite a criação de alunos, disciplinas e a atribuição de tarefas aos alunos com base em suas disciplinas. É uma extensão de uma API de tarefas simples.

## 🚀 Recursos Principais

- **Alunos:** Crie, atualize, liste e exclua informações sobre os alunos.
- **Disciplinas:** Gerencie disciplinas, incluindo criação, atualização e listagem.
- **Tarefas:** Atribua tarefas a alunos específicos com base nas disciplinas.

## 🛠 Tecnologias Utilizadas
- Python
- djangorestframework
- Postman

## 🔧 Configuração

-  Clone o repositório:

   ```
   git clone https://github.com/GabrielHenrique-K/DJANGO-API-CONTROLE-ESCOLAR.git
    ```

## ⚙️ Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, siga estas etapas em seu CODER:

- Baixe o Python antes de iniciar a Configuração
-   **Crie um ambiente virtual:**

    ```
    python -m venv .env 
    ```

- Utilize o seguinte comando:

    ```
    .env\Scripts\activate
    ```

-  Logo Após, utilize:

    ```
    pip install djangorestframework
    ```

- **Instale as dependências:**

    ```
    pip install -r requirements.txt
    ```

- **Crie as migrações:**

    ```
    python manage.py makemigrations
    ```
- **Realize as migrações no Banco de Dados:**

    ```
    python manage.py migrate
    ```

- **Inicie o servidor de desenvolvimento:**
    ```
    python manage.py runserver
    ```

Com essas etapas concluídas, sua API estará pronta para uso localmente.

## 📄 Documentação da API

A documentação completa da API está disponível [aqui](https://drive.google.com/file/d/1FPlsYdy8ANm1UckuJhp9x30-YeORClWq/view?usp=drive_link).

## Uso/Exemplos

```
- Json Criar Aluno
{
    "nome": "gabriel",
    "email": "gabriel@senai"
}
```


## Documentação da API

#### Criar Aluno 🔽

```http
  POST /controle
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `nome e email` | `Char` | **Obrigatório**. Nome e Email  |

#### Após o POST, retorna o ID gerado, nome e email criados para o Aluno.

#### Retorna Aluno 🔽

```http
  GET /controle/alunos/${1} (Gerado automaticamente depois do POST de criação)
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do Aluno |

#### Retorna o aluno da ID escolhida podendo alterar suas informações com método PUT, ou Deletar o Aluno.

#### Retorna Todos os Alunos 🔽

```http
  GET /controle/alunos/ 
  ```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `/alunos`      | `string` | **Obrigatório**. Aba Alunos |

#### Volta todas as informações de todos os alunos registardos.



