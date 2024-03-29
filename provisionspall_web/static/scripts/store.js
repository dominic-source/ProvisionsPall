const mapStyle = [{
    'featureType': 'administrative',
    'elementType': 'all',
    'stylers': [{
        'visibility': 'on',
    },
    {
        'lightness': 33,
    },
    ],
},
{
    'featureType': 'landscape',
    'elementType': 'all',
    'stylers': [{
        'color': '#f2e5d4',
    }],
},
{
    'featureType': 'poi.park',
    'elementType': 'geometry',
    'stylers': [{
        'color': '#c5dac6',
    }],
},
{
    'featureType': 'poi.park',
    'elementType': 'labels',
    'stylers': [{
        'visibility': 'on',
    },
    {
        'lightness': 20,
    },
    ],
},
{
    'featureType': 'road',
    'elementType': 'all',
    'stylers': [{
        'lightness': 20,
    }],
},
{
    'featureType': 'road.highway',
    'elementType': 'geometry',
    'stylers': [{
        'color': '#c5c6c6',
    }],
},
{
    'featureType': 'road.arterial',
    'elementType': 'geometry',
    'stylers': [{
        'color': '#e4d7c6',
    }],
},
{
    'featureType': 'road.local',
    'elementType': 'geometry',
    'stylers': [{
        'color': '#fbfaf7',
    }],
},
{
    'featureType': 'water',
    'elementType': 'all',
    'stylers': [{
        'visibility': 'on',
    },
    {
        'color': '#acbcc9',
    },
    ],
},
];


function initMap() {
    get_id = document.getElementById('map').dataset.ids;
    let url = "https://provisionspall-hwvs.onrender.com/api/v1/locate/" + get_id;
    // let url = "http://localhost:5000/api/v1/locate/" + get_id;

    fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(geoData => {
            //Create the map
            let longitude = geoData.geoJsonFormat.features[0].geometry.coordinates[0];
            let latitude = geoData.geoJsonFormat.features[0].geometry.coordinates[1];
            const map = new google.maps.Map(document.getElementById('map'),
                {
                    center: { lat: latitude, lng: longitude },
                    zoom: 13,
                    styles: mapStyle
                });

            map.data.addGeoJson(geoData.geoJsonFormat, { idPropertyName: 'storeid' });

            // Define the custom marker icons using the store's "category"
            map.data.setStyle((feature) => {
                return {
                    icon: {
                        url: `/static/images/icon_${feature.getProperty('category')}.png`,
                        scaledSize: new google.maps.Size(64, 64),
                    }
                }
            });
            const apiKey = 'AIzaSyCtRXnkNE4h6eeqCg0IoTyMXqyHrfbOYLI';
            const infoWindow = new google.maps.InfoWindow();

            // Show the information for a store when its marker is clicked
            map.data.addListener('click', (event) => {
                const category = event.feature.getProperty('category');
                const name = event.feature.getProperty('name');
                const description = event.feature.getProperty('description');
                const hours = event.feature.getProperty('hours');
                const phone = event.feature.getProperty('phone');
                const position = event.feature.getGeometry().get();
                const content = `<img style="float:left; width:200px; margin-top:30px" src="img/logo_${category}.png">
        <div style="margin-left:220px; margin-bottom:20px;">
          <h2>${name}</h2><p>${description}</p>
          <p><b>Open:</b> ${hours}<br/><b>Phone:</b> ${phone}</p>
          <p><img src="https://maps.googleapis.com/maps/api/streetview?size=350x120&location=${position.lat()},${position.lng()}&key=${apiKey}&solution_channel=GMP_codelabs_simplestorelocator_v1_a"></p>
        </div>
        `;
                infoWindow.setContent(content);
                infoWindow.setPosition(position);
                infoWindow.setOptions({ pixelOffset: new google.maps.Size(0, -30) });
                infoWindow.open(map);
            });

            // Build and add the search bar
            const card = document.createElement('div');
            const titleBar = document.createElement('div');
            const title = document.createElement('div');
            const container = document.createElement('div');
            const input = document.createElement('input');
            const options = {
                types: ['address'],
                componentRestrictions: { country: 'gb' },
            };
            card.setAttribute('id', 'pac-card');
            title.setAttribute('id', 'title');
            title.setContent = 'Find the nearest store';
            titleBar.appendChild(title);
            container.setAttribute('id', 'pac-container');
            input.setAttribute('id', 'pac-input');
            input.setAttribute('type', 'text');
            input.setAttribute('placeholder', 'Enter an address');
            container.appendChild(input);
            card.appendChild(titleBar);
            card.appendChild(container);
            map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

            // Make the search bar into a Places Autocomplete search bar and select
            // which detail fields should be returned about the place that
            // the user selects from the suggestions.
            const autocomplete = new google.maps.places.Autocomplete(input, options);

            autocomplete.setFields(['address compents', 'geometry', 'name']);


            // Set the origin point when the user selects an address
            const originMarker = new google.maps.Marker({ map: map });
            originMarker.setVisible(false);
            let originLocation = map.getCenter();
            autocomplete.addListener('place_changed', async () => {
                originMarker.setVisible(false);
                originLocation = map.getCenter();
                const place = autocomplete.getPlace();

                if (!place.geometry) {
                    // User entered the name of a Place that was not suggested and
                    // pressed the Enter key, or the Place Details request failed.
                    window.alert('No address available for input: \'' + place.name + '\'');
                    return;
                }
                // Recenter the map to the selected address
                originLocation = place.geometry.location();
                map.setCenter(originLocation);
                map.setZoom(9);
                console.log(place);

                originMarker.setPosition(originLocation);
                originMarker.setVisible(true);

                // Use the selected address as the origin to calculate distances
                // to each of the store locations
                const rankedStores = await calculateDistances(map.data, originLocation);
                showStoresList(map.data, rankedStores);

                return;

            });


        })
        .catch(error => {
            console.log(error);
        });
}

async function calculateDistances(data, origin) {
    const stores = [];
    const destination = [];

    // Build parallel arrays for the store IDs and destinations
    data.forEach((store) => {
        const storeNum = store.getProperty('storeid');
        const storeLoc = store.getGeometry().get();

        stores.push(storeNum);
        destination.push(storeLoc);
    });


    // Retrieve the distances of each store from the origin
    // The returned list will be in the same order as the destinations list
    const service = new google.maps.DistanceMatrixService();
    const getDistanceMatrix = (service, parameters) => new Promise((resolve, reject) => {
        service.getDistanceMatrix(parameters, (response, status) => {
            if (status != google.maps.DistanceMatrixStatus.OK) {
                reject(response);
            } else {
                const distances = [];
                const results = response.rows[0].elements;

                for (let j = 0; j < results.length; j++) {
                    const element = results[j];
                    const distanceText = element.distance.text;
                    const distanceVal = element.distance.value;
                    const distanceObject = {
                        storeid: stores[j],
                        distanceText: distanceText,
                        distanceVal: distanceVal,
                    };
                    distances.push(distanceObject);
                }
                resolve(distances);
            }
        });
    });
    const distanceList = await getDistanceMatrix(service, {
        origins: [origin],
        destinations: destinations,
        travelMode: 'DRIVING',
        unitSystem: google.maps.UnitSystem.METRIC,
    });

    distanceList.sort((first, second) => {
        return first.distanceVal - second.distanceVal;
    });

    return distanceList;
}


function showStoresList(data, stores) {
    if (stores.length == 0) {
        console.log('empty stores');
        return;
    }

    let panel = document.createElement('div');
    // If the panel already exists, use it. Else, create it and add to the page.
    if (document.getElementById('panel')) {
        panel = document.getElementById('panel');

        // If panel is already open, close it
        if (panel.classList.contains('open')) {
            panel.classList.remove('open');
        }
    } else {
        panel.setAttribute('id', 'panel');
        const body = document.body;
        body.insertBefore(panel.body.childNodes[0]);
    }

    // Clear the previous details
    while (panel.lastChild) {
        panel.removeChild(panel.lastChild);
    }

    stores.forEach((store) => {
        // Add store details with text formatting
        const name = document.createElement('p');
        name.classList.add('place');

        const currentStore = data.getFeatureById(store.storeid);
        name.textContent = currentStore.getProperty('name');
        panel.appendChild(name);

        const distanceText = document.createElement('p');
        distanceText.classList.add('distanceText');
        distanceText.textContent = store.distanceText;
        panel.appendChild(distanceText);
    });

    // Open the panel
    panel.classList.add('open');

    return;
};
