$(function () {
    $('#store').on('click', function () {
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition(
                function (position) {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;
                    // Remove readonly attribute
                    $('#longitude').removeAttr('readonly')
                    $('#latitude').removeAttr('readonly')

                    $('#longitude').val(longitude)
                    $('#latitude').val(latitude)
                    $('#longitude').attr('readonly', 'true')
                    $('#latitude').attr('readonly', 'true')

                    // You can use latitude and longitude here as needed
                },
                function (error) {
                    switch (error.code) {
                        case error.PERMISSION_DENIED:
                            console.error('User denied the request for Geolocation.');
                            break;
                        case error.POSITION_UNAVAILABLE:
                            console.error('Location information is unavailable.');
                            break;
                        case error.TIMEOUT:
                            console.error('The request to get user location timed out.');
                            break;
                        case error.UNKNOWN_ERROR:
                            console.error('An unknown error occurred.');
                            break;
                    }
                }
            );
        } else {
            console.error('Geolocation is not supported by this browser.');
        }
    });
    let options;
    $('#submit_store').on('click', function () {
        options = {
            'name': $('#name').val(),
            'description': $('#description').val(),
            'number': $('#number').val(),
            'street': $('#street').val(),
            'area': $('#area').val(),
            'city': $('#city').val(),
            'country': $('#country').val(),
            'longitude': $('#longitude').val(),
            'latitude': $('#latitude').val(),
        }
        let id = $('#view').attr('data-user_id')
        $.ajax({
            url: "http://127.0.0.2:5001/api/v1/user/" + id + "/stores",
            type: 'POST',
            data: JSON.stringify(options),
            headers: {
                "content-type": "application/json",
            },
            success: function (data) {
                console.log("success");
                $(".create_store").addClass("invisible");
                $("body").removeClass("body-overflow");
            },
            error: function (xhr, status, error) {
                console.log("error: ", error);
            },
        });
    });
   
    $("#close2").on("click", function () {
        $(".create_store").addClass("invisible");
        $("body").removeClass("body-overflow");
    });
});