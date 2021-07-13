$(document).ready(function(){
    console.log("Se hizo correctamente1")
    if (navigator.geolocation){
      console.log("Navegación correctamente")
      navigator.geolocation.getCurrentPosition(showPosition);
    }else{
      console.log("Navegación erronea")
    }
    function showPosition(position){
      var latitud = (position.coords.latitude);
      var longitud = (position.coords.longitude);

      var url = "https://www.metaweather.com/api/location/search/?lattlong=";
      var urlpos = `${url}${latitud},${longitud}`;
      $.get(urlpos,function(data){
        console.log(data);
      }).then (function(data){
      var newurl = `https://www.metaweather.com/api/location/${data[0].woeid}`;
      var ciudad = (data[0].title);
      console.log (newurl);
        $.get(newurl,function(data){
          console.log(data);
          console.log(data.consolidated_weather[0].weather_state_name);
          console.log(data.consolidated_weather[0].the_temp);
          console.log(data.consolidated_weather[0].weather_state_abbr);
          var clima = (data.consolidated_weather[0].weather_state_name);
          if (clima == "Heavy Cloud"){
            var clima = "Gran Nubosidad"
          }
          else if (clima == "Light Cloud"){
            var clima = "Nubosidad Parcial"
          }
          else if (clima == "Clear"){
            var clima = "Despejado"
          }
          else if (clima == "Snow"){
            var clima = "Nevando"
          }
          else if (clima == "Sleet"){
            var clima = "Agua Nieve"
          }
          else if (clima == "Hail"){
            var clima = "Granizando"
          }
          else if (clima == "Thunderstorm"){
            var clima = "Tormenta Electrica"
          }
          else if (clima == "Heavy Rain"){
            var clima = "Precipitaciones"
          }
          else if (clima == "Light Rain"){
            var clima = "Llovizna"
          }
          else if (clima == "Showers"){
            var clima = "Chubasco"
          }
          var temp = (data.consolidated_weather[0].the_temp);
          var state = (data.consolidated_weather[0].weather_state_abbr);
          console.log(clima);
          var newurl = `https://www.metaweather.com/static/img/weather/ico/${state}.ico`;
          console.log(newurl);
          var tiempo =     `<div class="col-6 col-md">
                              <h6>Tiempo</h6>
                                <ul class="list-unstyled text-small">
                                  <li>Ciudad: ${ciudad}</li>
                                  <li>Temperatura: ${temp}</li>
                                  <li> Clima: ${clima}</li>
                                  <li><img src=" ${newurl}"></></li>
                                </ul>
                            </div>`
          $("#ContenedorTiempo").append(tiempo)
        })
      })
    }
  })