import time
from ISStreamer.Streamer import streamer

streamer = Streamer(bucket_name="Python Streamer", bucket_key="001", access_key="RRMP1DarpoG7JYkZlhUTIeDPrOmoXe8P")

streamer.log("My Messages", "Stream Starting")

for num in range(1, 20):
	time.sleep(0.1)
	streamer.log("My Numbers", num)

	if (num%2 == 0):
		streamer.log("My Booleans", "false")
	else:
		streamer.log("My Booleans", "true")
	
	if num%3 == 0:
		streamer.log("My Events", "pop")
	
	if num%10 == 0:
		streamer.log("My Messages", "Stream Half Done")

streamer.log("My Messages", "Stream Done")
