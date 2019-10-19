<template>
  <div v-if="brand" class="brand-badge">
    <div
      class="brand-badge__color-mark"
      :style="{ background: `${brand.color}` }"/>
    <small class="brand-badge__name grey--text text--darken-2">
      {{ brand.name }}
    </small>
  </div>
</template>

<style lang="less">
.brand-badge {
  height: 16px;
  line-height: 16px;
  margin-bottom: 8px;

  .brand-badge__color-mark {
    vertical-align: top;
    height: 16px;
    width: 16px;
    display: inline-block;
    border-radius: 50%;
    border: 1px solid #212121;
    margin-right: 8px;
  }
  .brand-badge__name {
    vertical-align: top;
    height: 16px;
    line-height: 16px;
    display: inline-block;
  }
}
</style>

<script>
export default {
  name: 'd-brand-badge',
  props: {
    brand: {
      type: Object,
      default: null
    }
  }
}
</script>
