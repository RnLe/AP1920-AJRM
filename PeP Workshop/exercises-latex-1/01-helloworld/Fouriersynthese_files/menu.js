( function() {
	"use strict";
	var nav = document.querySelector("#mainnav");
	var allinp = document.querySelectorAll("#mainnav input");
	var inp = document.querySelectorAll("#mainnav li input");
	var smallmenu = document.querySelector("#smallmenu");
	var inPath = function(node,toSearch) {
		var path = [];
		while(node && node != document.body) {
			path.push(node);
			node = node.parentNode;
		}
		return path.indexOf(toSearch) > -1;
	}
	// Alle Submenüs schließen
	var close_all = function(e) { 
		if(!inPath(e.target,nav)) {
			for(var j=0;j<inp.length;j++) inp[j].checked = false; 
			smallmenu.checked = false;
		}
	}
	// Menü auch bei Enter öffnen
	for(var i=0;i<allinp.length;i++) {
		allinp[i].addEventListener("keydown",function(e) { 
			if(e.keyCode == 13) this.checked = !this.checked; 
			if(this.checked) 
				for(var j=0;j<inp.length;j++) 
					if(this != inp[j]) 
						inp[j].checked = false; 				
		});
	}
	// nur maximal ein Submenü offen
	for(var i=0;i<inp.length;i++) {
		inp[i].addEventListener("change",function(e) {
			if(this.checked) 
				for(var j=0;j<inp.length;j++) 
					if(this != inp[j]) 
						inp[j].checked = false; 				
		});
	}
	// Menüzeile raus/rein-scrollen
	var last_pos = 0;
	var pos = 0;
	var scroll_nav = function() {  
		if(window.scrollY) pos = window.scrollY;
		else if(document.documentElement.scrollTop) pos = document.documentElement.scrollTop; // IE
		var delta = pos - last_pos;
		if(delta>0) nav.style.top = Math.max(nav.offsetTop-Math.ceil(delta*2),-(nav.offsetHeight-5)) + "px";
		else nav.style.top = Math.min(nav.offsetTop-delta*2,0) + "px";
		last_pos = pos;
	}
	// Eventhandler setzen
	var handler_set = false;
	var mq = window.matchMedia("screen and (min-width:46em)");
	var sethandler = function() {
		if(mq.matches) {
			if(!handler_set) {
				window.addEventListener("scroll",scroll_nav);
				// Alle Submenüs schließen, wenn Mausbewegung, Klick oder Touch außerhalb Navigation
				window.addEventListener("mouseover",close_all);  
				window.addEventListener("touchstart",close_all);
				window.addEventListener("click",close_all);
				handler_set = true;
			}
		}
		else {
			if(handler_set) {
				window.removeEventListener("scroll",scroll_nav);
				window.removeEventListener("mouseover",close_all);  
				window.removeEventListener("touchstart",close_all);
				window.removeEventListener("click",close_all);
				handler_set = false;
			}
			nav.style.top = 0;
		}
	}
	mq.addListener(sethandler);
	sethandler();
})();

