<h1> Rede CNN - Keras - Kaggle </h1>

Repositório criado para trabalho pratico da disciplina de Inteligência Artificial.

Unisinos - 2022/1

Link do Notebook no GoogleColab: (https://colab.research.google.com/drive/1G7uIH4UvCKWCW-TYUIXhz2kSMkTv4J17?hl=pt_BR#scrollTo=ES4NAnxmYfiJ)


<h2> Objetivo do Trabalho: </h2>

Deve ser implementada uma rede neural do tipo Convolutional Neural Network (CNN) para a classificação de 
imagens. 
A rede deve ser implementada do zero utilizando o [Keras](https://keras.io/). 

A rede neural deve ser treinada e testada em um conjunto de dados de escolha do grupo. O dataset deve abordar 
o problema de classificação de imagens.

<h2> Representação do Problema - Escolha e Configuração inicial do DataSet </h2>

Eu escolhi o dataset do Kaggle [BIRDS 400 - SPECIES IMAGE CLASSIFICATION](https://www.kaggle.com/datasets/gpiosenka/100-bird-species). 
O Conjunto de dados possui 400 espécies de aves.
Sendo, 58388 imagens de treinamento, 2000 imagens de teste (5 imagens por espécie) e 2000 imagens de validação (5 imagens por espécie).  
As imagens possuem tamanho de 224x224, e formato de cores RGB. Todas elas possuem apenas 1 pássaro que ocupa cerca de 50% da imagem.

O principal objetivo desse trabalho é conseguir gerar uma rede CNN que consiga realizar a classificação correta das espécies, considerando o conjunto de teste, para cada imagem a rede deve predizer qual a espécie correspondente.

Decidi, como sugestão do professor, reduzir o número de espécies possíveis para facilitar a resolução do problema, dessa forma trabalharei com 10 espécies, as quais serão definidas no código.

Inicialmente, utilizei um código padrão para acessar e realizar o download do dataset. 
Após descompactar, criei um diretório '100-bird-species/' que será o root e joguei todos os arquivos lá. 

A estrutura deve ser a seguinte:

![image](https://user-images.githubusercontent.com/58199187/174257907-08450017-70f4-4553-8503-a1e52e327e29.png)

<h2>Resultados </h2>

A acurácia obtida foi de 93,99%
![image](https://user-images.githubusercontent.com/58199187/174258246-b64e05d1-dd7c-44d6-b697-3a9a2457ebe7.png)

