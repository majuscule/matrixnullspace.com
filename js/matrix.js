$(document).ready(function(){
  $('#submit').click(function(event){
    if ($('#matrix').val() == ''
        || $('#matrix').val().match(/[^.\-\d\s]/) != null) {
        event.preventDefault();
        $('#results').fadeOut('slow', function() {
            $('#results').html(
                $('<span>').attr('id', 'fail').text(
                    $('#matrix').val() == '' ?
                        'Enter a matrix!' : 'Invalid character in matrix.'
                    ));
            $('#results').fadeIn();
        });
        return;
    }
    $.post('/calculate', { 'matrix' : $('#matrix').val() })
        .done(function(data) {
            $('#results').fadeOut('slow', function() {
                $('#results').html('').append(
                    $('<li>').text('eigenvalues').append(
                        $('<pre>').text(data.eigenvalues)),
                    $('<li>').text('determinant').append(
                        $('<pre>').text(data.determinant)),
                    $('<li>').text('nullspace').append(
                        $('<pre>').text(data.nullspace))
                );
                $('#results').fadeIn();
            });
        })
        .fail(function(data) {
            $('#results').fadeOut('slow', function() {
                $('#results').html(
                    $('<span>').attr('id', 'fail')
                        .text('Uh-oh, something\'s gone wrong!'));
                $('#results').fadeIn();
            });
        });
  });
  $('textarea').focus(function(e) {
      $(e.target).text('');
      $(e.target).css({ 'color' : 'black', 'font-style' : 'none' });
  });
});
