<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar>
      Planeación por áreas
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Planeación por áreas" icon="ballot">
                <div >
            <canvas ref="jPolygon" width="640" height="480" style="cursor:crosshair"
              data-imgsrc="https://images.squarespace-cdn.com/content/v1/557663e3e4b0dbb60c7d8c5e/1537894737858-3VX3YEEXGY1HMZYYELYM/ke17ZwdGBToddI8pDm48kAnkJg-YzxtCygogjUK3bbh7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0nafa6-LSz8qNVVJSth8ciCFH6we3r-KDuPDypPpS-KbkuaghfxlWIaIzffUae6kXw/MapIsolated_2018.png?format=60000w"
              v-on:mousedown="mouseDownHandler" v-on:contextmenu="contextMenuHandler">
                Your browser does not support the HTML5 canvas tag.
            </canvas>
        </div>
        <div >
            <div>
                <button v-on:click="handlerEventMap">Undo</button>
                <button v-on:click="handlerEventMap">Clear</button>
                <p>Press <strong>Left Click</strong> to draw a point.</p>
                <p><strong>CTRL+Click</strong> or <strong>Right Click</strong> to close the polygon.</p>
            </div>
        </div>
        <div>
          <p><strong>Coordinates:</strong></p>
        </div>
      </card-component>
      <card-component>
        <!-- <div v-for="point in perimeter" :key="point.x">point: {{ point }} </div> -->
      </card-component>
    </section>
  </div>
</template>

<script>
import checkIntersect from '@/assets/jPolygon'
import CardComponent from '@/components/CardComponent'
// @ is an alias to /src
const TitleBar = () => import(/* webpackChunkName: "titlebar" */ '@/components/TitleBar')
const HeroBar = () => import(/* webpackChunkName: "herobar" */ '@/components/HeroBar')

export default {
  name: 'AreaPlanning',
  components: { HeroBar, CardComponent, TitleBar },
  data () {
    return {
      isLoading: false,
      canvas: null,
      perimeter: [],
      complete: false,
      ctx: null
    }
  },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Planeacion por área'
      ]
    }
  },
  methods: {
    undo: function (event) {
      // let ctx = undefined
      this.perimeter.pop()
      this.complete = false
      this.start(true)
    },
    clear_canvas: function (event) {
      // ctx = undefined;
      this.complete = false
      this.perimeter = []
      let canvas = this.$refs.jPolygon
      let img = new Image()
      img.src = canvas.getAttribute('data-imgsrc')
      let ctx = canvas.getContext('2d')
      img.addEventListener('load', function () {
        console.log({ img })
        console.log(this)
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
      }, false)
    },
    mouseDownHandler: function (event) {
      console.log({ event })
      if (this.complete) {
        alert('Polygon already created')
        return false
      }
      let rect, x, y
      if (event.ctrlKey || event.which === 3 || event.button === 2) {
        if (this.perimeter.length === 2) {
          alert('You need at least three points for a polygon')
          return false
        }
        x = this.perimeter[0]['x']
        y = this.perimeter[0]['y']
        console.log('first')
        if (checkIntersect(x, y)) {
          console.log('The line you are drowing intersect another line')
          return false
        }
        console.log('second')
        this.draw(true)
        alert('Polygon closed')
        event.preventDefault()
        return false
      } else {
        let canvas = this.$refs.jPolygon
        console.log('berlin')
        rect = canvas.getBoundingClientRect()
        console.log('paris')
        x = event.clientX - rect.left
        y = event.clientY - rect.top
        console.log('london')
        console.log({ x, y })
        if (this.perimeter.length > 0 && x === this.perimeter[this.perimeter.length - 1]['x'] && y === this.perimeter[this.perimeter.length - 1]['y']) {
          // same point - double click
          return false
        }
        console.log('prague')
        console.log({ checkIntersect })
        if (checkIntersect.checkIntersect(x, y, this.perimeter)) {
          alert('The line you are drowing intersect another line')
          return false
        }
        console.log('rome')
        this.perimeter.push({ x, y })
        console.log('buda')
        this.draw(false)
        console.log('minsk')
        return false
      }
    },
    contextMenuHandler (event) {
      return false
    },
    point: function (x, y) {
      let canvas = this.$refs.jPolygon
      let img = new Image()
      img.src = canvas.getAttribute('data-imgsrc')
      let ctx = canvas.getContext('2d')
      ctx.fillStyle = 'white'
      ctx.strokeStyle = 'white'
      ctx.fillRect(x - 2, y - 2, 4, 4)
      ctx.moveTo(x, y)
    },
    start: function (withDraw) {
      console.log('doing start stuff')
      let canvas = this.$refs.jPolygon
      let img = new Image()
      img.src = canvas.getAttribute('data-imgsrc')
      let ctx = canvas.getContext('2d')
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
      if (withDraw === true) {
        this.draw(false)
      }
    },
    draw: function (end) {
      let canvas = this.$refs.jPolygon
      let img = new Image()
      img.src = canvas.getAttribute('data-imgsrc')
      let ctx = canvas.getContext('2d')
      ctx.lineWidth = 1
      ctx.strokeStyle = 'white'
      ctx.lineCap = 'square'
      ctx.beginPath()
      for (var i = 0; i < this.perimeter.length; i++) {
        if (i === 0) {
          ctx.moveTo(this.perimeter[i]['x'], this.perimeter[i]['y'])
          end || this.point(this.perimeter[i]['x'], this.perimeter[i]['y'])
        } else {
          ctx.lineTo(this.perimeter[i]['x'], this.perimeter[i]['y'])
          end || this.point(this.perimeter[i]['x'], this.perimeter[i]['y'])
        }
      }
      if (end) {
        ctx.lineTo(this.perimeter[0]['x'], this.perimeter[0]['y'])
        ctx.closePath()
        ctx.fillStyle = 'rgba(255, 0, 0, 0.5)'
        ctx.fill()
        ctx.strokeStyle = 'blue'
        this.complete = true
      }
      ctx.stroke()
    }
  },
  mounted: function () {
    console.log('created')
    let canvas = this.$refs.jPolygon
    let img = new Image()
    img.src = canvas.getAttribute('data-imgsrc')
    let ctx = canvas.getContext('2d')
    img.addEventListener('load', function () {
      console.log({ img })
      console.log(this)
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
    }, false)
  }
}
</script>
