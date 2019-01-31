var {PythonShell} = require('python-shell');

var options = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: './',
};

var test =  new PythonShell('CaptureCameraFace.py', options);
test.on('message',function (message) {
    console.log(message);
});
