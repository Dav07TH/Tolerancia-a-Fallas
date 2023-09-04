# Principios de prevención de defectos (Parte 2)
### Introducción:
Leer el siguiente articulo e investiga sobre diferentes métodos para la prevención de defectos.

https://www.ajol.info/index.php/star/article/view/98848/88107

### Desarrollo:
Orthogonal Defect Classification (ODC) es un modelo de prevención y clasificación de defectos utilizado en el desarrollo de software. ODC implica categorizar los defectos en función de varias clasificaciones ortogonales, como el desencadenante del defecto y el tipo de defecto, para identificar características comunes de los defectos que afectan a un proyecto de software en particular. ODC se puede utilizar para medir el progreso del desarrollo con respecto a la calidad del producto e identificar problemas de proceso, lo que puede ayudar a establecer "Mejores Prácticas" que se deben seguir para erradicar los defectos en los proyectos posteriores.

ODC se ha aplicado al desarrollo y las fases de operación de sistemas críticos de seguridad, revelando desafíos en la clasificación adecuada de este tipo específico de problemas con el enfoque más amplio de ODC. Se identifican y sistematizan las dificultades y se proponen propuestas específicas de mejora.

Para abordar el problema de las etiquetas de categoría faltantes para muchos sistemas de software, se ha propuesto una solución de minería de texto que puede categorizar los defectos en varios tipos mediante el análisis tanto de los textos de los informes de errores como de las características del código de las correcciones de errores. Además, un enfoque basado en la clasificación puede clasificar automáticamente los defectos en tres supercategorías que están compuestas por categorías de ODC: flujo de control y datos, estructurales y no funcionales. El enfoque de clasificación automática puede etiquetar defectos con una precisión promedio del 77,8% utilizando el algoritmo de clasificación multiclase SVM.
ODC también se utiliza para la clasificación de informes de errores en el tipo de defecto de ODC utilizando la memoria a corto y largo plazo, una RNN que se utiliza en muchas tareas de clasificación. El método propuesto supera a los enfoques clásicos como los modelos de clasificación basados en bolsa de palabras y TF-IDF.

En un artículo de 2001, ODC se utilizó para categorizar e inferir que resultó en listas de verificación sintetizadas que reflejan la última experiencia del proyecto y las reglas más frecuentemente incumplidas durante el desarrollo de software. Luego se desarrollaron técnicas que utilizaron automáticamente las listas de verificación para buscar defectos en el código fuente. Esta técnica automatizada de detección de defectos libera recursos que se pueden utilizar para buscar problemas específicos del proyecto.

A continuación, se presenta cómo trabaja ODC:
1. Clasificación de defectos: ODC se basa en la idea de que los defectos de software pueden clasificarse en categorías específicas según su naturaleza y gravedad. Estas categorías son predefinidas y se conocen como "categorías ortogonales". Las categorías ortogonales son mutuamente excluyentes y exhaustivas, lo que significa que cada defecto puede asignarse a una sola categoría.
2. Categorías ortogonales: Las categorías ortogonales son un conjunto de categorías que cubren todas las posibles causas de defectos en el software. Estas categorías pueden variar según la organización, pero algunas categorías comunes incluyen:
  + Requisitos: Defectos relacionados con problemas en la comprensión, documentación o definición de los requisitos del software.
  + Diseño: Defectos relacionados con errores en el diseño de la arquitectura o la interfaz del software.
  + Código: Defectos que se encuentran en el código fuente, como errores de sintaxis, lógica incorrecta o mal uso de variables.
  +  Pruebas: Defectos relacionados con la calidad de las pruebas, como casos de prueba insuficientes o mal diseñados.
  + Documentación: Defectos relacionados con errores en la documentación del software, como manuales mal escritos o documentación desactualizada.
  + Defectos de interfaz: Defectos relacionados con la interacción del software con otros sistemas o componentes.
  + Defectos de rendimiento: Defectos relacionados con problemas de rendimiento, como la lentitud del software o el uso ineficiente de recursos.
  + Defectos de seguridad: Defectos que pueden conducir a vulnerabilidades de seguridad en el software.

3. Registro y seguimiento: Cada vez que se encuentra un defecto en el proceso de desarrollo o pruebas, se registra y se clasifica en una de las categorías ortogonales. Además, se asigna una gravedad o prioridad para determinar cuán crítico es el defecto.
4. Análisis y toma de decisiones: Una vez que se han registrado y clasificado los defectos, ODC permite realizar análisis y generar informes para identificar patrones y tendencias. Esto ayuda a la alta dirección y al equipo de desarrollo a tomar decisiones informadas sobre cómo asignar recursos para corregir los defectos. Por ejemplo, si se observa que la mayoría de los defectos se encuentran en la categoría de "Código", la organización podría decidir enfocar sus esfuerzos en mejorar las prácticas de codificación.
5. Mejora continua: ODC promueve la mejora continua de la calidad del software al proporcionar datos objetivos sobre la frecuencia y la naturaleza de los defectos. Esto permite que las organizaciones identifiquen áreas problemáticas y tomen medidas para prevenir defectos similares en el futuro.

En resumen, Orthogonal Defect Classification (ODC) es una metodología que se utiliza para clasificar y analizar los defectos de software de manera sistemática. Ayuda a las organizaciones a comprender mejor la naturaleza de los defectos, tomar decisiones informadas y mejorar continuamente la calidad del software que desarrollan.
