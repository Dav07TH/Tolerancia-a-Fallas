# Ejercicio 01 Conceptos básicos.
> Alumno: David Torres Hernández
  Codigo: 215428899
  Ciclo: 2023B
  Carrera: INCO
  Seccio: D06
  Profesor: Michel Emanuel Lopéz Franco

###### Objetivos:
Conocer los conceptos básicos en sistemas tolerantes a fallas.

###### Desarrollo:
Contesta las siguientes preguntas:
### ¿Qué son los sistemas tolerantes a fallos?
Los sistemas tolerantes a fallos son aquellos que tienen la capacidad de seguir funcionando correctamente incluso después de que uno o varios de sus componentes hayan fallado.
Estos sistemas están diseñados para prevenir interrupciones que puedan surgir de un solo punto de falla, asegurando la alta disponibilidad y la continuidad de las aplicaciones o sistemas de misión crítica.

Algunas características y técnicas asociadas a los sistemas tolerantes a fallos son:
Replicación: Consiste en proporcionar múltiples casos idénticos en el mismo sistema o subsistema, dirigiendo las tareas o solicitudes a todos ellos en paralelo y eligiendo el resultado correcto.

Componentes de respaldo: Los sistemas tolerantes a fallos utilizan componentes de respaldo que automáticamente toman el lugar de los componentes fallados, asegurando que no se pierda el servicio.
Redundancia: La redundancia es una técnica comúnmente utilizada en los sistemas tolerantes a fallos. Sin embargo, es importante tener en cuenta que la redundancia puede tener algunas penalizaciones, como el aumento de peso, tamaño, consumo de energía y costo, así como el tiempo necesario para diseñar, verificar y probar.
Alta disponibilidad: Los sistemas tolerantes a fallos buscan garantizar la alta disponibilidad de las aplicaciones o sistemas, lo que implica que puedan seguir funcionando sin interrupción incluso en caso de fallos.

La tolerancia a fallos puede lograrse tanto a través de enfoques basados en software como en hardware. En el caso de un fallo del sistema primario, un sistema secundario de respaldo asume el control desde el momento exacto en que el sistema primario falla, evitando así la duplicación o interrupción del servicio.
### ¿Qué es un fallo?
Un fallo es un estado o situación en la que un sistema formado por dispositivos, equipos, aparatos y/o personas deja de cumplir la función para la cual había sido diseñado.
En ingeniería, se considera que todos los sistemas llegarán a un instante en el que no cumplirán satisfactoriamente aquel producto o aquella función para la cual fueron diseñados, con lo cual, fallarán. Los fallos pueden ser clasificados por su origen, y pueden ser puntuales o pueden conllevar un efecto dominó en el transcurso del proceso, siendo este último el tipo de fallo más peligroso.

En el contexto de la tolerancia a fallos, un fallo se refiere a la situación en la que entra en juego el sistema de respaldo o redundancia para garantizar la continuidad del servicio.
### ¿Qué es un Bug?
Un bug, en el contexto de la informática y la programación, se refiere a un error o defecto en el código de un programa informático. También se puede considerar como un fallo o una anomalía en el funcionamiento de un sistema o software. Los bugs pueden ser causados por errores en la lógica del programador, problemas de diseño, problemas de interoperabilidad o cualquier otro factor que conduzca a un comportamiento inesperado o incorrecto del programa.

Los bugs pueden manifestarse de diferentes maneras y tener diferentes grados de gravedad. Algunos bugs pueden ser menores y tener un impacto mínimo en el funcionamiento del programa, como errores estéticos o tipográficos. Otros bugs pueden ser más graves y provocar que el programa se bloquee, se comporte de manera incorrecta o incluso cause daños en el sistema.

Es importante destacar que los bugs son comunes en el desarrollo de software y, por lo tanto, se lleva a cabo un proceso de depuración o debugging para identificar y corregir estos errores antes de que los usuarios finales los encuentren. Los desarrolladores utilizan técnicas de prueba y depuración para encontrar y solucionar los bugs, lo que ayuda a mejorar la calidad y la estabilidad del software.

### ¿Qué es un error?
En el contexto del software, un error es una acción humana que produce un resultado incorrecto, una idea equivocada de algo. Es decir, un error es una equivocación de parte del desarrollador o del analista. Un error puede ser reproducible o no reproducible, conocido o no conocido. Un ejemplo de error en programación puede ser un error en la lógica de la programación o un requerimiento que esté mal especificado.

Es importante destacar que en el área del aseguramiento de la calidad del software, se utilizan los términos error, defecto y falla para describir diferentes situaciones. Un error es una acción humana que produce un resultado incorrecto, mientras que un defecto es la manifestación de ese error en el código. Por otro lado, una falla es la manifestación del defecto al usar el sistema.
En resumen, un error es una acción humana que produce un resultado incorrecto, mientras que un defecto y una falla son términos que se utilizan en el contexto del software para describir situaciones específicas.

### ¿Qué es la latencia de un fallo?
La latencia de un fallo se refiere al tiempo que transcurre desde que se produce un fallo hasta que se manifiesta el error. En otras palabras, es el tiempo que tarda un sistema en detectar un fallo y en tomar medidas para corregirlo. La latencia de un error, por otro lado, se refiere al tiempo que transcurre desde que se produce un error hasta que se detecta.

Es importante tener en cuenta que la latencia de un fallo puede tener un impacto significativo en la calidad del servicio y en la experiencia del usuario. En el contexto de la tolerancia a fallos, la latencia es un factor importante a considerar, ya que un sistema tolerante a fallos debe ser capaz de detectar y corregir los fallos de manera rápida y eficiente para garantizar la continuidad del servicio.

### ¿Qué es la latencia de un error?
La latencia de un error se refiere al tiempo que transcurre desde que se produce un error hasta que se detecta. Es decir, es el tiempo que tarda un sistema en identificar que se ha producido un error. La latencia de un error es un factor importante a considerar en el aseguramiento de la calidad del software, ya que cuanto menor sea la latencia, más rápido se podrán corregir los errores y mejorar la calidad del software. Es importante tener en cuenta que la latencia de un error puede tener un impacto significativo en la experiencia del usuario y en la calidad del servicio.

##### Conclucion:
En el contexto de la informática y la programación, se utilizan diferentes términos para describir situaciones específicas. Un error es una acción humana que produce un resultado incorrecto, mientras que un defecto es la manifestación de ese error en el código y una falla es la manifestación del defecto al usar el sistema. Por otro lado, un bug se refiere a un error o defecto en el código de un programa informático que puede provocar un comportamiento inesperado o incorrecto del sistema. La latencia de un fallo se refiere al tiempo que transcurre desde que se produce un fallo hasta que se manifiesta el error, mientras que la latencia de un error se refiere al tiempo que transcurre desde que se produce un error hasta que se detecta. Es importante tener en cuenta estos términos y conceptos en el desarrollo de software y en el aseguramiento de la calidad del mismo.
##### Bibliografias:

- "Referencias bibliográficas: indicadores para su evaluación en trabajos científicos" (http://www.scielo.org.mx/scielo.php?pid=S0187-358X2017000100151&script=sci_arttext)
- "Cómo Preparar una Bibliografía Anotada - LibGuides at Cornell University" (https://guides.library.cornell.edu/bibliografia_anotada)
- "APA, MLA, Chicago: dar formato a bibliografías automáticamente - Microsoft Support" (https://support.microsoft.com/es-es/office/apa-mla-chicago-dar-formato-a-bibliograf%C3%ADas-autom%C3%A1ticamente-405c207c-7070-42fa-91e7-eaf064b14dbb)
- "INVESTIGACIÓN CIENTÍFICA - UNM Digital Repository" (https://digitalrepository.unm.edu/cgi/viewcontent.cgi?article=1356&context=abya_yala)
- "Estrategias de lectura en lectores expertos para la producción de textos académicos" (https://www.tdx.cat/bitstream/handle/10803/4759/mzg1de1.pdf)
- "Modelos de estudios en investigación aplicada: conceptos y criterios para el diseño" (https://scielo.isciii.es/pdf/mesetra/v54n210/aula.pdf)
