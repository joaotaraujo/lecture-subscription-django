<h2> Projeto web para gerenciar inscrições em palestras (Django e Bootstrap) </h2>

O sistema de inscrição em palestras é composto pela área de acesso público, e pela área de análise das inscrições, que exige autenticação.

**Para rodar o projeto:** python manage.py runserver

**Para acessar o projeto:** localhost:8000


**Conta de administrador**

**Usuário:** administrador

**Senha:** administrador123


<h4>Área pública</h4>

**Tela de inscrição na palestra:** É a tela inicial do sistema, onde é permitido ao usuário se inscrever em uma palestra.

**Requisitos**

1. Todos os dados são obrigatórios.
2. Todos os arquivos devem ser anexados.
3. Os arquivos devem ser obrigatoriamente no formato PDF.
4. Após gravar as informações o sistema deve informar ao usuário o número da sua 
inscrição para consulta posterior;
5. O número deve ser gerado automaticamente pelo sistema;
6. A inscrição pode ter 3 status: pendente, aceita, não aceita;
7. A inscrição recebe inicialmente o status “pendente”.

**Tela de consulta de inscrição:** Nesta tela é permitido ao usuário consultar se sua inscrição foi aceita, bastando que seja informado o número recebido no ato do envio da inscrição.

**Requisitos**

1. Caso o número de inscrição não exista, é exibida a mensagem “O número de inscrição 
não foi encontrado”.
2. Caso a inscrição esteja pendente, é exibida a mensagem “Caro <nome do usuário>, sua 
inscrição ainda está pendente de análise”, onde <nome do usuário> deve ser 
substituído pelo nome informado no ato da inscrição;
3. Caso a inscrição tenha sido aceita, é exibida a mensagem “Caro <nome do usuário>, 
sua inscrição foi aceita.”, onde <nome do usuário> deve ser substituído pelo nome 
informado no ato da inscrição;
4. Caso a inscrição não tenha sido aceita, é exibida a mensagem “Caro <nome do 
usuário>, sua inscrição não foi aceita pelo motivo: <motivo>”, onde <nome do usuário> deve ser substituído pelo nome informado no ato da inscrição, e <motivo> 
pelo motivo informado pelo responsável que realizou a análise da inscrição.



<h4>Área de análise de inscrições</h4>

**Tela de listagem de todas as inscrições:** Essa página deve ser exibida assim que o usuário efetuar logon no sistema. O usuário para acesso deve ser “administrador”, e a senha deve ser “administrador123”. Nesta tela são exibidas todas as inscrições realizadas pelo público. Deve ser exibida uma listagem das inscrições realizadas, onde são exibidos todos os dados (nome, CPF e data de nascimento). Ao se clicar em uma inscrição, o usuário é levado até outra tela para análise da inscrição.

**Requisitos**

1. Devem ser listadas todas as inscrições, independente do aceite;
2. A primeira coluna da listagem deve ser o número da inscrição;
3. Nas demais colunas devem ser listados todos os dados informados na inscrição (nome, 
CPF e data de nascimento), nesta mesma ordem;
4. A última coluna deve informar se a inscrição foi aceita;
5. O número da inscrição deve ser um link, que leva até a página de análise de inscrições.

**Tela de análise da inscrição:** Nessa tela devem ser exibidos todos os dados informados no cadastro, deve permitir fazer download dos arquivos anexados na inscrição, e informar se a inscrição foi aceita, e o motivo em caso de a inscrição não ter sido aceita.

**Requisitos**

1. Devem ser exibidos todos os dados informados na inscrição (nome, CPF e data de 
nascimento), nesta mesma ordem;
2. Deve ser permitido fazer o download dos arquivos anexados no ato da inscrição;
3. Deve ser permitido ao usuário logado informar se a inscrição foi ou não aceita;
4. Deve ser permitido que o usuário logado informe o motivo caso a inscrição não tenha
sido aceita;
5. O campo <motivo> deve ser desabilitado caso a informação de aceite da inscrição seja 
“aceita” ou “pendente”;
6. As informações devem ser persistidas quando o usuário clicar em “gravar”, e o sistema 
deve retornar para a “Tela de listagem de todas as inscrições”
