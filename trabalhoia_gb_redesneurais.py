# DOWNLOAD E CONEXÃO COM KAGGLE PARA ACESSAR DATASET
! pip install -q kaggle
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
! kaggle competitions download -c 'spaceship-titanic'
#DOWNLOAD DO DATASET
! kaggle datasets download gpiosenka/100-bird-species
! unzip 100-bird-species

#---------------------------------------------------------------------------------------------------------------------
#IMPORTAÇÃO DAS BIBLIOTECAS NECESSÁRIAS
import tensorflow
from tensorflow import keras
import tensorflow_hub as hub
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import ModelCheckpoint
from keras.utils.np_utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#DIRETÓRIO RAIZ DO DATASET
data_root='100-bird-species/'
#SEPARAÇÃO DAS IMAGENS EM TREINO E TESTE
train_data_dir = str(data_root+'train')
test_data_dir = str(data_root+'test')

#TAMANHO DA IMAGEM
image_shape = (224,224) 
#AJUSTE DA ESCALA E VALIDAÇÃO
data_kwargs = dict(rescale=1./255, validation_split=.20) 

#GERAÇÃO DOS DADOS A PARTIR DAS AMOSTRAS DE TREINO, VALIDAÇÃO E TESTE.
train_data = ImageDataGenerator(**data_kwargs)
train_generator = train_data.flow_from_directory(
    train_data_dir, #DIRETÓRIO ONDE ESTÃO AS IMAGENS
    subset="training", #CONJUNTO DE TREINO
    shuffle=True, #PADRÃO
    target_size=image_shape, #TAMANHO DA IMAGEM
    classes = ['ABBOTTS BABBLER', 'AFRICAN FIREFINCH', 'AZURE TIT', 'BARN OWL', 'BLACK BAZA', 
           'BLUE THROATED TOUCANET', 'CHATTERING LORY', 'COMMON IORA', 'CURL CRESTED ARACURI', 'DOUBLE BARRED FINCH'] 
           #CLASSES POSSÍVEIS
)

valid_data = ImageDataGenerator(**data_kwargs)
valid_generator = valid_data.flow_from_directory(#pego a partir do diretório do drive
    train_data_dir,  #DIRETÓRIO ONDE ESTÃO AS IMAGENS
    subset="validation",#CONJUNTO DE VALIDAÇÃO
    shuffle=True, #PADRÃO
    target_size=image_shape, #TAMANHO DA IMAGEM
    classes = ['ABBOTTS BABBLER', 'AFRICAN FIREFINCH', 'AZURE TIT', 'BARN OWL', 'BLACK BAZA', 
           'BLUE THROATED TOUCANET', 'CHATTERING LORY', 'COMMON IORA', 'CURL CRESTED ARACURI', 'DOUBLE BARRED FINCH'] 
           #CLASSES POSSÍVEIS
)

test_data = ImageDataGenerator(**data_kwargs)
test_generator = test_data.flow_from_directory(
    test_data_dir, #DIRETÓRIO ONDE ESTÃO AS IMAGENS
    target_size=image_shape, #TAMANHO DA IMAGEM
    classes = ['ABBOTTS BABBLER', 'AFRICAN FIREFINCH', 'AZURE TIT', 'BARN OWL', 'BLACK BAZA', 
           'BLUE THROATED TOUCANET', 'CHATTERING LORY', 'COMMON IORA', 'CURL CRESTED ARACURI', 'DOUBLE BARRED FINCH'] 
           #CLASSES POSSÍVEIS
)

#CARREGA O SHAPE DO BATCH DE TREINO
x_train, y_train = next(iter(train_generator)) # CARREGA O SHAPE DO BATCH DE TREINO
print("Image batch shape: ", x_train.shape) # DEVE PRINTAR (32, 224, 224, 3)
print("Label batch shape: ", y_train.shape) # DEVE PRINTAR (32, 15)
dataset_y = sorted(train_generator.class_indices.items(), key=lambda pair:pair[1]) # ORDENA OS ITENS
dataset_y = np.array([key.title() for key, value in dataset_y]) # RECUPERA AS CLASSES
print(dataset_y)


###CRIAÇÃO DA REDE CNN
modelo = keras.Sequential()

modelo.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu', input_shape=(224, 224, 3)))
modelo.add(MaxPooling2D(pool_size=2))
modelo.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
modelo.add(MaxPooling2D(pool_size=2))
modelo.add(Conv2D(filters=128, kernel_size=2, padding='same', activation='relu'))
modelo.add(MaxPooling2D(pool_size=2))
modelo.add(Flatten())
modelo.add(Dense(256, activation='relu'))
modelo.add(Dense(train_generator.num_classes, activation='softmax'))
### Acurácia: 0.9399999976158142 #######
#------------------------------------------------------

# QUARTA TENTATIVA
#modelo.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu', input_shape=(224, 224, 3)))
#modelo.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Conv2D(filters=128, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Flatten())
#modelo.add(Dense(256, activation='relu'))
#modelo.add(Dense(train_generator.num_classes, activation='softmax'))
### Acurácia: 0.8399999737739563  #######
#-----------------------------------------------------

# TERCEIRA TENTATIVA
#modelo.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu', input_shape=(224, 224, 3)))
#modelo.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Flatten())
#modelo.add(Dense(128, activation='relu'))
#modelo.add(Dense(train_generator.num_classes, activation='softmax'))
#### Acurácia: 0.800000011920929  #######
#-----------------------------------------------------

# SEGUNDA TENTATIVA
#modelo.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(224, 224, 3)))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Conv2D(filters=128, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Conv2D(filters=256, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Flatten())
#modelo.add(Dense(500, activation='relu'))
#modelo.add(Dense(200, activation='relu'))
#modelo.add(Dense(train_generator.num_classes, activation='softmax'))
#### Acurácia: 0.7200000286102295  #######
#-------------------------------------------------------

# PRIMEIRA TENTATIVA
#modelo.add(Conv2D(filters=16, kernel_size=2, padding='same', activation='relu', input_shape=(224, 224, 3)))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
#modelo.add(MaxPooling2D(pool_size=2))
#modelo.add(Flatten())
#modelo.add(Dense(500, activation='relu'))
#modelo.add(Dense(train_generator.num_classes, activation='softmax'))
#### Acurácia: 0.7000000095367432 #########
#----------------------------------------------------------

#EXIBE INFORMAÇÕES DO MODELO
modelo.summary()

#COMPILA O MODELO
modelo.compile(
optimizer='Adam',
loss='categorical_crossentropy',
metrics=['acc'])

# cria um checkpoint para salvar os pesos do melhor modelo encontrado no trainamento
checkpointer = ModelCheckpoint(filepath='modelo.weights.best.hdf5', verbose=1, save_best_only=True)

#TREINA O MODELO
hist = modelo.fit(train_generator, batch_size=16, epochs=10,
          validation_data=(valid_generator), callbacks=[checkpointer], 
          verbose=1, shuffle=True)

# carrega os pesos do melhor modelo encontrado no treinamento
modelo.load_weights('modelo.weights.best.hdf5')

#RETORNA A ACURÁCIA DO MODELO
score = modelo.evaluate(test_generator, verbose=0)
print('\n', 'Acurácia:', score[1])


#TESTA AS AMOSTRAS DO DIRETÓRIO DE TESTES COM O MODELO TREINADO

#obtem entradas e saídas de teste
x_test, y_test = next(iter(test_generator))
#obtem as prediçoes do modelo pra cada imagem de teste
y_hat = modelo.predict(x_test)
# define os labels (fonte: https://www.cs.toronto.edu/~kriz/cifar.html)
classes = ['ABBOTTS BABBLER', 'AFRICAN FIREFINCH', 'AZURE TIT', 'BARN OWL', 'BLACK BAZA', 
           'BLUE THROATED TOUCANET', 'CHATTERING LORY', 'COMMON IORA', 'CURL CRESTED ARACURI', 'DOUBLE BARRED FINCH'] 
           #CLASSES POSSÍVEIS

# exibe alguns exemplos aleatórios do teste, bem como sua predição e o resultado esperado
fig = plt.figure(figsize=(20, 20))
for i, idx in enumerate(np.random.choice(x_test.shape[0], size=30, replace=False)):
    ax = fig.add_subplot(10, 3, i + 1, xticks=[], yticks=[])
    ax.imshow(np.squeeze(x_test[idx]))
    pred_idx = np.argmax(y_hat[idx])
    true_idx = np.argmax(y_test[idx])
    ax.set_title("{} ({})".format(classes[pred_idx], classes[true_idx]),
                 color=("green" if pred_idx == true_idx else "red"))

# O Modelo apresentou Acurácia de 93,9.
# Das 30 imagens geradas, o modelo classificou 28 imagens corretamente. O que foi bem satisfatório."""
