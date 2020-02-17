from flask import Flask

import calc_cesd as csd
import transcript_extract as trans
import comment_extract as ce


app = Flask(__name__)

@app.route("/calculate_score")

def calcCESD():
	# transcript = trans.getTranscripts("Zr16eHb4YNU")
	ce.get_comments("https://www.youtube.com/watch?v=GBexfwe-9j0")
	score = csd.score()

	print(score)

	return "score"
    

if __name__ == "__main__":
	app.run(port = 6788, debug = True)