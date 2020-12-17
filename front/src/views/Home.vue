<template>
  <div class="home">
    <CityWeather v-for="widget in widgets" v-bind:key=widget.id v-bind:params=widget.params />
  </div>
</template>

<script>
import CityWeather from "@/components/widgets/CityWeather.vue";
import axios from 'axios'

export default {
  name: "Home",
  components: {
    CityWeather,
    Youtube,
    Twitter
  },
  data() {
    return {
      widgets: []
    }
  },
  methods: {
    async fetchWidgets() {
      this.widgets = await axios.get("http://127.0.0.1:5000/widgets").then(res => {
        return res.data
      })
    }
  },
  created() {
    this.fetchWidgets()
  }
};
</script>
