$(document).ready(function(){
  $(".button-collapse").sideNav({
    menuWidth: 300,
    edge: 'left',
  });
  $('.modal').modal({
    dismissible: true,
    opacity: .5,
    in_duration: 300,
    out_duration: 200,
  });
  $('.collapsible').collapsible();
  $('.slider').slider();
});
