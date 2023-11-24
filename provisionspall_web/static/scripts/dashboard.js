$(function() {

    // Make sure to store all values of store here before proceeding
    let store = {};
    let products = {};

    $('#view, .user_image_normal').on('click', function () {
        $('#aside').removeClass('invisible');
        $('body').addClass('body-overflow');
    });
    $('#close').on('click', function () {
        $('#aside').addClass('invisible');
        $('body').removeClass('body-overflow');
    });

    $('#edit').on('click', function() {
        $('.dashboard_action').toggleClass('invisible');
        $('.view_products').addClass('invisible');
        $('.create_products').addClass('invisible');


    });

    $('#produce').on('click', function() {
        $('.view_products').toggleClass('invisible');
        $('.dashboard_action').addClass('invisible');
        $('.create_products').addClass('invisible');
    });

    $('#create').on('click', function() {
        $('.view_products').addClass('invisible');
        $('.dashboard_action').addClass('invisible');
        $('.create_products').toggleClass('invisible');
    });

    $('.open').on('click', function (){
        if ($(this).html() === 'edit') {
            $(this).html('close');
            $('#' + $(this).attr('data-id')).removeClass('invisible');
        } else {
            $(this).html('edit');
            $('#' + $(this).attr('data-id')).addClass('invisible');
        }
    });

    // Dashboard
    $('.dashboard_action input').on('change', function(){
        store[$(this).attr('name')] = $(this).val();
    });
    $('#submit').on('click', function() {
        console.log(store);
    });

    // view Board
    $('.view_products input').on('change', function(){
        products[$(this).attr('name')] = $(this).val();
    });
    $('#submit2').on('click', function() {
        console.log(products);
    });

    // create product
    $('.create_products input').on('change', function(){
        products[$(this).attr('name')] = $(this).val();
    });
    $('#submit3').on('click', function() {
        $('.create_products input').val("");
        console.log(products);
    });

});