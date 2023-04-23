import websockets
import asyncio
import base64
import json
import pyaudio
import os
from pathlib import Path

# Audio parameters 
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

# Open an audio stream with above parameter settings
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

# Send audio (Input) / Receive transcription (Output)
async def send_receive():
	URL = f"wss://api.assemblyai.com/v2/realtime/ws?sample_rate={RATE}"

	print(f'Connecting websocket to url ${URL}')

	async with websockets.connect(
		URL,
		extra_headers=(("Authorization", "YOUR_API_KEY_HERE"),),
		ping_interval=5,
		ping_timeout=20
	) as _ws:

		r = await asyncio.sleep(0.1)
		print("Receiving messages ...")

		session_begins = await _ws.recv()
		print(session_begins)
		print("Sending messages ...")


		async def send():
			while True:
				try:
					data = stream.read(FRAMES_PER_BUFFER)
					data = base64.b64encode(data).decode("utf-8")
					json_data = json.dumps({"audio_data":str(data)})
					r = await _ws.send(json_data)

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					print(e)
					assert False, "Not a websocket 4008 error"

				r = await asyncio.sleep(0.01)


		async def receive():
			while True:
				try:
					result_str = await _ws.recv()
					result = json.loads(result_str)['text']

					if json.loads(result_str)['message_type']=='FinalTranscript':
						print(result)

						transcription_txt = open('transcription.txt', 'a')
						transcription_txt.write(result)
						transcription_txt.write(' ')
						transcription_txt.close()


				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					print(e)
					assert False, "Not a websocket 4008 error"
			
		send_result, receive_result = await asyncio.gather(send(), receive())


asyncio.run(send_receive())

if Path('transcription.txt').is_file():
	print('Transcription file created successfully.')
	os.remove('transcription.txt')
