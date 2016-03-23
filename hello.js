//wspr auto
var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';

page.onConsoleMessage = function(msg) {
  console.log('Log  message >> ' + msg);
};
page.open('http://49.207.178.71:443', function(status) {
  page.evaluate(function() {
    console.log(document.title);
	document.usernameform.username.value='ris|';
	setfreqif(7038.6); 
	setmf('usb',  0.3,  2.7);
	var slider = document.getElementById('volumecontrol2')
	slider.value= 4; // range is -20 to 6
	console.log(document.usernameform.username.value);
	//start
	//var sTime = new Date().getTime();
	//var countDown = 30;
	//function UpdateTime() {
    //var cTime = new Date().getTime();
    //var diff = cTime - sTime;
    //var seconds = countDown - Math.floor(diff / 1000);
    //show seconds
	//console.log(seconds);
	//}
    //UpdateTime();
    //var counter = setInterval(UpdateTime, 500);
	//end 
	
	//BEGIN AUDIO RECORD
	
	//end 
	
  });
 
var cookies = page.cookies;

console.log('Listing cookies:');
  for(var i in cookies) {
    console.log(cookies[i].name + '=' + cookies[i].value);
  } 
  //phantom.exit();
});




