#teoria 
| Tipus missatge IGMP        | Enviat per | Adreça IP destí       | Objectiu                                                                 |
| -------------------------- | ---------- | --------------------- | ------------------------------------------------------------------------ |
| Membership Report          | Host       | Adreça grup multicast | Informa que es vol unir a un grup [[Mutlicast]]                              |
| Membership query: general  | Router     | 224.0.0.1             | Pregunta pels grups multicast als quals s’han unit els hosts de la xarxa |
| Membership query: specific | Router     | 224.0.0.1             | Pregunta si algun host s’ha unit a un grup [[Mutlicast]] en particular       |
| Leave Group                | Host       | 224.0.0.2             | Informa que vol abandonar un grup [[Mutlicast]]|
