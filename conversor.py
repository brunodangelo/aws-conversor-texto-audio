import boto3
import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
	# Inicializamos S3 y Polly
	s3 = boto3.client(‘s3’)
	polly = boto3.client(‘polly’)

	# Obtenemos los buckets desde las variables de entorno
	bucket_origen = os.environ[‘BUCKET_ORIGEN’]
	bucket_destino = os.environ[‘BUCKET_DESTINO’]

	# Evento en Lambda
	text_file_key = event[‘Records’][0][‘s3’][‘object’][‘key’]
	audio_key = text_file_key.replace(‘.txt’, ‘.mp3’)

	try:
		# Recupera el texto desde el bucket origen
		logger.info(f”Obteniendo el texto desde: {bucket_origen}, key: {text_file_key}”)
		text_file = s3.get_object(Bucket=bucket_origen, Key=text_file_key)
		text = text_file[‘Body’].read().decode(‘utf-8’)

		# Envio del texto a Polly
		logger.info(f”Enviando el texto a Polly”)
		response = polly.synthesize_speech(
			Text=text,
			OutputFormat=’mp3′,
			VoiceId=’Lucia’ # voz personalizada
		)

		# El audio se guarda en el bucket de destino
		if ‘AudioStream’ in response:
			temp_audio_path = ‘/tmp/audio.mp3’
			with open(temp_audio_path, ‘wb’) as file:
			file.write(response[‘AudioStream’].read())

			logger.info(f”Subiendo el audio en: {bucket_destino}, key: {audio_key}”)
			s3.upload_file(temp_audio_path, bucket_destino, audio_key)

			logger.info(f”Proceso completado para el archivo: {text_file_key}”)

			return {
				‘statusCode’: 200,
				‘body’: json.dumps(‘Proceso completado con exito!’)
			}

	except Exception as e:
		logger.error(f”Error procesando {text_file_key} desde el bucket {bucket_origen}: {str(e)}”)
		return {
			‘statusCode’: 500,
			‘body’: json.dumps(‘Ocurrió un error en el proceso’)
	}