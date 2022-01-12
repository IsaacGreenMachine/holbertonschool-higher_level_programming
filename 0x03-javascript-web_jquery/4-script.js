$('#toggle_header').click(function () {
  if ($('header').attr('class').includes('green')) {
    $('header').addClass('red');
    $('header').removeClass('green');
  } else if ($('header').attr('class').includes('red')) {
    $('header').addClass('green');
    $('header').removeClass('red');
  }
});
