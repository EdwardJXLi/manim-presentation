/*
Main script file for manim-presentation
*/

//Global Vars
var timecodes;
var video;
var debug = true;
var goToTime = undefined; //Hacky implementation, -1 means to skip time checking

//Debug Print
function debugLog(text){
    if(debug == true){
        console.log(text);
    }
}

//Fullscreen Code
function openFullscreen() {
    var elem = document.documentElement;
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.mozRequestFullScreen) { /* Firefox */
        elem.mozRequestFullScreen();
    } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE/Edge */
        elem.msRequestFullscreen();
    }
}

//Start Presentation
function initPres(){
    video = document.getElementById("videoPlayer");
    openFullscreen();
    document.getElementById("loadPanel").style.display="none"; //Hide Loading Controls
    document.getElementById("videoPanel").style.display="inline"; //Show Video Box
    video.src = URL.createObjectURL(document.getElementById("video").files[0]); //Set video object to video file uploaded
    //Read from timecodes file and add values variable
    var fr = new FileReader();
    fr.onload = function(e) {
        var res = e.target.result;
        timecodes = res.split("\n").map(x=>+x);
        debugLog(timecodes);
        //Add zero onto the front if 0 does not exist
        if(timecodes[0] != 0){
            timecodes.unshift(0);
        }
    };
    fr.readAsText(document.getElementById("timecode").files[0]);
    //video.play();
    startPres();
}

function startPres(){
    currentSlide = 0;
    //Video handler that checks time every frame
    video.addEventListener("timeupdate", function(){
        if(goToTime != undefined){
            debugLog("VIDEO FRAME HANDLER: currentTime: " + this.currentTime + " | goToTime: " + goToTime);
            if(this.currentTime >= goToTime) {
                this.pause();
            }
        }
    });
    //Checks for presentation keyboard control
    document.addEventListener('keydown', function(event) {
        if(event.keyCode == 37) {
            //alert('Left was pressed');
            currentSlide = processPrevSlide(currentSlide - 1);
        }
        else if(event.keyCode == 39 || event.keyCode == 32) {
            //alert('Right was pressed');
            currentSlide = processNextSlide(currentSlide + 1);
        }
    });
    //Checks for presentation mouse control
    video.addEventListener('click', function() {
        currentSlide = processNextSlide(currentSlide + 1);
    });
}

//Code to run animation until next slide
function processNextSlide(toSlide){
    fromSlide = toSlide - 1;
    debugLog("FROM SLIDE " + fromSlide + " TO SLIDE " + toSlide);

    //If Slide Is Less Than 0, Do Nothing (This should never happen)
    if(fromSlide < 0){
        debugLog("event1");
        video.pause();
        return 0;
    }
    //If Presentation Is Done, Do Nothing
    else if(toSlide > timecodes.length){
        debugLog("event2");
        video.pause();
        return toSlide;
    }
    //Play Video Until Final Slide
    else{
        debugLog("event3");
        video.currentTime = timecodes[fromSlide];
        //Kind of hacky implementation where if the presentation goes to the last slide, 
        //the value is undefined, allowing the play to play until the end!
        goToTime = timecodes[toSlide]; 
        debugLog(timecodes[toSlide]);
        video.play();
        return toSlide;
    }
    
}

//Code to run animation until previous slide
function processPrevSlide(toSlide){
    debugLog("TO SLIDE " + toSlide);

    //If Slide Is Less Than 0, Do Nothing
    if(toSlide < 0){
        debugLog("event1");
        video.pause();
        return 0;
    }
    //If Presentation Is Done, Do Nothing (This should never happen)
    else if(toSlide >= timecodes.length){
        debugLog("event2");
        video.pause();
        return timecodes.length;
    }
    //Set time to previous time
    else{
        debugLog("event3");
        video.pause();
        video.currentTime = timecodes[toSlide];
        return toSlide;
    }
}