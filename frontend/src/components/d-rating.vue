<template>
<div>
  <!--v-rating
    v-model="rating"
    class="d-rating">
    <d-icon
      slot-scope="props"
      slot="item"
      color="#ffeb3b"
      scale="1.25"
      @click="props.click"
      :name=" props.rating ? 'b-star' : 'b-star-o' "/>
  </v-rating-->
</div>
</template>

<style lang="less">

</style>

<script>
export default {
  name: 'd-rating',
  data () {
    return {
      rating: 5
    }
  }
}
</script>
