$(document).ready(function(){
  $('#submit').click(function(event){
    if ( $('#matrix').val() == ''
       ){
         event.preventDefault();
    }
  });
});
