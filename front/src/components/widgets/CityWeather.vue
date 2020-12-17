<template>
  <div class="city_weather">
    <h1>City : {{ params.name }}</h1>
    Temperature : {{ temperature }} °C
    <br />
    Wind speed : {{ wind_speed }} km/h
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CityWeather",
  props: {
    params: Object,
  },
  data() {
    return {
      temperature: "",
      wind_speed: "",
    }
  },
  methods: {
    async fetchWeather() {
      const response = await axios
        .get(
          `https://api.openweathermap.org/data/2.5/weather?q=${this.params.name}&appid=b44ef639cb05793bbaa9f8e8497e9225&units=metric`
        )
        .then((res) => {
          return res;
        });
      this.temperature = response.data.main.temp;
      this.wind_speed = response.data.wind.speed;
    },
  },
  created() {
    this.fetchWeather();
  },
};
</script>
