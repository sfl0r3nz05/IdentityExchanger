# Estado de la Técnica

Con el objetivo de proteger a los usuarios de las amenazas anteriormente mencionadas en la actualidad se llevan a cabos numerosos esfuerzos. Por su trascendencia, los sistemas de verificación de edad se convierten en una necesidad en aras, por ejemplo, de garantiza la protección del interés superior del menor, a partir de principios, derechos y obligaciones establecidos en el GDPR. En ese sentido la Agencia Española de Protección de Datos (AEPD), ha diseñado una prueba de concepto (PoC) para adoptar un procedimiento de verificación de edad que permita limitar el acceso a contenidos inadecuados para personas menores [1]. El objetivo último de este sistema es que cumpla escrupulosamente con la normativa de protección de datos dado el alto riesgo que supone el gran impacto sobre los derechos fundamentales. 

Desde una perspectiva más científica el artículo de S. Hammann et al. [2] discute las limitaciones de OpenID Connect en términos de privacidad y presenta dos extensiones, Privacy-Preserving OpenID Connect (POIDC) y Pairwise POIDC, que abordan estas dichas limitaciones. La extensión POIDC reemplaza el client_id con un seudónimo único para el RP y permite al usuario dar consentimiento para iniciar sesión en un RP específico sin que el IdP conozca la identidad del RP. Pairwise POIDC va un paso más allá al introducir identificadores únicos para cada RP, ocultando la asociación entre las cuentas de los usuarios en diferentes RPs. Ambas extensiones garantizan la misma seguridad que OpenID Connect estándar. El artículo incluye sendas demostraciones de implementación del algoritmo propuesto [3]. 

Desde la perspectiva de innovación existen patentes que buscan garantizar la privacidad de los usuarios desde la perspectiva de la descentralización de la identidad. Así, por ejemplo, T. J. Ronda et al. [4] han propuesto un intermediario de autenticación de confianza el cual pueda autenticar al usuario con diferentes RPs sin necesidad de utilizar ningún intermediario que centralice o federe información relacionada con el poseedor de la identidad digital. 

Desde la perspectiva de evaluación se encuentran modelos como las Evaluaciones del Impacto sobre la Privacidad (PIA, del inglés Privacy Impact Assessments) el cual es fundamental para evaluar las actividades de privacidad de una organización y mitigar los riesgos de la manera más eficaz posible. El modelo PIA no sólo es útil, sino que puede llegar a ser obligatoria para el cumplimiento de la normativa sobre privacidad. Adicionalmente, el modelo PIA aplicado al ámbito de la protección de datos (DPIA, del inglés Data Protection Impact Assessment) es un requisito previsto en un número cada vez más leyes de protección de datos cuando se introducen nuevos procesos, sistemas o tecnologías de tratamiento de datos [5]. Por ejemplo, el artículo 35 del GDPR, indica como previo al tratamiento de los datos el responsable de este deberá llevar a cabo una evaluación del impacto de dicho tratamiento.

## References

1. https://www.aepd.es/guias/nota-pruebas-concepto-verificacion-edad.pdf 
2. https://people.inf.ethz.ch/rsasse/pub/poidc-asiaccs20.pdf
3. https://github.com/tamarin-prover/tamarin-prover/tree/develop/examples/asiaccs20-POIDC
4. https://patentimages.storage.googleapis.com/9a/b7/ac/408320daf9d7fb/US10237259.pdf
5. OneTrust, The ultimate PIA and DPIA handbook for privacy professionals. December 2022