# Método Monte Carlo

O método Monte Carlo foi formalizado em 1949, por meio do artigo intitulado “Monte Carlo Method”, publicado por John Von Neumann e Stanislav Ulam.Também chamado de método das provas estatísticas, consiste na exploração das propriedades estatísticas dos números aleatórios para assegurar que o resultado correto é computado da mesma maneira que num jogo de cassino para se certificar de que a “casa” sempre terá lucro. As técnicas de Monte Carlo (MC) são algoritmos numéricos que utilizam números pseudo aleatórios para realizar cálculos matemáticos e modelar sistemas físicos ou para simulação de algum procedimento experimental.

## Amostragem direta

Considere um círculo de raio unitário inscrito em um quadrado de lado 2, conforme a figura 1. É
evidente que a razão entre a área do círculo e do quadrado é igual a π/4.

Se pontos são selecionados com probabilidade uniforme no interior do quadrado, a probabilidade que
um desses pontos esteja no interior do círculo é justamente π/4.  A tarefa consistiu em gerar uma amostra
de tamanho N de pontos. Conta-se como “sucesso” o ponto estar no interior do círculo. No caso de n
sucessos temos que π/4 é aproximadamente n/m.

![circulo](https://user-images.githubusercontent.com/71646387/148658141-f295b703-cc20-4cd3-9bab-79e14329c7e7.png)

Utilizando um algoritmo simples de Monte Carlo para calcularmos o valor de π usando uma sequência
de números aleatórios. Considerei um círculo de raio um inscrito no quadrado de lado dois; gerei
aleatoriamente um conjunto de pontos com coordenadas dentro do quadrado, é contabilizado o ponto se
estiver dentro do círculo, caso caia fora, não é contabilizado. A quantidade de pontos dentro do círculo
dividido pelo número total de pontos multiplicado por quatro é aproximadamente igual ao valor de π,
ou seja, 3.1415926. 

Podemos verificar nos gráficos a aproximação do valor de π em função do número de
pontos; a linha vermelha é referente ao valor 3.1415926..., denotado por π.

Abaixo, vemos o resultado da simulação para n=50.000.

