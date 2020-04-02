# Projeto-Fractal

## Fractais que já foram feitos:

<ul>
  <li><a href="#binario">Fractal Binário Invertido</a></li>
  <li><a href="#caotico">Fractal Triângulo de Sierpinski Caótico</a></li>
  <li><a href="#sierpinski">Fractal Triângulo de Sierpinski</a></li>
  <li><a href="#dragao">Fractal Curva do Dragão</a></li>
  <li><a href="#hilbert">Fractal Curva de Hilbert</a></li>
  <li><a href="#koch">Fractal Curva de Koch</a></li>
  <li><a href="#floco">Fractal Floco</a></li>
  <li><a href="#dpmfrr">Fractal dpmfrr</a></li>
  <li><a href="#dpmfrrumalinha">Fractal dpmfrr uma linha</a></li>
  <li><a href="#kochx">Fractal Curva de Koch X</a></li>
  <li><a href="#arvore">Fractal Árvore</a></li>
  <li><a href="#sierpinskilinear">Triângulo De Sierpinski Linear</a></li>
</ul>

### Conjunto dos Números Primos com as Casas Binárias Trocadas Subtraídos do Próprio Número <a name="binario"></a>

#### Definição:

Este fractal é resultado de um algoritmo que, para cada valor natural do eixo das abscissas, ele atribui um valor no eixo das ordenadas que é a diferença entre o número, e o próprio número lido da direita para a esquerda em base 2; caso esse seja primo

![fractal_binarioinvertido(524288)](https://user-images.githubusercontent.com/49809730/78200187-3bf9ce00-7464-11ea-8946-0e8f2affc6a5.png)

#### Variáveis de input:

<ul>
  <li><b>Fim:</b> Até que valor o fractal será feito recomendado uma potência de 2 (para processadores inferior ao i5 5ºg recomendado valor <= 2<sup>18</sup> = 262.144</li>
  <li><b>Contagem:</b> Mostrará em qual valor está sendo feito o calculo (para facilitar utilize 1 para sim e 0 para não)</li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_binarioinvertido.py"> Clique aqui </a>

### Triângulo de Sierpinky Gerado a partir de escolhas randômicas <a name="caotico"></a>

#### Definição:

Esse fractal é gerado marcando os pontos que, a cada iteração, vê-se o ponto méio entre o anterior e um dos vértices que é escolhido aleatóriamente.

![fractal_triangulocaotico(vezes100000)](https://user-images.githubusercontent.com/49809730/78200212-4e740780-7464-11ea-96f0-650bd785fb83.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes</b></li>
  <li><b>Passo???</b></li>
  <li><b>vamo acrescentar mais coisas, eu acho que com o mesmo codigo da pra fazer o tapete caótico.</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_triangulocaotico.py"> Clique aqui </a>

### Triângulo de Sierpinski <a name="sierpinski"></a>

#### Definição:

Esse fractal se define como um triângulo equilátero, do qual é subtraído o triãngulo equilátero formado pelos pontos médios de seus lados; sendo o mesmo feito para todos os triângulos equiláteros restante *ad infinitum*.

![fractal_triangulodesierpinski(vezes7_tamanho50)](https://user-images.githubusercontent.com/49809730/78200487-32249a80-7465-11ea-80c9-76cc8b38697b.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_triangulodesierpinski.py"> Clique aqui </a>

### Curva do Dragão <a name="dragao"></a>

#### Definição:

Esse fractal surge ao sempre copiar o(s) segmento(s) do iniciador ou do cunjunto de retas já computado após uma rotação de um quarto de volta, tendo como eixo de rotação o uma das extremidades desse.

![fractal_curvadodragrao(vezes22)img2](https://user-images.githubusercontent.com/49809730/78201211-6b5e0a00-7467-11ea-9eca-1503248ee06c.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
  <li><b> **vamo acrescentar mais opções**</b> </li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_curvadodragao.py"> Clique aqui </a>

### Curva de Hilbert <a name="hilbert"></a>

#### Definição:

Essa curva de preenchimento de espaço é gerada acrescentando ao iniciador ou ao conjunto de retas já computado uma cópia transladada à direita, outra transladada para cima e rotacionada 90º e uma quarta transladada para a direita e para cima rotacionada 270º (ou -90º).
Ao final, após o redimensionamento, todos os pontos com coordenadas reais estão inclusos nessa curva.

![fractal_curvadehilbert(vezes5)img2](https://user-images.githubusercontent.com/49809730/78201280-9e080280-7467-11ea-96b2-02cf0ee30c23.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_curvadehilbert.py"> Clique aqui </a>

### Curva de Koch <a name="koch"></a>

Em cada iteração, cada segmento é substituído por quatro segmentos com um terço do seu comprimento, com as extremidades coincidindo e os segmentos centrais inclinados em 60º e 300º(-60º) respectivamente.

![fractal_curvadekoch(vezes12)](https://user-images.githubusercontent.com/49809730/78201478-0ce55b80-7468-11ea-97e0-346aadb54cd8.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_curvadekoch.py"> Clique aqui </a>

### Floco de Koch <a name="floco"></a>

O iniciador é um triângulo, e cada um de seus lados passa pelo processo da Curva de Koch. Como resultado, esse polígono apresenta área finita, e um perímetro infinito.

![fractal_floco(vezes10)](https://user-images.githubusercontent.com/49809730/78201597-5cc42280-7468-11ea-9a22-0e9cc0c097b2.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_floco.py"> Clique aqui </a>

### Curva de Koch modificada para ângulos retos(Fractal dpmfrr) <a name="dpmfrrumalinha"></a>

Em cada iteração, cada segmento é substituído por cinco segmentos com um terço do seu comprimento, com as extremidades coincidindo, os adjascentes a esses sendo perpendiculares e o central paralelo ao original, mas transladado acima em um terço do comprimento.

![fractal_dpmfrrumalinha(vezes10)](https://user-images.githubusercontent.com/49809730/78200579-7f087100-7465-11ea-82d1-81c0467c9e6d.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_dpmfrrumalinha.py"> Clique aqui </a>

### Quadrado dpmfrr <a name="dpmfrr"></a>

O iniciador é um quadrado, e cada um de seus lados passa pelo processo da Curva de Koch modificada para ângulos retos. Como resultado, esse polígono apresenta área finita, e um perímetro infinito. Diferencia-se do Fractal dpmfrr X porque seus pontos contados em sentido horário aumentam a área do fractal em relação ao iniciador.

![fractal_dpmfrr(vezes8)](https://user-images.githubusercontent.com/49809730/78200561-757f0900-7465-11ea-9e4c-e91942250bcf.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_dpmfrr.py"> Clique aqui </a>

### Fractal dpmfrr X <a name="kochx"></a>

O iniciador é um quadrado, e cada um de seus lados passa pelo processo da Curva de Koch modificada para ângulos retos. Como resultado, esse polígono apresenta área nula, e um perímetro infinito. Diferencia-se do Quadrado dpmfrr porque seus pontos contados em sentido anti-horário diminuem a área do fractal em relação ao iniciador.

![fractal_curvadekochX(vezes10)](https://user-images.githubusercontent.com/49809730/78200601-8c256000-7465-11ea-9e1e-9946bdc33421.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_curvadekochX.py"> Clique aqui </a>

### Fractal Árvore <a name="arvore"></a>

A semente são três segmetos concorrentes. Inclinação e tamanho customizáveis incluiundo aleatórios.

![fractal_arvore(vezes17_ang15)](https://user-images.githubusercontent.com/49809730/78199712-db1dc600-7462-11ea-9251-1fab9133d297.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b></li>
  <li><b>Tamanho:</b></li>
  <li><b>Inclinação:</b></li>
  <li><b>Mudança no tamanho dos galhos por iteração:</b></li>
  <li><b>Taxa de randomização do aspecto:</b></li>
  <li><b>Mudança na inclinação dos galhos por iteração:</b></li>
  <li><b>Taxa de randomização do aspecto:</b></li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_arvore.py"> Clique aqui </a>

### Fractal Triângulo De Sierpinski Linear <a name="sierpinskilinear"></a>

Uma curva que tende a formar um Triângulo De Sierpinski. A semente são três segmentos, as extremidades coincidentes ao segmento original e o segmento central paralelo.

![fractal_triangulodesierpinskilinear(vezes10)](https://user-images.githubusercontent.com/49809730/78200625-a52e1100-7465-11ea-99f9-b0780185791f.png)

#### Variáveis de input:

<ul>
  <li><b>Vezes:</b> Quantidade de iterações</li>
</ul>

#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/fractais_prontos/fractal_triangulodesierpinskilinear.py"> Clique aqui </a>
