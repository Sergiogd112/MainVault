#lab
El protocol [[IGMP]] permet que un host expressi el seu interès per a unir-se a un determinat grup multicast o per abandonar-lo. En particular, el host ha d’informar del seu interès per formar part d’un grup o abandonar-lo al router que té connectat directament (el first-hop router).  
Malgrat el seu nom (protocol de gestió de grups), l’[[IGMP]] opera a nivell local, és a dir, entre un host i un router que té directament connectat. (Per tal de coordinar els routers amb l’objectiu de crear l’arbre de distribució [[Mutlicast]], es necessita un protocol d’encaminament multicast, com el PIM-SM).  
Actualment existeixen 3 versions del protocol IGMP, essent la segona versió ([[IGMP]]v2) la més utilitzada.

# Encaminament [[Multicast]] ( forwarding )

En el model unicast, cada router pren decisions d’encaminament en base a l’adreça IP destí del paquet, mirant la taula  
d’encaminament unicast i enviant el paquet cap al next-hop. En el model multicast hi ha diferents mecanismes que  
permeten decidir per quina interfície s’ha d’enviar un paquet.

# Protocols d’encaminament [[Multicast]]

Els protocols d’encaminament multicast permeten crear els arbres de distribució multicast, de manera que els receptors que s’han unit a un determinat grup multicast, puguin rebre el trànsit dirigit a aquest grup. Els protocols que existeixen avui en dia es poden classificar en tres categories:  
- **Mode dens (dens mode): DVRMPv3, PIM-DM.**  
Els protocols en mode dens utilitzen exclusivament arbres de font (SPT) utilitzant el principi de push. Aquest   principi assumeix que hi ha receptors a tots els punts de la xarxa i per tant, inicialment s’inunda tota la xarxa   amb trànsit multicast. A partir d’aquí es van podant les branques innecessàries. Periòdicament es repeteix la  inundació de la xarxa per si hi ha nous receptors interessats en rebre trànsit destinat a un grup particular.  Aquest procés seria anàleg a la transmissió de ràdio o TV; els receptors només han de sintonitzar la  freqüència corresponent per començar a sentir l’emissora o veure el canal de TV.  
- **Mode dispers (sparse mode): PIM-SM, CBT**  
Aquest tipus de protocols utilitzen arbres compartits i en alguns casos, com en el PIM-SM, s’utilitzen arbres  de font per distribuir el trànsit multicast. Enlloc d’utilitzar el model de push, utilitzen el model de pull, el qual  assumeix que els receptors no volen rebre el trànsit multicast a menys que el sol·licitin expressament. Seguint amb l’analogia anterior, aquest model seria equivalent a un servei sota demanda (vídeo o àudio), on només  s’envia el flux a aquells usuaris que ho han sol·licitat.  
- **Protocols d’estat d’enllaç (link-state protocols): MOSPF**  
Els protocols d’estat d’enllaç funcionen d’una forma similar als protocols en mode dens en el sentit que tots  dos utilitzen arbres de font per distribuir el trànsit multicast. Tot i així, no utilitzen la tècnica de flood and prune  sinó que els routers envien informació d’estat d’enllaç per identificar els membres d’un determinat grup  multicast.
# Comandes
l

