<template>
  <v-pagination
    class="d-old-pagination"
    v-model="page"
    :length="15"
    :total-visible="5"></v-pagination>
</template>

<style lang="less">
.d-old-pagination {
  &.v-pagination {
    .v-pagination__item {
      box-shadow: none;
      font-weight: 600;
      background: transparent;
      margin: 0.2rem !important;
      @media screen and (max-width: 960px) {
        min-width: 32px;
        height: 32px;
      }
      &:focus {
        background-color: #fcb814 !important;
        outline: none;
      }
    }
    .v-pagination__item.v-pagination__item--active.primary {
      background-color: #fcb814 !important;
      border-color: #fcb814 !important;
    }
    .v-pagination__navigation {
      background: #212121 !important;
      .v-icon {
        color: #fff !important;
        font-size: 2rem;
      }
      @media screen and (max-width: 960px) {
        background: transparent !important;
        .v-icon {
          color: #000 !important;
        }
      }
    }
  }
}
</style>

<script>
export default {
  name: 'd-pagination',
  data () {
    return {
      page: 1
    }
  }
}
</script>
