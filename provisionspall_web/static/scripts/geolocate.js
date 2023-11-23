if ('geolocation' in navigator) {
    console.log("geolocation is enabled");
    navigator.geolocation.watchPosition((position) => {
        let latitude = position.coords.latitude;
        let longitude = position.coords.longitude;

        let map = L.map('map').setView([latitude, longitude], 13);

        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        
        //we add marker to identify current location
        L.marker([latitude, longitude]).addTo(map);

        //We add Routing controls which is a plugin to give direction from users current
        // location to business area
        let businessLatitude =  latitude + 0.01;
        let businessLongitude = longitude + 0.01;
        L.Routing.control({
                waypoints: [
                    L.latLng(longitude, longitude),
                    L.latLng(businessLatitude, businessLongitude)
                ],
                routeWhileDragging: true
        }).addTo(map);

        
    }, (error) => {
        console.error('Error getting location', error.message);
    }, { enableHighAccuracy: true });
} else {
    console.log("Geolocation not enabled!")
}
