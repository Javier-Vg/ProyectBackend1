Clases:

1: Tablero:
-Establece todos los procesos del cambio de tablero y verificaciones de gane.
-Divide los procesos de cada rol en sus respectivos metodos unicos.
-Valida los datos.
-Se muetra el tablero que esta en juego.
-Se elige la palabra a adivinar.

2: Palabras:
-Es la responsable de retornar palabras al azar, ya sea para adivinar o para que la maquina las use para adivinar.
-Se usa un archivo con formato .txt para capturar las palabras.

3: Roles:
-Divide y inicia el juego.
-Realiza procesos iniciales del juego, como llamar a las demas clases, aplicando composicion.
-Crea el tablero inicial.

4: Retroalimentacion:
-Hereda de la clase abstracta "Intentos".
-Verifica las posiciones erroneas, correctas y inexistentes dentro de la palabra.
-Verifica la cantidad de intentos, si debe de seguir el juego o no.

5: Intentos:
-Contiene un metodo abstracto, que son los intentos.
-Es heredada a la clase "Retroalimentacion".

Funciones:

1: main:
-Se usa para escoger el rol del juego.
-Es un bucle que deja de enciclarse cada que el usuario pida que se frene el programa.