$(function () {
    $('#address').on('click', function () {
        let store_id = $(this).attr('data-store');
        $.ajax({
            url: "http://127.0.0.2:5001/api/v1/locate/" + store_id,
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
});
