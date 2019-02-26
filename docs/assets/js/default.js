/*

  Author: Robby Bergers

  This is the main JS file used by the BADMedia page

*/

/* Variables */

navbar = false;

/* Functions */

$(document).ready(function() {

  // Set event listeners
  $("#navbar").click(function() {
    toggleNav();
  });

});

function toggleNav() {
  if (navbar) {
    $("#nav").css("height", "0");
  } else {
    $("#nav").css("height", "100vh");
  }
}
