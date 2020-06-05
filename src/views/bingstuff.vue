<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar>
      Planeación por definición de ruta
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Planeación por definición de ruta" class="bmap">
        <bing-map :credentials="mapCredentials" :options="mapOptions" v-if="mapVisible">
        <bing-map-layer name="activeFlightsLayer"
                        v-on:layer-click="handleEvent"
                        v-on:layer-mouseover="showTooltip"
                        v-on:layer-mouseout="hideTooltip"
                        :visible="pinsVisible">
            <bing-map-pushpin v-for="item in pins" :metadata="item.metadata"
            :location="item.location" :options="item.options" :key="item.key"></bing-map-pushpin>
            <!-- <bing-map-infobox :options="tooltip">
                <div class="customInfobox">{{tooltip.description}}</div>
            </bing-map-infobox> -->
        </bing-map-layer>
        </bing-map>
      </card-component>
    </section>
  </div>

</template>

<script>
import CardComponent from '@/components/CardComponent'
import TitleBar from '@/components/TitleBar'
import HeroBar from '@/components/HeroBar'
export default {
  name: 'Tables',
  components: { HeroBar, TitleBar, CardComponent },
  data: function () {
    return {
      mapOptions: {
        zoom: 13,
        center: {
          latitude: 3.37995482366928,
          longitude: -76.5272338699882
        }
      },
      mapCredentials: 'Aqi5alIcpuMyeuu7-YIeT08W_MUQxVQzmuDPeLXuU0pWYD4HIA-Oyy27EEOGUPBA',
      mapVisible: true,
      pinsVisible: true,
      pins: [
        {
          key: 'Home',
          location: {
            latitude: 3.37995482366928,
            longitude: -76.5272338699882
          },
          options: {
            title: 'Home',
            visible: true
          }
        },
        {
          key: 'pin2',
          location: {
            latitude: 39.950806,
            longitude: -77.770620
          },
          options: {
            title: 'pin 2',
            visible: true
          }
        }
      ]
    }
  },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Planeacion por ruta'
      ]
    }
  },
  methods: {
    showTooltip: function (eventst) {
      console.log({ eventst })
    },
    hideTooltip: function (eventht) {
      console.log({ eventht })
    },
    handleEvent: function (evently) {
      console.log({ evently })
    },
    mapclickHandler: function (event) {
      console.log({ event })
    },
    moverHandler: function (emover) {
      console.log({ emover })
    },
    rightclickHandler: function (rightclick) {
      console.log({ rightclick })
    }
  }
}
</script>

<style>
.customInfobox {
    background-color: rgba(0,0,0,0.5);
    color: white;
    max-width: 200px;
    border-radius: 10px;
    padding: 10px;
    font-size:12px;
    pointer-events:auto !important;
}
.bmap {
  width: 550px;
  height: 300px;
}
</style>
