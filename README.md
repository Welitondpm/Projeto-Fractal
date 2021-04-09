# Projeto-Fractal
 
## Dependências:
* Python 3
 #### Downloads
 * Windos / Mac: [Clique Aqui!](https://www.python.org/downloads/)
 * Linux: `$ sudo apt-get install python3`
 
* Matplotlib
 #### Download e Instalação
 `$ python -m pip install -U pip`
 `$ python -m pip install -U matplotlib`
 
## Fractais produzidos e estudados durante o Projeto:
 
* <a href="cantor_set"> Cantor Set | Conjunto de Cantor </a>
* <a href="dragon_curve"> Dragon Curve | Curva do Dragão </a>
* <a href="hilbert_curve"> Hilbert Curve | Curva de Hilbert </a>
* <a href="inverted_binary"> Inverted Binary | Binário Invertido </a>
* <a href="koch_curve"> Koch Curve | Curva de Koch </a>
 * <a href="flake"> Koch Flake | Floco de Koch</a>
 * <a href="koch_tetrahedron">Koch Tetrahedron | Tetraedro de Koch</a>
* <a href="mandelbrot"> Mandelbrot </a>
 * <a href="logarithmic_mandelbrot"> Logarithmic Mandelbrot | Mandelbrot Logarítmico </a>
 * <a href="harmonic_mandelbrot"> Harmonic Mandelbrot | Mandelbrot Harmônico </a>
 * <a href="segmented_mandelbrot"> Segmented Mandelbrot | Mandelbrot Segmentado </a>
* <a href="logistic_map"> Logistic Map | Mapa Logístico </a>
* <a href="Logistic Mandelbrot"> Logistic Mandelbrot | Mandelbrot Logístico </a>
* <a href="sierpinski_triangle"> Sierpinski Triangle | Triângulo de Sierpinski </a>
 * <a href="sierpinski_carpet"> Sierpinski Carpet | Tapete de Sierpinski </a>
 * <a href="sierpinski_tetrahedron"> Sierpinski Tetrahedron | Tetraedro de Sierpinski </a>
   * <a href="colorful_sierpinski_tetrahedron"> Colorful Sierpinski Tetrahedron | Tetraedro de Sierpinski Colorido </a>
 * <a href="menger_sponge"> Merger Sponge | Esponja de Menger </a>
   * <a href="colorful_menger_sponge"> Colorful Merger Sponge | Esponja de Menger Colorida </a>
* <a href="sierpinski_arrowhead"> Sierpinski Arrowhead | Ponta de Seta de Sierpinski </a>
* <a href="sierpinski_triangle_chaotic"> Sierpinski Triangle (Chaotic) | Triângulo de Sierpinski (Caótico) </a>
* <a href="sierpinski_triangle_pascal"> Sierpinski Triangle from Pascal's Triangle | Triângulo de Sierpinski no Triângulo de Pascal </a>
* <a href="tree"> Tree | Árvore </a>
<hr>
## Cantor Set | Conjunto de Cantor <a name="cantor_set"></a>
 
#### Definição:
Este fractal é resultado de um algoritmo que, a cada iteração, remove a terça parte central de cada segmento ou do resultado da iteração anterior.
 
![Imagem Cantor Set](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/cantor_set.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/cantor_set.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Dragon Curve | Curva do Dragão <a name="dragon_curve"></a>
 
#### Definição:
Esse fractal surge ao sempre copiar o(s) segmento(s) do iniciador ou do conjunto de retas já computado após uma rotação de um quarto de volta, tendo como eixo de rotação uma das extremidades deste.
 
![Imagem Dragon Curve](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/dragon_curve.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/dragon_curve.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Hilbert Curve | Curva de Hilbert <a name="hilbert_curve"></a>
 
#### Definição:
Essa curva de preenchimento de espaço é gerada acrescentando ao iniciador ou ao resultado da iteração anterior uma cópia transladada à direita, outra transladada para cima e rotacionada 90º e uma quarta transladada para a direita e para cima rotacionada 270º (ou -90º). Ao final, após o redimensionamento, todos os pontos com coordenadas reais estão inclusos nessa curva.
 
![Imagem Hilbert Curve](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/hilbert_curve.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/hilbert_curve.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Inverted Binary | Binário Invertido <a name="inverted_binary"></a>
 
#### Definição:
Este fractal é resultado de um algoritmo que, para cada valor natural do eixo das abscissas, ele atribui um valor no eixo das ordenadas que é a diferença entre o número, e o próprio número lido da direita para a esquerda em base 2; caso esse seja primo.
 
![Imagem Inverted Binary](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/inverted_binary.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/inverted_binary.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Koch Curve | Curva de Koch <a name="koch_curve"></a>
 
#### Definição:
Em cada iteração, cada segmento é substituído por n segmentos com um terço do seu comprimento, com as extremidades coincidindo e os segmentos centrais inclinados em g[180 * (n-2)] / n graus, com g sendo a ordinalidade de cada segmento central.
 
![Imagem Koch Curve](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/koch_curve.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/koch.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
 
#### Derivados: 
* <a href="flake"> Koch Flake | Floco de Koch</a>
* <a href="koch_tetrahedron">Koch Tetrahedron | Tetraedro de Koch</a>
<hr>
## Koch Flake | Floco de Koch <a name="flake"></a>
 
#### Definição:
Um polígono regular de n lados com uma Curva de Koch no lugar de cada um.
 
![Imagem Koch Flake](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/flake.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/flake.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Koch Tetrahedron | Tetraedro de Koch <a name="koch_tetrahedron"></a>
 
#### Definição:
Um tetraedro regular que a cada iteração adquire tetraedros com uma das faces formadas pelos pontos médios das arestas de cada face do resultado da iteração anterior.
 
![Imagem Koch Tetrahedron](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/koch_tetrahedron.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/koch_tetrahedron.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Mandelbrot <a name="mandelbrot"></a>
 
#### Definição:
O conjunto dos números complexos que não aumentam indefinidamente em módulo ao serem elevados ao quadrado e somados a si mesmos infinitas vezes.
 
![Imagem Mandelbrot](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/mandelbrot.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/mandelbrot.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
 
#### Derivados:
* <a href="logarithmic_mandelbrot"> Logarithmic Mandelbrot | Mandelbrot Logarítmico </a>
* <a href="harmonic_mandelbrot"> Harmonic Mandelbrot | Mandelbrot Harmônico </a>
* <a href="segmented_mandelbrot"> Segmented Mandelbrot | Mandelbrot Segmentado </a>
<hr>
## Logarithmic Mandelbrot | Mandelbrot Logarítmico <a name="logarithmic_mandelbrot"></a>
 
#### Definição:
O conjunto de Mandelbrot, com as cores periféricas se dando em função do crescimento logarítmico do contador de iterações.
 
![Imagem Logarithmic Mandelbrot](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/logarithmic_mandelbrot.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/mandelbrot.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Harmonic Mandelbrot | Mandelbrot Harmônico <a name="harmonic_mandelbrot"></a>
 
#### Definição:
O conjunto de Mandelbrot, com as cores periféricas se dando em função do crescimento harmônico do contador de iterações.
 
![Imagem Harmonic Mandelbrot](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/harmonic_mandelbrot.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/mandelbrot.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Segmented Mandelbrot | Mandelbrot Segmentado <a name="segmented_mandelbrot"></a>
 
#### Definição:
O conjunto de Mandelbrot, com as cores periféricas se dando em função do crescimento aritmético do contador de iterações.
 
![Imagem Segmented Mandelbrot](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/segmented_mandelbrot.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/mandelbrot.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Logistic Map | Mapa Logístico <a name="logistic_map"></a>
 
#### Definição:
Resultados estáveis da soma de números reais com o quadrado do resultado da iteração anterior.
 
![Imagem Logistic Map](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/logistic_map.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/mandelbrot.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Logistic Mandelbrot | Mandelbrot Logístico <a name="logistic_mandelbrot"></a>
 
#### Definição:
O conjunto de Mandelbrot, com as partes reais estáveis registradas no terceiro eixo.
 
![Imagem Logistic Mandelbrot](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/logistic_mandelbrot.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/mandelbrot.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Sierpinski Triangle | Triângulo de Sierpinski <a name="sierpinski_triangle"></a>
 
#### Definição:
Esse fractal se define como um triângulo equilátero, do qual é subtraído o triângulo equilátero formado pelos pontos médios de seus lados; sendo o mesmo feito para todos os triângulos equiláteros restantes ad infinitum.
 
![Imagem Sierpinski Triangle](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/sierpinski_triangle.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
 
#### Derivados:
* <a href="sierpinski_carpet"> Sierpinski Carpet | Tapete de Sierpinski </a>
* <a href="sierpinski_tetrahedron"> Sierpinski Tetrahedron | Tetraedro de Sierpinski </a>
* <a href="menger_sponge"> Merger Sponge | Esponja de Menger </a>
<hr>
## Sierpinski Carpet | Tapete de Sierpinski <a name="sierpinski_carpet"></a>
 
#### Definição:
Esse fractal se define como um quadrado, do qual é subtraído o quadrado de centro comum, igual orientação e lado com um terço do comprimento do lado do quadrado anterior; ao que se segue realizando o mesmo aos quatro quadrados com lados comuns e quatro quadrados diagonais ao quadrado subtraído.
 
![Imagem Sierpinski Carpet](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/sierpinski_carpet.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Sierpinski Tetrahedron | Tetraedro de Sierpinski <a name="sierpinski_tetrahedron"></a>
 
#### Definição:
Esse fractal se define como um tetraedro, do qual é subtraído o tetraedro de centro comum, igual vertical contrária e aresta com um terço do comprimento da aresta do tetraedro anterior; ao que se segue realizando o mesmo aos quatro tetraedros com faces comuns ao tetraedro subtraído.
 
![Imagem Sierpinski Tetrahedron](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/sierpinski_tetrahedron.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
 
#### Derivados:
* <a href="colorful_sierpinski_tetrahedron"> Colorful Sierpinski Tetrahedron | Tetraedro de Sierpinski Colorido </a>
<hr>
## Colorful Sierpinski Tetrahedron | Tetraedro de Sierpinski Colorido<a name="colorful_sierpinski_tetrahedron"></a>
 
#### Definição:
Um Tetraedro de Sierpinski cuja luminosidade é inversamente proporcional ao módulo de cada ponto. 
 
![Imagem Colorful Sierpinski Tetrahedron](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/colorful_sierpinski_tetrahedron.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Menger Sponge | Esponja de Menger <a name="menger_sponge"></a>
 
#### Definição:
Esse fractal se define como um cubo, do qual é subtraído o cubo de centro comum, igual orientação e aresta com um terço do comprimento da aresta do cubo anterior; ao que se segue realizando o mesmo aos seis cubos com faces comuns e oito cubos diagonais ao cubo subtraído.
 
![Imagem Menger Sponge](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/menger_sponge.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/menger.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
 
#### Derivados:
* <a href="colorful_menger_sponge"> Colorful Merger Sponge | Esponja de Menger Colorida </a>
<hr>
## Colorful Menger Sponge | Esponja de Menger Colorida <a name="colorful_menger_sponge"></a>
 
#### Definição:
Uma Esponja de Menger colorizada de acordo com a posição espacial dos pontos transcrita para RGB.
 
![Imagem Colorful Menger Sponge](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/colorful_menger_sponge.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/menger.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Sierpinski Arrowhead | Ponta de seta de Sierpinski <a name="sierpinski_arrowhead"></a>
 
#### Definição:
Uma curva que tende a formar um Triângulo De Sierpinski. A semente são três segmentos, as extremidades coincidentes ao segmento original e o segmento central paralelo.
 
![Imagem Sierpinski Arrowhead](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/sierpinski_arrowhead.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Sierpinski Triangle (Chaotic) | Triângulo de Sierpinski (Caótico) <a name="sierpinski_triangle_chaotic"></a>
 
#### Definição:
Esse fractal é gerado marcando os pontos que, a cada iteração, vê-se o ponto médio entre o anterior e um dos vértices que é escolhido aleatóriamente.
 
![Imagem Sierpinski Triangle (Chaotic)](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/sierpinski_triangle_chaotic.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Sierpinski Triangle from Pascal’s Triangle | Triângulo de Sierpinski no Triângulo de Pascal <a name="sierpinski_triangle_pascal"></a>
 
#### Definição:
Triângulo de Sierpinski formado pelos números ímpares do Triângulo de Pascal.
 
![Imagem Sierpinski Triangle from Pascal’s Triangle](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/sierpinski_triangle_pascal.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/sierpinski.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>
<hr>
## Tree | Árvore <a name="tree"></a>
 
#### Definição:
A semente são três segmentos concorrentes em um ponto. Inclinação e tamanho customizáveis.
 
![Imagem Tree](https://github.com/Welitondpm/Projeto-Fractal/blob/master/Imgs/tree.png)
 
#### Variáveis de Input:
 
#### Código: <a href="https://github.com/Welitondpm/Projeto-Fractal/blob/master/Fractals/tree.py" target="_blank">Clique aqui (o código será aberto em outra aba)</a>


