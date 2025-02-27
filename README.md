
                                     desafio 1
O controle de versão, também conhecido como controle de fonte, é a prática de rastrear e gerenciar as alterações em um código de software. Os sistemas de controle de versão são ferramentas de software que ajudam as equipes de software a gerenciar as alterações ao código-fonte ao longo do tempo. Como os ambientes de desenvolvimento aceleraram, os sistemas de controle de versão ajudam as equipes de software a trabalhar de forma mais rápida e inteligente. Eles são ainda mais úteis para as equipes de DevOps, pois as auxiliam a reduzir o tempo de desenvolvimento e aumentar as implementações bem-sucedidas.

O software de controle de versão mantém registro de todas as modificações no código em um tipo especial de banco de dados. Se um erro for cometido, os desenvolvedores podem voltar no tempo e comparar versões anteriores do código para ajudar a corrigir o erro enquanto diminuem interrupções para todos os membros da equipe.                     
                           
algumas vantagens sobre o controle de versão é: 
historico de alteração
colaboração
recuperação de erros
geranciamento de realeses
trabalho de ramificações (branches) 

À também alguns exemplos como:
Git
Subversion(SVN)
Mercurial

                                         desafio 2
Programação Orientada a Objetos (POO) é uma abordagem de desenvolvimento de software que se concentra em modelar o mundo real através de objetos. Imagine que estamos construindo um software que simula uma cidade. Em vez de pensar em apenas funções e dados separados, na POO, pensamos em termos de entidades, ou objetos, como carros, prédios, pessoas, etc. Cada um desses objetos tem suas próprias características (como cor ou altura) e comportamentos (como dirigir ou falar).

Quando criamos um objeto, estamos essencialmente criando uma instância de uma classe, que é como uma planta baixa ou um modelo que define o que aquele tipo de objeto deve ser e fazer. Por exemplo, uma classe Carro pode definir que todos os carros têm um número de portas, uma cor e a capacidade de acelerar. Cada carro que criamos a partir dessa classe terá esses atributos, mas com valores específicos, como "vermelho" ou "quatro portas".

Além disso, a POO nos permite agrupar dados e funcionalidades em um único lugar, chamado de objeto, tornando o código mais organizado e modular. Podemos pensar em objetos como pequenos programas dentro de um programa maior, cada um com seu próprio conjunto de dados e funções, mas capazes de interagir entre si. Isso facilita a manutenção do código e a adição de novas funcionalidades, pois podemos alterar ou adicionar objetos sem afetar todo o sistema.

os seus pilares são os seguintes:
Encapsulamento
Herança
Abstração
Polimorfismo

Abstração:
No contexto computacional, uma abstração é uma representação que oculta especificidades para um consumidor de serviços, tornando sua utilização mais genérica e de fácil entendimento. Um bom exemplo é o sistema operacional (S.O) do seu laptop. Ele abstrai todos os detalhes de como o computador funciona.

Encapsulamento:
O conceito de encapsulamento está intimamente ligado ao conceito de ocultamento da informação (information hiding). Imagine em sua casa, como seria se outras pessoas, que não são seus familiares ou amigos, entrassem sem permissão e usassem suas coisas.

Herança:
De modo simplificado, herança é "uma classe (classe filha) que tem os mesmos atributos de outra (classe mãe), mais alguns atributos distintos". Alguns exemplos podem ser vistos abaixo: Exemplo 1: Uma classe Cliente que é a classe principal e duas classes filhas da mesma, "Pessoa Física" e "Pessoa jurídica".

Poliforfismo:
Polimorfismo é a característica única de linguagens orientadas a objetos que permite que diferentes objetos respondam a mesma mensagem cada um a sua maneira. Em termos de programação, polimorfismo representa a capacidade de uma única referência invocar métodos diferentes, dependendo do seu conteúdo.

algumas vantagens da POO:
Encapsulamento
Reutilização de Código
Manutenção Simplificada
Colaboração Eficiente
Modelagem Realista
                                             
                                       desafio 3
Desafio 3: É um protocolo que permite a obtenção de recursos, como documentos HTML. É a base de qualquer troca de dados na Web e um protocolo cliente-servidor, o que significa que as requisições são iniciadas pelo destinatário, geralmente um navegador da web.
Informa ao seu navegador como e comunicar com o servidor de um site, a fim de enviar e recuperar informações; quando é HTTPS, significa que é o HTTP seguro, que possui alguns padrões de segurança e texto criptografado.
A arquitetura REST permite a comunicação entre aplicações. Quando se abre o navegador, o REST estabelece uma conexão TCP/IP com o servidor de destino. Ele envia uma requisição GET HTTP a partir do endereço informado. Por sua vez, o servidor envia uma resposta HTTP ao navegador.
APIs Web e REST são usados para construir aplicativos que fornecem recursos e se comunicam através de HTTP. Enquanto REST descreve restrições arquitetônicas sobre interface uniforme, as Web APIs são geralmente um conceito que pode ser RESTful dependendo da implementação.
O REST utiliza os métodos a seguir de solicitações HTTP:
GET: Recuperar dados de um recurso do servidor
POST: Enviar dados ao servidor para criar 
PUT: Atualizar completamente um recurso existente ou criar um recurso se ele não existir 
PATCH: Atualizar parcialmente um recurso existente
DELETE: Remover um recurso do servidor
HEAD: Recuperar cabeçalhos de resposta para um recurso, sem o corpo da resposta
OPTIONS: Recuperar as opções de comunicação permitidas para um recurso ou o servidor inteiro.
TRACE: Realizar um loopback de teste para verificar o caminho percorrido por uma mensagem até destino final.


                             desafio 4
Uma camada, em arquitetura de software, é um nível de abstração que agrupa componentes ou funcionalidades de uma aplicação com responsabilidades semelhantes. Cada camada tem um papel específico na estrutura do software, ajudando a organizar o código de maneira que seja mais fácil de entender, manter e escalar.

Entity: Em uma API organizada em camadas, a camada Entity é responsável por representar o modelo de dados da aplicação, definindo classes que correspondem às tabelas do banco de dados. 

Controller: A camada Controller lida com requisições HTTP, atuando como intermediária entre o cliente e a lógica de negócio, interpretando dados da requisição e retornando respostas apropriadas. 

Service: A camada Service contém a lógica de negócio da aplicação, orquestrando operações complexas e chamando a camada de Repository para realizar operações de acesso e manipulação de dados. 

Repository: A camada Repository é responsável por gerenciar o acesso a dados e operações de persistência, realizando operações CRUD diretamente no banco de dados. 

                              desafio 5
Um padrão de projeto é uma solução reutilizável para um problema comum que ocorre em um determinado contexto no desenvolvimento de software. Eles são como receitas ou guias que ajudam a resolver problemas de design recorrentes de maneira eficiente e eficaz, facilitando a comunicação entre desenvolvedores e melhorando a manutenção e a evolução do software. Utilizamos padrões de projeto por várias razões. Primeiramente, eles promovem boas práticas de design, ajudando a criar sistemas que são mais flexíveis, reutilizáveis e fáceis de entender. Padrões de projeto também fornecem uma linguagem comum entre desenvolvedores, o que facilita a comunicação e o entendimento do código. 

A arquitetura de software é o processo de definir uma estrutura para um sistema de software e as diretrizes para sua evolução. Ela descreve os componentes principais do sistema, as suas relações, e como eles interagem uns com os outros para alcançar os objetivos do sistema.

Os propósitos da arquitetura de software são:

Visão Geral do Sistema: Oferece uma compreensão clara da estrutura e funcionamento do sistema.
Facilitação da Tomada de Decisões: Orienta escolhas sobre tecnologias, frameworks e padrões, ajudando a identificar riscos.
Reusabilidade e Mantenabilidade: Promove a reutilização de componentes e facilita a manutenção e evolução do sistema.
Escalabilidade e Desempenho: Garante que o sistema possa crescer e operar eficientemente.
Segurança e Confiabilidade: Assegura a proteção de dados e a continuidade do serviço.
Comunicação e Colaboração: Facilita a comunicação entre as equipes, alinhando objetivos técnicos e de negócios.

A sigla SOLID representa cinco princípios de design para melhorar a qualidade do software orientado a objetos:

Single Responsibility Principle (Princípio da Responsabilidade Única):* Cada classe deve ter uma única responsabilidade ou razão para mudar.

Open/Closed Principle (Princípio do Aberto/Fechado):* Classes devem ser abertas para extensão, mas fechadas para modificação.

Liskov Substitution Principle (Princípio da Substituição de Liskov):* Objetos de classes derivadas devem poder substituir objetos de classes base sem alterar o comportamento esperado.

Interface Segregation Principle (Princípio da Segregação de Interface):* Classes não devem ser obrigadas a implementar interfaces que não utilizam; é melhor usar interfaces pequenas e específicas.

Dependency Inversion Principle (Princípio da Inversão de Dependência):* Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações.


