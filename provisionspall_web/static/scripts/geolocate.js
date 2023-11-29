
function initMap() {

    // Map option
    let options = {
        center: { lat: 7.7190, lng: 5.3110 },
        zoom: 10,
    }

    //New Map
    let map = new google.maps.Map(document.getElementById("map"), options);

    // listen for click on map location
    /*
        //Maker
        let marker = new google.maps.Marker({
            position: {lat: 7.7979, lng: 5.3286},
            map: map,
            icon: "https://img.icons8.com/nolan/2x/marker.png"
        });
    
        // InfoWindow
        const detailWindow = new google.maps.InfoWindow({
            content: `<h2>Ikole City</h2>`,
        });
    
        marker.addListener('mouseover', () => {
            detailWindow.open(map, marker);
        });
    */
    // Add Markers to array
    MarkerArray = [
        {
            location: { lat: 7.7979, lng: 5.3286 },
            imageIcon: "https://img.icons8.com/nolan/2x/marker.png",
            content: `<h2>Ikole City</h2>`,
        },
        {
            location: { lat: 7.4991, lng: 5.2319 },
            content: `<h2>Ikere City</h2>`,
        }
    ]

    // Create a for loop for markers
    for (let i = 0; i < MarkerArray.length; i++) {
        addMarker(MarkerArray[i]);
    }

    // Add marker
    function addMarker(property) {
        let marker = new google.maps.Marker({
            position: property.location,
            map: map,
            // icon: property.imageIcon,
        });
        // Check custom Icon
        if (property.imageIcon) {
            // set image Icon
            marker.setIcon(property.imageIcon);
        }

        if (property.content) {
            // InfoWindow
            const detailWindow = new google.maps.InfoWindow({
                content: property.content,
            });

            marker.addListener('mouseover', () => {
                detailWindow.open(map, marker);
            });
        }

    }
}