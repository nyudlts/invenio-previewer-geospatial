import L from "leaflet"
import 'leaflet-gpx';
import "leaflet/dist/leaflet.css";

document.addEventListener("DOMContentLoaded", () => {
  const mapElement = document.getElementById("map");
  const gpxFileUri = mapElement.getAttribute("data-file-uri")
  const gpxUrl = new URL(gpxFileUri, window.location.href);

  const map = L.map('map').setView([0, 0], 13);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);

  new L.GPX(gpxUrl.href, {
    async: true,
    gpx_options: {
      parseElements: ['track', 'route']
    },
    markers: {
      // TODO: Figure out how to display stock images from leaflet-gpx
      startIcon: null,
      endIcon: null
    }
  }).on('loaded', (e) => {
    map.fitBounds(e.target.getBounds());
  }).addTo(map);
});
