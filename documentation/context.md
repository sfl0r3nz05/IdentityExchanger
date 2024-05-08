# Contexto

Los abusos entorno a la identidad digital crecen y evolucionan año con año. Según el informe anual de robos de identidad y fraude generado por el centro de investigación sobre robos de identidades (ITRC [1], por sus siglas en inglés) en 2023 hubo un incremento del número de personas impactadas como se viene dando año con año. A esto debe sumarse la propagación de la desinformación gracias a la capacidad de los de crear cuentas falsas en las redes sociales con facilidad [2]. La sofisticación de los bots sociales y sus patrones se han desarrollado lo suficiente como para emular el comportamiento humano y la posibilidad de eliminar la cuenta de un usuario real, algo que la mayoría de las plataformas de redes sociales quieren evitar.

Aunque el cibercrimen representa una amenaza no es la única existente para la identidad digital. La federación de identidad permite a los proveedores de servicios de identidad (IdP, por sus siglas en inglés) mantener las credenciales de usuario en nombre de varias partes interesadas (RP, por sus siglas en inglés).  Esto proporciona a los usuarios la funcionalidad de inicio de sesión único, en la que una cuenta puede utilizarse para iniciar sesión en muchos servicios diferentes [3]. Para este proceso de autenticación delegada, el protocolo más utilizado en la actualidad es OpenID Connect [4], soportado por proveedores de identidad como Google y Microsoft. El inconveniente de OpenID Connect es que el proveedor de identidad sabe exactamente a qué RP accede un usuario, cuándo y con qué frecuencia. Esta aproximación afecta la privacidad del usuario poseedor de la identidad digital tanto desde el punto de vista de la revelación de la información sensible como desde el punto de vista del perfilado del usuario conteniendo atributos personales verificados de este.

Otra amenaza representativa a la identidad digital y específicamente a la privacidad lo representan las cookies. Por definición, estas presentan un papel esencial para la prestación de numerosos servicios de la sociedad de la información que concentran la mayor inversión publicitaria facilitando la navegación del usuario y ofreciendo una publicidad basada en los hábitos de navegación. Sin embargo, el uso de cookies de terceros representa un tipo de seguimiento que puede resultar intrusivo, siendo enviadas al equipo terminal del usuario desde un equipo o dominio que no es gestionado por el editor, sino por otra entidad que trata los datos obtenidos a través de las cookies.

Con intensión de proteger cada vez más a los usuarios, los gobiernos e instituciones públicas están llevando a cabo un endurecimiento del marco normativo. La Ley General de Protección de Datos (GDPR [5], por sus siglas en inglés) impone directrices estrictas sobre protección de datos y privacidad a personas y organizaciones dentro de la UE y en el espacio económico europeo. Por su parte, el Reglamento (UE) 2022/2065 del Parlamento Europeo (DSA [6], por sus siglas en inglés) relativo a un mercado único de servicios digitales, apoya los métodos eficaces de verificación de la edad con carácter prioritario. A nivel nacional, el artículo 22 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI) y la Ley Orgánica 3/2018, de Protección de Datos y garantía de los derechos digitales (LOPDGDD) establecen exigencias regulatorias para la protección de datos personales, en particular en relación con las categorías especiales de datos. Por su parte, Ley General de Comunicación Audiovisual de 2022 [7] exige, como medidas para la protección de personas menores de edad frente a determinados contenidos audiovisuales.


## References

1. https://www.idtheftcenter.org/ 
2. https://www.cnn.com/2022/10/10/tech/elon-musk-twitter-bot-analysis-cyabra 
3. https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01142020.pdf 
4. Nat Sakimura, John Bradley, Mike Jones, Breno de Medeiros, and Chuck Mortimore. OpenID Connect Core 1.0 incorporating errata set 1. 2014.
5. https://gdpr-info.eu/ 
6. https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R2065
7. Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual

