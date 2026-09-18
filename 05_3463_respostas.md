1. Pessoa, Iguarias e Restaurante são as classes base de funcionário, pizza, bolo e pizzaria. Já funcionário é a classe base de garçom, chefe de cozinha e gerente.

2. Iguaria e Restaurante são classes diferentes; cada subclasse em Restaurante herda ou não certas subclasses de Iguaria. Pode-se fazer atributos como doce/salgado/sobremesas/etc.

3. Garçom: anotar_pedido( arg1 ) -> tipo = Iguaria; Chefe de cozinha: preparar( agr2 ) -> tipo = Iguaria; Gerente: demitir( arg3 ) -> tipo = Funcionário.