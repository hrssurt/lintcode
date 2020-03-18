## FINDINGS
	Group all the entries by IP. Treat each group as a session:
		1. The average duration of the sessions is 2663 seconds, which is roughly 44 minutes
		2. The average url counts per session is 9, and the max url count in a session is 26423
		3. The max session has IP 119.81.61.166, with the duration is 66621 seconds, which is roughly 18 hours


## toolkit
Used spark. With all code in main.scala

## command running the code
	spark-shell -i main.scala

notce the file path in the main.scala needs to be changed to point to the right location of the data log.
