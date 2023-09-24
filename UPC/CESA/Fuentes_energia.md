#teoria
# Red de distribución eléctrica
## Normativa
* Comisión Europea
	* Dictan directivas
	* No tienen poder legislativo
	* Compromiso de los paises miembros
* Paises miembros
	* Dictan las leyes o reglamentos
	* Tienen poder legislativo
	* Siguen directivas europeas
* Comités técnicos
	* Dictan normas tecnicas (no son de obligado cumplimiento)
	* Privados: AENOR
	* Públicos: CEN, CENELEC
	* Normas harmonizadas
### Introducir nuevos productos
- Peligrosos
	- Pasar pruebas en laboratorio homologado
	- Presentar "Declaración de Conformidad" con las leyes y reglamentos del pais
	- Marcar los productos con "CE"
- No peligrosos
	- Presentar "Declaración de Conformidad" con las leyes y reglamentos del pais
	- Marcar los productos con "CE"
## Toplogia de la red
![[Diagrama red electrica.png]]
En una red eléctrica podemos distinguir tres partes; 
- la generación de la energía eléctrica (marcada en negro)
- la red de transporte (marcada en azul)
- la red de distribución (marcada en verde).

La generación de energía eléctrica tiene lugar en las centrales eléctricas, que pueden ser: hidráulicas, térmicas (tanto convencionales como nucleares) y basadas en energías renovables (fotovoltaicas, eólicas, …). Proporcionan una tensión alterna trifásica de media tensión (6 kV a 30 kV) mediante turbinas conectadas a generadores trifásicos (Tesla) o bien una tensión continua (es el caso de los parques fotovoltaicos) que se convierte en alterna trifásica mediante convertidores conmutados. Dicha tensión se eleva mediante los transformadores de salida de la central, para ser inyectada en la red de transporte. La frecuencia del sistema de corriente alterna que se genera es fija y está normalizada: 50 Hz en Europa y 60 Hz en gran parte de América.

La red de transporte y distribución está formada por las líneas que llevan la energía a los consumidores finales. El transporte se hace en alta tensión (110 kV, 220 kV, 400 kV, 750 kV en Europa Occidental) para disminuir las pérdidas. La red de alta tensión es geográficamente extensa, va más allá de las fronteras de los países, y es mallada. En los nudos de esta malla se encuentran las subestaciones que reducen las tensiones mediante transformadores. Las líneas de salida a menor tensión forman las redes de distribución en media tensión (de 1 kV a 66 kV), mucho menos malladas y de menor tamaño, en las que se encuentran los centros de transformación en los que la tensión se va reduciendo hasta que finalmente, y conforme el sistema llega hasta los últimos consumidores, se transforman en las redes de baja tensión (230 V y 400 V), que son radiales.

Los consumidores de la energía, también llamados cargas, se conectan a la red en alta tensión (grandes industrias), en media tensión (industrias, distribución a las ciudades) y en baja tensión (pequeñas industrias y consumidores domésticos)
### Trifásica a monofásica
![[Transformacion trifasica a monofasica.png]]
Un centro de transformación transforma, mediante un transformador trifásico, la tensión de la red en media tensión a la de la red en baja tensión. La red trifásica de media tensión se transforma en baja tensión mediante un transformador trifásico. El punto de unión de los secundarios (lado de baja tensión) es el terminal de neutro y los otros terminales las fases R, S y T. A los consumidores domésticos les llega una red monofásica compuesta por: - Una de las fases R, S o T. - El neutro del transformador. Para que las cargas del transformador estén balanceadas (sean iguales para las tres fases), se va distribuyendo cada una de las fases entre las diferentes viviendas. 
En la mayoría de las redes de distribución, como veremos posteriormente, el neutro del transformador se conecta a tierra. La puesta a tierra consiste en la unión eléctrica directa, mediante un conductor o grupo de conductores, de una parte conductora (el neutro en este caso) con un electrodo o grupos de electrodos enterrados en el suelo.
### Esquemas de distribución de baja tension
Los esquemas de distribución en baja tensión se clasifican en función de las conexiones a tierra de la red de distribución (red de alimentación), por un lado, y de las masas de la instalación receptora, por otro. Se designan mediante dos letras, según el tipo. Según el “Reglamento electrotécnico para baja tensión”, existen tres esquemas de distribución: TT, TN y IT. 
- La primera letra indica si el neutro de la red de alimentación está conectado a 
	- tierra (letra “T”) 
	- está aislado de tierra o conectado a ésta a través de una impedancia de valor elevado (letra “I”). 
- La segunda letra indica si las masas de los receptores (partes conductoras, que pueden ser accesibles por los usuarios) están conectadas 
	- a tierra (letra “T”) (mediante el conductor de protección, CP) 
	- al neutro de la red de alimentación (letra “N”).

Los esquemas de distribución no se pueden normalmente elegir por el usuario y además pueden diferir según países. Los esquemas más empleados son el TT y el TN; algunos países, principalmente 
- Noruega, utilizan el régimen IT. 
- Los países anglosajones (por ejemplo Alemania y Gran Bretaña) utilizan sobre todo el esquema TN
- resto del mundo, entre ellos España y Francia, emplean el esquema TT. 

No obstante, en aplicaciones comerciales e industriales, se puede utilizar un esquema propio (por ejemplo un esquema IT) si su conexión a la red se hace a través de un transformador de distribución propio. Como veremos posteriormente, los sistemas de protección contra choques eléctricos (en personas) van ligados a los esquemas de distribución.

## Seguridad eléctrica
### Problemas de seguridad en la red eléctrica
- Instalaciones y equipos
	- Sobreintensidades
	- Sobretensiones
- Choque eléctrico (usuario)