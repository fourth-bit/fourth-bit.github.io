"use strict";

var idx;

$.getJSON("/json/charities.json", function(data) {
    idx = lunr(function(){
        this.ref('name');
        this.field('name');
        this.field('about');
        this.field('address');
        this.field('email');
        this.field('items');
    
        data['charities'].forEach(element => {
            this.add(element);
        }, this);

        data['items'].forEach(element => {
            for (var i = 0; i < element['items'].length; i++) {
                let obj = {name: element['items'][i]};
                this.add(obj);
            }
        }, this);
    });

    const params = new URLSearchParams(window.location.search);
    const query = params.get('q');

    var search_result = idx.search(query);

    var content = $('<div>').addClass("container").attr({id: 'content'});
    content.html(
        "<h1 class='text-center'>Results for \"" + query + "\"</h1>"
    );

    var cardContainer = $('<div>').addClass("card-container");

    search_result.forEach(element => {
        var type;
        for (var i = 0; i < data['charities'].length; i++) {
            if (data['charities'][i]['name'] == element.ref) {
                type = 'Charity';
                break;
            }
            if (i + 1 == data['charities'].length) {
                type = 'Item';
            }
        }

        let card = $('<div>').addClass("card");
        card.append(
            $('<div>').addClass('card-header').append(
                $('<h4>').html(type)
            )
        );
        card.append(
            $('<div>').addClass('card-body').append(
                $('<h5>').html(element.ref)
            )
        );

        var url;
        if (type == 'Charity') {
            url = '/charities/';
        } else {
            url = '/items/';
        }

        url += element.ref.toLowerCase().replaceAll(' ', '-');
        url += '.html';

        cardContainer.append(
            $('<a>').attr({href: url}).addClass('result-link').append(card)
        );
    });

    if (search_result.length === 0) {
        content.html(
            "<h1 class='text-center'>No Results for \"" + query + "\"</h1>"
        );
    }

    content.append(cardContainer);

    content.append(
        $("<p>").html(
            "If you did not find what you were looking for, try to refine your search, or open an issue on <a class='text-info' href='https://github.com/fourth-bit/marin-donates/issues/new'>the github repository</a> if we are missing data."
        )
    );

    $('body').append(content);

    $('#spin-container').css({display: "none"}).removeClass("d-flex");
});