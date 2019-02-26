/*

  Author: Robby Bergers

  This is the main JS file used by the BADMedia page

*/

/* Variables */

navbar = false;

/* Functions */

$(document).ready(function() {

  // Set event listeners
  $("#navbutton").click(function() {
    toggleNav();
  });

});

function toggleNav() {
  if (navbar) {
    $("#nav").css("height", "0");
    $("#nav").css("opacity", "0");
    $("#navbutton").html("&#9776;");
    navbar = false;
  } else {
    $("#nav").css("height", "100vh");
    $("#nav").css("opacity", "1");
    $("#navbutton").html("&#10005;");
    navbar = true;
  }
}
