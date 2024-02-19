$(function () {

    let store_id = $('#address').attr('data-store');
    let url = "https://provisionspall.onrender.com/api/v1";
    // Display the addres when the button for address clicked
    $('#address, #address2').on('click', function () {
        $.ajax({
            url: url + "/locate/" + store_id,
            type: 'GET',
            header: {
                'Content-Type': 'application/json',
            },
            success: function (response) {
                $("#close").on("click", function () {
                    $("#aside").addClass("invisible");
                    $("body").removeClass("body-overflow");
                });
                $('#aside').removeClass('invisible');
                let element = `<h4>Store address information</h4>
                <p>Name of store: ${response.addressFormat[0].store_name}</p>
                <p>Address number: ${response.addressFormat[0].number} </p>
                <p>Street Number': ${response.addressFormat[0].street} </p>
                <p>Location area: ${response.addressFormat[0].area} </p>
                <p>City: ${response.addressFormat[0].city} </p>
                <p>Country: ${response.addressFormat[0].country} </p>
                <p>Longitude: ${response.addressFormat[0].longitude} </p>
                <p>Latitude: ${response.addressFormat[0].latitude} </p>
                `
                $('#store_address').append(element);
            },
            error: function (error) {
                console.log(error);
            },
        });
    });

    // Get the all stores or product information
    // to save having to get data for each input
    let url2;
    if (!store_id) {
        url2 = url + "/stores";
    } else {
        url2 = `${url}/${store_id}/product`;
    }

    let items = {};
    $.ajax({
        url: url2,
        type: 'GET',
        header: {
            'Content-Type': 'application/json',
        },
        success: function (response) {
            if (!store_id) items.stores = response;
            else items.products = response;
        },
        error: function (error) {
            console.log(error);
        },
    });

    let cache_id = $('.image-grid').attr('data-cache');
    $('#searchBar').on('input', function () {
        let data = $(this).val()
        // If search is empty list should be visible else do otherwise
        if (data == "") {
            $('.image-grid > .card').removeClass('invisible');
            $('.image-grid .uniqueElement').remove();
        }
        else {
            $('.image-grid .uniqueElement').remove();
            $('.image-grid > .card').addClass('invisible');

            // Arrange Element based on most probable value
            let startElements = '';
            let nextElements = '';
            // console.log(store_id, "give me a moment ");
            if (!store_id) {
                // Loop over the stores to get the stores need
                for (let item of items.stores) {
                    // Create Card for stores
                    let element = `<a href='/market/store/${item.id}?${cache_id}' class="card uniqueElement"
                                data-id="${item.id}">
                                <img src="/static/uploads/${item.image}?${cache_id}" alt="Store Image">
                                <div class="card-content">
                                <h2 class="card-title">${item.name}</h2>
                                <p class="card-description">${item.description}</p>
                                </div>
                            </a>`
                    if (item.name.toUpperCase().startsWith(data.toUpperCase())) startElements += element;
                    else if (item.name.toUpperCase().includes(data.toUpperCase())) nextElements += element;
                }

            } else {
                // Loop over the products to get the product need
                for (let item of items.products) {
                    // Create Card for products
                    let element = `<div class="card uniqueElement" data-id="${item.id}">
                                    <img src="/static/uploads/${item.image}?${cache_id}"
                                    alt="Product Image">
                                    <div class="card-content">
                                    <h2 class="card-title">${item.name}</h2>
                                    <p class="card-description">${item.category}</p>
                                    <p class="card-title">$ ${item.price}</p>
                                    </div>
                                </div>`
                    if (item.name.toUpperCase().startsWith(data.toUpperCase())) startElements += element;
                    else if (item.name.toUpperCase().includes(data.toUpperCase())) nextElements += element;
                }
            }

            if (startElements == '' && nextElements == '') {
                $('.image-grid').append('<h1 class="uniqueElement login-link2" style="margin: 50% 20%; width: 200px;">No data was found</h1>');
            } else {
                $('.image-grid').append(startElements);
                $('.image-grid').append(nextElements);
            }
        }

    });


    // For mobile phones    
    $('.smallDevice').on('click', function inner() {
        $(this).toggleClass('rotate');
        $('.device').toggleClass('asideDash');
        $('.asideItem').toggleClass('invisible');

        $(window).on('resize', function () {
            let windowWidth = $(window).width();
            if (windowWidth > 500) {
                $('.smallDevice').removeClass('rotate');
                $('.device').removeClass('asideDash');
                $('.asideItem').addClass('invisible');
            } else if (windowWidth < 500) {
                    $('.smallDevice').removeClass('rotate');
                    $('.device').removeClass('asideDash');
                    $('.asideItem').addClass('invisible');
            }
        });
    });
});
