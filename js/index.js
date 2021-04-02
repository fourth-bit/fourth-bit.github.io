"use strict";

$(document).ready(function(){
    $(".dropdown").on('click', function(){
        var ul = $(this).children("ul");
        var arrow = $(this).children("div").children("h4").children("span");
        if (ul.css('height') === '0px') {
            ul.css({margin: '', padding: ''});
            ul.css({display: 'none', height: 'initial'});
            var h = ul.css('height');
            ul.css({height: '0px', display: ''});
            ul.animate({height: h}, 250);
            $({deg: 0}).animate({deg: 180}, {
                duration: 250,
                step: function(now) {
                    arrow.css({
                        transform: 'rotate(' + now + 'deg)',
                        bottom: (0.4 / 180) * (180 - now) - 0.2 + 'rem'
                    });
                }
            });
        } else {
            ul.animate({height: '0px'}, 250);
            $({deg: 180}).animate({deg: 0}, {
                duration: 250,
                step: function(now) {
                    arrow.css({
                        transform: 'rotate(' + now + 'deg)',
                        bottom: (0.4 / 180) * (180 - now) - 0.2 + 'rem'
                    });
                    if (now === 0) {
                        ul.css({margin: 0, padding: 0});
                    }
                }
            });
        }
    });
});