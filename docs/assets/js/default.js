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
  $("#homebutton").click(function() {
    homepage();
  });
  $("#audiobutton").click(function() {
    audiopage();
  });
  $("#imagebutton").click(function() {
    imagepage();
  });
  $("#textbutton").click(function() {
    textpage();
  });
  $("#youtubebutton").click(function() {
    youtubepage();
  });

  homepage();

});

// Hide all page sections
function clearPage() {

  $("#homebg").hide();
  $("#audiobg").hide();
  $("#imagebg").hide();
  $("#textbg").hide();
  $("#youtubebg").hide();

  // Hide navbar when option is selected
  if (navbar) {
    toggleNav();
  }

}

// Toggles navigation sidebar
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

// Show page section
function homepage() {
  clearPage();
  $("#homebg").show();
}
function audiopage() {
  clearPage();
  $("#audiobg").show();
}
function imagepage() {
  clearPage();
  $("#imagebg").show();
}
function textpage() {
  clearPage();
  $("#textbg").show();
}
function youtubepage() {
  clearPage();
  $("#youtubebg").show();
}
