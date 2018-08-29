# Tarea 1

### Ejercicio 1

Se desea almacenar un conjunto de datos sobre una lista enlazada y se desea soportar búsquedas sobre dicho conjunto de datos. Se sabe que ciertos elementos del conjunto son buscados más frecuentemente que otros, y que la tendencia de búsqueda cambia con el tiempo, en el sentido que los elementos más frecuentemente consultados no necesariamente son los mismos en todo momento. Implemente una lista enlazada para permitir la búsqueda eficiente de los elementos más consultados. También debe soportar la inserción eficiente de nuevos elementos.

### Ejercicio 2

La notación polaca, también conocida como notación de prefijo o notación prefija, es una forma de notación para la lógica, la aritmética, el álgebra y la computación. Su característica distintiva es que coloca los operadores a la izquierda de sus operandos.

La notación polaca inversa es un método algebraico alternativo de introducción de datos. Su nombre viene por analogía con la relacionada notación polaca. En la notación polaca inversa es al revés: primero están los operandos y después viene el operador que va a realizar los cálculos sobre ellos. Tanto la notación polaca como la notación polaca inversa no necesitan usar paréntesis para indicar el orden de las operaciones,

* Ejemplo notación polaca

```
(5 - 6) * 7 <=> * (- 5 6) 7
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) <=> - * / 15 - 7 + 1 1 3 + 2 + 1 1 
```

El orden de operaciones es definido dentro de la estructura. Una cosa a tener presente es que al ejecutar una operación, la operación es aplicada AL primer operando POR el segundo operando.

* Ejemplo notación polaca inversa

```
(5 - 6) * 7 <=> 5 6 - 7 *
5 + (( 1 + 2) * 4) - 3 <=> 5 1 2 + 4 * + 3 -
```

Su tarea consiste en implementar ambos algoritmos utilizando una estructura de datos adecuada.


## Entrega

Fecha límite: Viernes 14 de Septiembre a las 10:00 hrs.

Para la entrega de la tarea deberá utilizar Github. Para esto deberán ingresar en ` https://github.com/EDD-2018-2 ` y seleccionar su repositorio, al hacer click encontrará los comandos con los cuales podrá comenzar a trabajar en su repositorio. Dicho repositorio deberá contener cada uno de los archivos de código en formato `.py` dentro de la carpeta `Tarea 1`.


## Recomendaciones

Haga la tarea con tiempo.

Utilice las pautas vistas en la primera ayudantía para escribir bien su código. 

Utilice un archivo `.py` para cada estructura de manera que se mantenga el código organizado.

## Git

Puede utilizar GitHub a través de:
* [GitHub Desktop](https://services.github.com/on-demand/github-desktop/es/instalar-github-desktop)
* [Terminal](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
* [Página web](https://github.com)

Guía sencilla para aprender Git http://rogerdudler.github.io/git-guide/index.es.html 

Se recomienda realizar un commit para identificar cada uno de los cambios que hace en su código.