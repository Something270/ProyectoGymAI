# ProyectoGymAI
## Main
En esta seccion mandamos a llamar el rom y creamos el ambiente en donde el agente aprendera a jugar, podemos tambien declarar un puntaje maximo de 21 cada episodio.

En la previsualizacion podemos ver el resumen de cada episodio y a la vez mandamos a llamar un nuevo episodio cada vez que hay un GAME OVER.


![capturaMAIN](https://user-images.githubusercontent.com/55809521/144763782-f3d5367a-5bf1-42fd-ac38-875d698984f8.PNG)


## Agente
El agente o modelo se encarga de entrenar y aprender a jugar el juego PONG utilizando un red nueronal convulucional. 

El agente realiza acciones random y regresa aquellos acciones que brindan una recompensa para el agente en otras palabras cualquier accion que no causen un GAME OVER.

![CaptureAGENTE](https://user-images.githubusercontent.com/55809521/144765572-8043b396-c173-4e4c-8ccd-1134ebfe3d3e.PNG)


## Agente Memoria
Esta seccion cuenta con las listas en donde se guardaran la experiencias y una funcion para agregar a estas listas

init: Creamos los variables que buscaremos guardar en la memoria.

add_experience: Guardamos las experiencias de cada episodio en la memoria del agente.

![CaptureAGENTEMEM](https://user-images.githubusercontent.com/55809521/144765574-db9bfce0-5445-44f6-9ee3-fc57cfadce57.PNG)


## Debug
Aqui podemos visualizar el agente entrenado, llamando la memoria del agente y el enviroment.

![CaptureDEBUG](https://user-images.githubusercontent.com/55809521/144765575-cd06fdef-70cc-4c21-8423-e6dd61b873fa.PNG)


## Enviroment
Creamos el entorno en donde el agente va a aprender, para evitar que el agente cargue datos de episodios anteriores iniciamos cada juego con data vacios.

Despues de crear el entorno se iran actualizando los timesteps y los pesos periodicamente agregando todo a la memoria con "add_experience".

![CaptureENVIRO](https://user-images.githubusercontent.com/55809521/144765576-9a570f17-2a58-4e92-b97a-974766e39a00.PNG)


## Processar Frames
Para apoyar el agente en el aprendizaje tenemos que procesar la imagen del emulador para que pueda identifacar la bolita y el barras, tambien eliminando espacios y bajando la resolucion y cambiando la imagen a escalas de grises.

Con estos cambios el agente podra aprender sin problemas.

![CaptureFRAMEPROC](https://user-images.githubusercontent.com/55809521/144765579-fe73fbdd-bc87-4799-8c1e-c34af70d72ca.PNG)


## Video
Y aqui podemos ver el agente con 50 episodios de experiencia.

https://user-images.githubusercontent.com/55809521/144765618-bad4d774-61da-49ad-a0bc-9151f05c6f28.mp4
