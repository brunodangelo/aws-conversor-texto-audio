# aws-conversor-texto-audio
Aplicación serverless utilizada para convertir texto a audio, empleando los servicios S3, Lambda (Python) y Polly de AWS.

**EXPLICACION DETALLADA PASO A PASO:** https://todotelco.com/proyecto-aws-aplicacion-serverless-para-convertir-texto-a-audio-utilizando-s3-lambda-polly-y-python


**Paso 1:** Crear los Buckets de destino y origen

**Paso 2:** Crear Politica IAM
-Asociar las acciones: GetObject y PutObject para el servicio de S3 (asignando a los buckets creados en el primer paso). Y para Polly asociar la accion SynthesizeSpeech.

**Paso 3:** Crear Rol IAM
-A la politica creada en el paso anterior, asignarla al un nuevo rol (el servicio que la utiliza es Lambda).

**Paso 4:** Creacion de la Función Lambda
-El lenguage utilizado es Python y se le debe asignar el rol creado en el paso 3.
-Tambien crear 2 variables de entorno para los nombres de los buckets (BUCKET_ORIGEN y BUCKET_DESTINO).
-Luego pegar el codigo "conversor.py" dentro de la función Lambda creada y Deploy.
-Finalmente crear un Evento "desencadenador" o trigger (asociandolo al bucket origen S3), para ejecutar la función cuando se sube un archivo .txt.

**Paso 5:** Probar la aplicación

**EXPLICACION DETALLADA PASO A PASO:** https://todotelco.com/proyecto-aws-aplicacion-serverless-para-convertir-texto-a-audio-utilizando-s3-lambda-polly-y-python
