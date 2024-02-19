$(function () {
    let url = "https://provisionspall.onrender.com/api/v1";
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
    // The submit button for Store creation
    $('#submit_store').on('click', function () {

        let imageInput = $('#imageInput')[0].files[0];
        let formData = new FormData();
        formData.append('file', imageInput);
        formData.append('name', $('#name').val());
        formData.append('description', $('#description').val());
        formData.append('number', $('#number').val());
        formData.append('street', $('#street').val());
        formData.append('area', $('#area').val());
        formData.append('city', $('#city').val());
        formData.append('country', $('#country').val());
        formData.append('longitude', $('#longitude').val());
        formData.append('latitude', $('#latitude').val());

        let id = $('#view').attr('data-user_id')
        $.ajax({
            url: url + "/user/" + id + "/stores",
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
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
