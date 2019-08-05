window.onload = () => {
  'use strict';

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
             .register('./sw.js');
  }
}


function changeImage() {
  var images = ['images/play-arrow.png', 'images/pause-symbol.png'],
                i = 1;

            // preload
            for (var j=images.length; j--;) {
                var img = new Image();
                img.src = images[j];
            }

            // event handler
            document.getElementById("foo").addEventListener('click', function() {
                this.src = images[i >= images.length - 1 ? i = 0 : ++i];
            console.log("changed image");
            }, false);
  }
  // // if (document.getElementById("foo").src == "images/pause-symbol.png")
  // // {
  // if (Image.getAttribute("value") == 0)
  // {
  //    document.getElementById("foo").src = "images/play-arrow.png";
  //    Image.setAttribute("value") = 1;
  // }
  // else if (Image.getAttribute("value") == 1)
  // {
  //    document.getElementById("foo").src = "images/pause-symbol.png";
  //    Image.setAttribute("value") = 0;
  // }
