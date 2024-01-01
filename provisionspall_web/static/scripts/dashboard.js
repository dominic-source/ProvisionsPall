$(function () {
  // Make sure to store all values of store here before proceeding

  // The url of the application
  let url = "https://api-services-swfd.onrender.com/api/v1";

  // A function to generate unique Id for elements
  function generateUUID() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
      /[xy]/g,
      function (c) {
        let r = (Math.random() * 16) | 0;
        let v = c == "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
      }
    );
  }
  // Here is the user Id
  let id = $(".user_details").data('user_id')

  // a variable that returns an Ajax request
  let sendRequest = (url, method = 'GET', data = null) => {
    return $.ajax({
      url: url,
      method: method,
      data: data,
      contentType: false,
      processData: false,
      success: function (data) {
        console.log("success");
      },
      error: function (xhr, status, error) {
        console.log("error: ", error);
      },
    });
  };



  $("#view, .user_image_normal").on("click", function () {
    $("#aside").removeClass("invisible");
    $("body").addClass("body-overflow");

    // Update the user information for each click
    sendRequest(url + "/user/" + id).done(function (info) {
      $("#user_details h4, #user_details h3").remove();
      let element = ` <h3>USER DETAILS</h3>
      <h4>User name: ${info[0].username}</h4>
      <h4>Company name: ${info[0].stores.length == 0 ? "No name yet" : info[0].stores[0].name}</h4>
      <h4>Number of stores: ${info[0].stores.length}</h4>
      <h4>Number of Products: ${info[0].products}</h4>`
      $("#user_details").append(element);

    });

  });

  // The close button
  $("#close").on("click", function () {
    $("#aside").addClass("invisible");
    $("body").removeClass("body-overflow");
  });

  // The create store button
  $("#store").on("click", function () {
    $("#aside").addClass("invisible");
    $(".create_store").removeClass("invisible")
    $("body").removeClass("body-overflow");
  });

  // The dashboard special button
  $("#edit").on("click", function (event) {
    $(".dashboard_action").toggleClass("invisible");
    $(".view_products").addClass("invisible");
    $(".create_products").addClass("invisible");
    sendRequest(url + "/user/" + id + "/stores").done(function (response) {
      // Remove all forms
      $(".dashboard_action").empty();

      // Add data
      $(".dashboard_action").append(
        "<h4 id='up'> Edit store details:</h4>"
      );
      // Looping over the response gotten from the AJAX request
      for (let info of response) {

        let uniqueId = generateUUID();
        let elem = `<h5>Store name: ${info.name} <button class="style_button submit_button store_del" data-id="${info.id}">delete</button></h5>`;
        $(".dashboard_action").append(`<div id="${uniqueId}"></div>`);
        $(`.dashboard_action #${uniqueId}`).append(elem);

        // Looping over each item in the array from the response
        for (let data in info) {
          let randomId = generateUUID();
          let element = `<label for="${randomId}" class="label_me"> 
          <h6>${data}: ${info[data]}</h6>
            <button class="style_button submit_button open" data-id="${randomId}">edit</button>
            </label>
            <input class="style_input invisible" value=${info[data]} type="text" 
                name="${data}" aria-label="${info.description}" 
                id="${randomId}">`;

          $(`.dashboard_action  #${uniqueId}`).append(element);
        }
        $(`.dashboard_action  #${uniqueId}`).append(
          `<button class="style_button submit_button submit" data-id="${uniqueId}">Update</button>`
        );
        $(`.dashboard_action  #${uniqueId}`).append("<hr />");

      }
      $(`.dashboard_action .open`).on("click", function (event) {
        if ($(this).html() === "edit") {
          $(this).html("close");
          $("#" + $(this).attr("data-id")).removeClass("invisible");
        } else {
          $(this).html("edit");
          $("#" + $(this).attr("data-id")).addClass("invisible");
        }
      });

      // Delete a store
      $(".store_del").on("click", function (event) {
        let id2 = $(this).attr('data-id');
        sendRequest(url + "/user/store/" + id2, method = 'DELETE').done(function (response) {
          $(".dashboard_action").empty();
          $(".dashboard_action").toggleClass("invisible");
          $(".view_products").addClass("invisible");
          $(".create_products").addClass("invisible");
        });
      });
      // Update store data
      $(".submit").on("click", function (event) {
        id3 = $(this).attr('data-id');
        let formData = new FormData();
        formData.append('name', $('#' + id3 + ' input[name=name]').val());
        formData.append('description', $('#' + id3 + ' input[name=description]').val());
        formData.append('store_id', $('#' + id3 + ' input[name=id]').val());
        sendRequest(url + "/user/" + id + "/stores", method = 'PUT', data = formData).done(function (response) {
          $(".dashboard_action").empty();
          $(".dashboard_action").toggleClass("invisible");
          $(".view_products").addClass("invisible");
          $(".create_products").addClass("invisible");
        });
      });
    });
  });

  // View all products
  $("#produce").on("click", function () {
    $(".view_products").toggleClass("invisible");
    $(".dashboard_action").addClass("invisible");
    $(".create_products").addClass("invisible");
    $(".view_products section").empty();

    // Send a request to get all stores information
    sendRequest(url + "/user/" + id + "/stores").done(function (info) {
      $('#mySelect2').empty();
      $('#mySelect2').append(`<option selected disabled>Select an option</option>`)

      for (let data of info) {
        $('#mySelect2').append(`<option value="${data.id}" class="style_button" >${data.name}</option>`)
      }
      $('#mySelect2').on('change', function () {
        let select_id2 = $('#mySelect2').val();
        sendRequest(url + "/" + select_id2 + "/product").done(function (response) {
          // console.log(response);
          $(".view_products section").empty();

          // List all the products
          $(".view_products section").append("<h4> View all products</h4>");

          for (let info of response) {
            let uniqueId = generateUUID();
            let name = `<h5 data-id="${info["id"]}">Product name: ${info.name} <button class="style_button submit_button product_del" data-id="${uniqueId}">delete</button></h5>`;
            $(".view_products section").append(`<div id="${uniqueId}"></div>`);
            $(`.view_products section #${uniqueId}`).append(name);
            for (let newData in info) {
              let randomId = generateUUID();
              let element = `<label for="${randomId}" class="label_me"> 
           <h6>${newData}: ${info[newData]}</h6>
           <button class="style_button submit_button open" data-id="${randomId}">edit</button>
           </label>
           <input class="style_input invisible" value="${info[newData]}" type="text" 
               name="${newData}" aria-label="${info.description}" 
                id="${randomId}">`;
              $(`.view_products #${uniqueId}`).append(element);
            }
            $(`.view_products #${uniqueId}`).append(
              `<button class="style_button submit_button submit2" data-id="${uniqueId}">update</button>`
            );
            $(`.view_products #${uniqueId}`).append("<hr />");
          }

          $(".view_products .open").on("click", function () {
            if ($(this).html() === "edit") {
              $(this).html("close");
              $("#" + $(this).attr("data-id")).removeClass("invisible");
            } else {
              $(this).html("edit");
              $("#" + $(this).attr("data-id")).addClass("invisible");
            }
          });

          // Delete a product
          $(".product_del").on("click", function (event) {
            let id5 = $(this).attr('data-id');
            let p_id = $('#' + id5 + ' input[name=id]').val();
            sendRequest(url + "/product/" + p_id, method = 'DELETE').done(function (response) {
              $(".view_products").toggleClass("invisible");
              $(".dashboard_action").addClass("invisible");
              $(".create_products").addClass("invisible");
              console.log(response);
            });
          });

          // Update product
          $(".submit2").on("click", function () {
            let id4 = $(this).attr('data-id');
	    let formData = new FormData();
            formData.append('name', $('#' + id4 + ' input[name=name]').val());
            formData.append('description', $('#' + id4 + ' input[name=description]').val());
            formData.append('price', $('#' + id4 + ' input[name=price]').val());
            formData.append('category', $('#' + id4 + ' input[name=category]').val());
            let p_id = $('#' + id4 + ' input[name=id]').val();
            sendRequest(url + "/product/" + p_id, method = 'PUT', data = formData).done(function (response) {
              $(".view_products").toggleClass("invisible");
              $(".dashboard_action").addClass("invisible");
              $(".create_products").addClass("invisible");
            });
          });
        });
      });
    });
  });

  //Create a product
  $("#create").on("click", function () {
    $(".view_products").addClass("invisible");
    $(".dashboard_action").addClass("invisible");
    $(".create_products").toggleClass("invisible");

    // Send a request to get all stores information
    sendRequest(url + "/user/" + id + "/stores").done(function (info) {
    $('#mySelect option').remove()  
    for (let data of info) {
        $('#mySelect').append(`<option value="${data.id}">${data.name}</option>`)
      }
    });

    // The submit button for product creation
    $('#submit_store2').on('click', function () {

      let select_id = $('#mySelect').val();

      let imageInput2 = $('#imageInput2')[0].files[0];
      let formData = new FormData();
      formData.append('file', imageInput2);
      formData.append('name', $('#name2').val());
      formData.append('description', $('#description2').val());
      formData.append('price', $('#price').val());
      formData.append('category', $('#category').val());
      formData.append('store_id', select_id);

      $.ajax({
        url: url + "/" + select_id + "/product",
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (data) {
          console.log("success");
          $('.create_products input').each((function () {
            $(this).val("");
          }));
        },
        error: function (xhr, status, error) {
          console.log("error: ", error);
          $('.create_products input').each((function () {
            $(this).val("");
          }));
        },
      });
    });
  });
});
