import L from "leaflet"
import "leaflet/dist/leaflet.css";

document.addEventListener("DOMContentLoaded", () => {
  const mapElement = document.getElementById("map");
  const baseUrl = mapElement.getAttribute("data-base-url")
  const layerName = mapElement.getAttribute("data-layer-name")

  const map = L.map('map').setView([51.505, -0.09], 13);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);

  const wmsLayer = L.tileLayer.wms(baseUrl, {
    layers: layerName,
    format: 'image/png',
    transparent: true
  });

  wmsLayer.addTo(map);
  wmsLayer.setOpacity(0.75);
  map.fitBounds([
    [17.881242, -179.14734],
    [71.390482, 179.778465]
  ])
});
