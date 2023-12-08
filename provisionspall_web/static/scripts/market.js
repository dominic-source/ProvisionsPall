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
                window.alert(JSON.stringify(response.addressFormat));
            },
            error: function (error) {
                console.log(error);
            },
        });
    });
});
