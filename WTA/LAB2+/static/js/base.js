window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("main-title").style.fontSize = "20px";
    document.getElementById("logo").style.fontSize = "25px";
  } else {
    document.getElementById("top-bar").style.fontSize = "50px";
    document.getElementById("logo").style.fontSize = "35px";
  }
}

// incomplete, not working^


var fb = document.getElementById("fb");
var but = document.getElementById("btn");

but.onclick = function () {
	fb.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == fb) {
    fb.style.display = "none";
  }
}