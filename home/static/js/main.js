
//printing function
var myApp = new function () {
    this.printDiv = function () {
        // Store DIV contents in the variable.
        var img = document.getElementById('parent');
        
        // Create a window object.
        var win = window.open('', '', 'height=800,width=800'); // Open the window. Its a popup window.
        win.document.write(img.outerHTML);     // Write contents in the new window.
        win.document.close();
    }
}

//top page button function

// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


