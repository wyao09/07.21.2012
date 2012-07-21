var express = require('express');

var app = express.createServer(express.logger());

app.use(express.static(__dirname + '/public'));

app.get('/', function(request, response) {
  response.send('Hello World!');
});

app.get('/timestamp', function(request, response){
    response.contentType('application/json');

    var clientTimestamp = request.param('t');
    var diff = (Date.now()) - clientTimestamp;

    response.send(String(diff));
});

var port = process.env.PORT || 5000;
app.listen(port, function() {
  console.log("Listening on " + port);
});