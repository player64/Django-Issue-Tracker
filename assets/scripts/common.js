'use strict';

// mobile menu handler
$('#menuOpener').click(function()  {
    $(this).next('div').slideToggle('show');
});