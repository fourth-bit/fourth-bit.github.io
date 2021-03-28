"use strict";

var idx;

class Charity {
    constructor(obj) {
        this.name = obj.name;
        this.address = obj.address;
        this.about = obj.about;
        this.website = obj.website;
        this.email = obj.email;
    }

    list_view() {
        var $card = $('<div>').addClass(["card", "bg-secondary"]);

        // Add title
        $card.append(
            $('<h5>').addClass('card-title').text(this.name)
        );

        // Add description
        $card.append(
            $('<div>').addClass('card-body').append(
                $('<p>').text(this.about)
            )
        );

        // Add web and real address
        $card.append(
            $('<div>').addClass('card-footer').append(
                [
                    $('<span>').text(this.address),
                    $('<a>').addClass("card-link").text(this.website)
                ]
            )
        );

        $card.on("click", this.click_handler);

        return $card;
    }

    click_handler() {

    }

    detail_view() {
        
    }
}

function list_view(obj) {
    /*
    Generate the list view of the charity.
    FORMAT:
    <div class="card bg-secondary">
        <h4 class="card-title">NAME</h4>
        <div class="card-body">
            <p>description</p>
        </div>
        <div class="card-footer">
            <span>Address</span>
            <a class="card-link">website</a>
        </div>
        </div>
    </div>
    */
    var $card = $('<div>').addClass(["card", "bg-secondary"]);
    // Add h4
    $card.append(
        $('<h4>').addClass('card-title').text(obj.name)
    );
    // Add description
    $card.append(
        $('<div>').addClass('card-body').append(
            $('<p>').text(obj.about)
        )
    );
    // Add web and real address
    $card.append(
        $('<div>').addClass('card-footer').append(
            [
                $('<span>').text(obj.address),
                $('<a>').addClass("card-link").text(obj.website)
            ]
        )
    );

    $card.on("click", function(){
        
    });

    return $card;
}

/*$.getJSON("./json/charities.json", function(data) {
    idx = lunr(function(){
        this.ref('name');
        this.field('name');
        this.field('about');
        this.field('address');
        this.field('email');
        this.field('items');
    
        data.forEach(element => {
            this.add(element);
        }, this);
    });

    data.forEach(obj => {
        $(".card-container").append(list_view(obj));
    });
});*/

$(document).ready(function(){
    $(".dropdown").on('click', function(){
        var ul = $(this).children("ul");
        var arrow = $(this).children("div").children("h4").children("span");
        console.log(arrow)
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