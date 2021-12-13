var sim;

var context;

function Player() {
	this.BUFFER_SIZE = 2048;

	context = new (window.AudioContext || window.webkitAudioContext)();

	this.loadFile = function(f) {
		var request = new XMLHttpRequest();
		request.open("GET", f, true);
		request.responseType = "arraybuffer";
		var loader = this;
		request.onload = function() {
			// Asynchronously decode the audio file data in request.response
			var audioData = request.response;

			context.decodeAudioData(audioData, function(buffer) {
				sim.gotAudioData(buffer.getChannelData(0));
			},

			function(e){ console.log("Error with decoding audio data" + e.err); });
		}
		request.send();
	}
};

// install callbacks for GWT
document.passSimulator = function passSimulator (sim_) {
	sim = sim_;
	player = new Player();
	sim.loadAudioFile = function(f) { player.stop(); player.loadFile(f); }
};

