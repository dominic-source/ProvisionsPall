$(function () {
  // Make sure to store all values of store here before proceeding
  let store = {};
  let products = {};
  let url = "http://127.0.0.2:5001/api/v1";

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

  let sendRequest = (url) => {
    return $.ajax({
      url: url,
      method: "GET",
      headers: {
        "content-type": "application/xml",
      },
      success: function (data) {
        console.log("success");
      },
      error: function (xhr, status, error) {
        console.log("error: ", error);
      },
      dataType: "json",
    });
  };

  $("#view, .user_image_normal").on("click", function () {
    $("#aside").removeClass("invisible");
    $("body").addClass("body-overflow");
  });
  $("#close").on("click", function () {
    $("#aside").addClass("invisible");
    $("body").removeClass("body-overflow");
  });

  $("#edit").on("click", function () {
    $(".dashboard_action").toggleClass("invisible");
    $(".view_products").addClass("invisible");
    $(".create_products").addClass("invisible");
    sendRequest(url + "/store").done(function (response) {
      // Remove all forms
      $(
        ".dashboard_action h4, .dashboard_action label, .dashboard_action input"
      ).remove();

      // Add data
      for (let info of response) {
        let element = `<label for="${info.id}" class="label_me"> 
            <h5>Store name: ${info.name} </h5>
            <button class="style_button submit_button open" data-id="${info.id}">edit</button>
            </label>
            <input class="style_input invisible" value type="text" 
                name="${info.name}" aria-label="${info.description}" 
                placeholder="Type here" id="${info.id}">`;

        $(".dashboard_action").prepend(element);
      }
      $(".dashboard_action").prepend("<h4> Edit store details details:</h4>");

      $(".dashboard_action .open").on("click", function () {
        if ($(this).html() === "edit") {
          $(this).html("close");
          $("#" + $(this).attr("data-id")).removeClass("invisible");
        } else {
          $(this).html("edit");
          $("#" + $(this).attr("data-id")).addClass("invisible");
        }
      });
      // Dashboard
      $(".dashboard_action input").on("change", function () {
        store[$(this).attr("name")] = $(this).val();
      });
      $("#submit").on("click", function () {
        console.log(store);
      });
    });
  });

  // View all products
  $("#produce").on("click", function () {
    $(".view_products").toggleClass("invisible");
    $(".dashboard_action").addClass("invisible");
    $(".create_products").addClass("invisible");

    sendRequest(url + "/products").done(function (response) {
      // Remove all forms
      $(
        ".view_products h4, .view_products label, .view_products button, .view_products input, .view_products h5"
      ).remove();

      // Add data
      $(".view_products").append("<h4> View all products</h4>");

      for (let info of response) {
        products[info["id"]] = {};
        let name = `<h5 data-id="${info["id"]}">Product name: ${info.name} </h5>`;
        $(".view_products").append(name);
        for (let newData in info) {
          let randomId = generateUUID();
          let element = `<label for="${randomId}" class="label_me"> 
           <h6>${newData}: ${info[newData]}</h6>
           <button class="style_button submit_button open" data-id="${randomId}">edit</button>
           </label>
           <input class="style_input invisible" value="${info[newData]}" type="text" 
               name="${newData}" aria-label="${info.description}" 
                id="${randomId}">`;
          $(".view_products").append(element);
        }
        $(".view_products").append("<hr />");
      }
      $(".view_products").append(
        '<button id="submit2" class="style_button submit_button">Save</button>'
      );

      $(".view_products .open").on("click", function () {
        if ($(this).html() === "edit") {
          $(this).html("close");
          $("#" + $(this).attr("data-id")).removeClass("invisible");
        } else {
          $(this).html("edit");
          $("#" + $(this).attr("data-id")).addClass("invisible");
        }
      });
      // view Board
      $(".view_products input").on("change", function () {
        let id = $(".view_products h5").attr("data-id");
        products[id][$(this).attr("name")] = $(this).val();
      });
      $("#submit2").on("click", function () {
        console.log(products);
      });
    });
  });

  //Create a product
  $("#create").on("click", function () {
    $(".view_products").addClass("invisible");
    $(".dashboard_action").addClass("invisible");
    $(".create_products").toggleClass("invisible");

    sendRequest(url + "/products").done(
      function (info) {
        // Remove all forms
        $(
          ".create_products h4, .create_products label, .create_products input"
        ).remove();
        $(".create_products").append("<h4> Add a new product:</h4>");

        // Add data
        for (let data in info[7]) {
          let randomId = generateUUID();
          let element = `<label for="${randomId}" class="label_me"> 
           </label>
           <input class="style_input" value type="text" 
               name="${data}" aria-label="This is where you type ${data}" 
               placeholder="Type the ${data} here" id="${randomId}">`;

          $(".create_products").append(element);
        }
        $(".create_products").append(
          '<button id="submit3" class="style_button submit_button">create</button>'
        );

        $(".create_products .open").on("click", function () {
          if ($(this).html() === "edit") {
            $(this).html("close");
            $("#" + $(this).attr("data-id")).removeClass("invisible");
          } else {
            $(this).html("edit");
            $("#" + $(this).attr("data-id")).addClass("invisible");
          }
        });

        // create product
        $(".create_products input").on("change", function () {
          products[$(this).attr("name")] = $(this).val();
        });
        $("#submit3").on("click", function () {
          $(".create_products input").val("");
          console.log(products);
        });
      }
    );
  });
});
