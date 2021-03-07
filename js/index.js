"use strict";

var idx;

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

    return $('<a>').attr("href", "./charities/" + obj.name).css({"color": "inherit"}).append($card);
}



$(document).ready(function(){
    $(".dropdown").on('click', function(){
        var ul = $(this).children("ul");
        if (ul.css('height') === '0px') {
            ul.css({display: 'none', height: 'initial'});
            var h = ul.css('height');
            ul.css({height: '0px', display: ''});
            ul.animate({height: h}, 250);
        } else {
            ul.animate({height: '0px'}, 250);
        }
    });
});

$.getJSON("./json/charities.json", function(data) {
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
});
