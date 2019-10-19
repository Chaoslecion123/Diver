<template>
  <v-layout class="d-category-filter">
    <v-list class="filter-list pa-0" expand>

      <v-list-group
        v-for="(box, i) in filterListBox"
        v-model="box.active"
        :key="i">

        <v-list-tile
          slot="activator">
          <v-list-tile-content>
            <v-list-tile-title >{{ box.filterTitle }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile
          v-for="(filter, i) in box.items"
          :key="i">
          <template
            v-if="box.type == 'checkbox'">
            <v-list-tile-action>
              <v-checkbox
                hide-details/>
            </v-list-tile-action>
            <v-list-tile-content class="body-1">
              <v-layout
                style="width:100%"
                row wrap align-center>
                <v-flex>{{ filter.option }}</v-flex>
                <v-flex class="filter-quantity" shrink>{{ filter.quantity }}</v-flex>
              </v-layout>
            </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'color'">
              <v-list-tile-content class="ma-0">
                <v-icon :color="filter.color">fiber_manual_record</v-icon>
              </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'size'">
            <v-list-tile-content class="ma-0">
              <v-chip text-color="black">{{ filter.size }}</v-chip>
            </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'slider'">
            <v-list-tile-content class="ma-0">
              <v-layout row wrap justify-space-between>
                <v-flex xs12 class="px-3">
                  <v-range-slider
                    v-model="range"
                    :max="filter.max"
                    :min="filter.min"></v-range-slider>
                </v-flex>
                <v-flex xs5
                  shrink
                  style="width: 60px">
                  <v-text-field
                    v-model="range[0]"
                    class="input__number ma-0 pa-0"
                    hide-details
                    solo
                    flat
                    single-line
                    type="number"></v-text-field>
                </v-flex>
                <v-flex xs5
                  shrink
                  style="width: 60px">
                  <v-text-field
                    v-model="range[1]"
                    class="input__number ma-0 pa-0"
                    hide-details
                    solo
                    flat
                    single-line
                    type="number"></v-text-field>
                </v-flex>
              </v-layout>
            </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'discounts.checkbox'">
            <v-list-tile-action>
              <v-checkbox></v-checkbox>
            </v-list-tile-action>
            <v-list-tile-content class="body-1">
              <v-layout
                style="width:100%"
                row wrap align-center>
                <v-flex>{{ filter.option }}</v-flex>
                <v-flex class="filter-quantity" shrink>{{ filter.quantity }}</v-flex>
              </v-layout>
            </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'featured.checkbox'">
            <v-list-tile-action>
              <v-checkbox></v-checkbox>
            </v-list-tile-action>
            <v-list-tile-content class="body-1">
              <v-layout
                style="width:100%"
                row wrap align-center>
                <v-flex>{{ filter.option }}</v-flex>
                <v-flex class="filter-quantity" shrink>{{ filter.quantity }}</v-flex>
              </v-layout>
            </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'freeShipping'">
            <v-list-tile-content
              style="height:60px;"
              class="body-1">
                <v-layout
                  style="width: 100%;"
                  row wrap align-center>
                  <v-flex grow> Envío gratuito </v-flex>
                  <v-flex shrink>
                    <v-switch
                      hide-details
                      color="#F58220"/>
                  </v-flex>
                </v-layout>
            </v-list-tile-content>
          </template>

          <template
            v-if="box.type == 'ranking'">
            <v-list-tile-content
              style="height:60px;"
              class="body-1">
              <v-layout
                style="width: 100%;"
                row wrap align-center>
                <v-flex>
                  <v-rating
                    v-model="rating"
                    class="d-rating d-inline-block">
                    <v-icon
                      class="pa-0"
                      slot="item"
                      slot-scope="props"
                      color="#000">
                      {{ props.isFilled ? 'star' : 'star_border' }}
                    </v-icon>
                  </v-rating>
                  <v-flex
                    ml-2
                    style="display: inline-block; font-size: 0.875rem;">
                    o más
                  </v-flex>
                </v-flex>
                <v-flex shrink>
                  <v-switch
                    hide-details
                    color="#F58220"/>
                </v-flex>
              </v-layout>
            </v-list-tile-content>
          </template>

        </v-list-tile>

      </v-list-group>
    </v-list>
  </v-layout>
</template>

<style lang="less">
.filter-list {
  .filter-quantity {
    padding: 0 8px;
    border-radius: 10px;
    background: #e8e8e8;
    color: #747474;
    font-size: 0.875rem;
    line-height: 1.35rem;
  }
  .v-list__group {
    margin: 8px 0;
    border-radius: 4px;
    background-color: #f5f5f5;
    &:nth-child(5), &:nth-child(6) {
      .v-list__group__items {
        padding: 8px;
        display: flex;
        flex: 1 1 auto;
        flex-direction: row;
        min-width: 0;
        flex-wrap: wrap;
        >div {
          .v-list__tile {
            padding: 0 12px;
            .v-list__tile__content {
              align-items: center;
              cursor: pointer;
            }
          }
        }
      }
    }
    &:nth-child(7) {
      .v-list__group__items{
        .v-list__tile{
          padding: 0 16px 8px 16px;
          height: auto !important;
          .v-input--slider {
            margin: 0 0 12px 0;
            .v-slider__track__container {
              height: 8px !important;
              border-radius: 64px;
            }
            .v-slider__track, .v-slider__track-fill {
              height: 8px !important;
              border: 1px solid #000 !important;
            }
            .v-slider__thumb {
              border: 1px solid #000 !important;
              width: 24px !important;
              height: 24px !important;
            }
            .v-input__control {
              .v-input__slot {
                margin:0;
              }
              .v-messages {
                display:none;
              }
            }
          }
          .input__number {
            .v-input__slot {
              border: 1px solid black;
              border-radius: 4px;
              min-height: 24px !important;
              height: 24px !important;
              input {
                padding: 4px 0;
              }
            }
          }
        }
      }
    }
    &:nth-child(10), &:nth-child(11) {
      display: none;
    }
    &__header {
      &__append-icon {
        position: absolute;
        right: 8px;
        padding: 0;

        i {
          font-size: 2.29rem;
          color: #000000;
        }
      }
      &:hover {
        background-color: transparent !important;
      }
    }
    &::before {
      display: none;
    }
    &__items {
      padding-bottom: 8px ;
      .v-list__tile {
        height:36px;
        .v-input--switch {
          padding: 0;
          margin: 0;
          .v-input__slot {
            margin:0;
          }
        }
        .v-list__tile__action {
          min-width: 36px;
          .v-input--checkbox {
            .v-input__slot {
              height: auto !important;
              min-height: auto !important;
              margin: 0 !important;
              .v-input--selection-controls__input {
                margin: 0 !important;
              }
            }
          }
        }
      }
    }
    @media only screen and (max-width: 960px) {
      padding: 0 8px !important;
      margin: 0;
      background-color: #fff;
      &:nth-child(10) {
        display: block;
        margin: 8px 0;
        .v-list__group__header {
          display: none;
        }
      }
      &:nth-child(11) {
        display: block;
      }
      .v-list__group__header {
        pointer-events: none;
        .v-list__tile__title {
          font-weight: 600;
        }
        &__append-icon {
          display: none;
        }
      }
      .v-list__group__items {
        .v-list__tile__action {
          order: 2;
          .v-input {
            position: absolute;
            right: 0;
            margin-right: 16px;
          }
        }
      }
      &--active:after, &--active:before {
        background: #fff !important;
      }
    }
  }
  input[type=number]::-webkit-inner-spin-button,
  input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  .theme--light.v-list .v-list__group--active:after, .theme--light.v-list .v-list__group--active:before {
    background: none;
  }
}
</style>

<script>
export default {
  name: 'd-category-filter',
  data () {
    return {
      panel: [true, true, true, true, true],
      range: [0, 1000],
      rating: 4,
      ex11: ['red'],
      filterListBox: [
        {
          active: true,
          filterTitle: 'SEXO',
          type: 'checkbox',
          items: [
            { option: 'Hombre', quantity: '1,657' },
            { option: 'Mujer', quantity: '26,086' }
          ]
        },
        {
          active: true,
          filterTitle: 'EDADES',
          type: 'checkbox',
          items: [
            { option: '0-4 años', quantity: '250' },
            { option: '4-8 años', quantity: '250' },
            { option: '8-16 años', quantity: '250' }
          ]
        },
        {
          active: true,
          filterTitle: 'CATEGORÍA',
          type: 'checkbox',
          items: [
            { option: 'Calzado', quantity: '250' },
            { option: 'Bolsos', quantity: '235' },
            { option: 'Zapatillas', quantity: '186' },
            { option: 'Accesorios', quantity: '276' },
            { option: 'Blusas', quantity: '128' }
          ]
        },
        {
          active: true,
          filterTitle: 'MARCA',
          type: 'checkbox',
          items: [
            { option: 'Adidas', quantity: '546' },
            { option: 'Nike', quantity: '96' },
            { option: 'Bata', quantity: '154' }
          ]
        },
        {
          active: true,
          filterTitle: 'COLORES',
          type: 'color',
          items: [
            { color: 'green' },
            { color: 'brown' },
            { color: 'red' },
            { color: 'yellow' },
            { color: 'blue' },
            { color: 'purple' },
            { color: 'orange' },
            { color: 'cyan' }
          ]
        },
        {
          active: true,
          filterTitle: 'TALLAS',
          type: 'size',
          items: [
            { size: 'XS' },
            { size: 'S' },
            { size: 'M' },
            { size: 'L' },
            { size: 'XL' },
            { size: 'XXL' }
          ]
        },
        {
          active: true,
          filterTitle: 'PRECIOS',
          type: 'slider',
          items: [
            { min: 0, max: 1000 }
          ]
        },
        {
          active: true,
          filterTitle: 'DESCUENTOS',
          type: 'discounts.checkbox',
          items: [
            { option: '10%', quantity: '6' },
            { option: '40%', quantity: '2' },
            { option: '70%', quantity: '3' }
          ]
        },
        {
          active: true,
          filterTitle: 'DESTACADOS',
          type: 'featured.checkbox',
          items: [
            { option: 'Puntuación', quantity: '6' },
            { option: 'Más vendidos', quantity: '2' },
            { option: 'Ofertas', quantity: '3' }
          ]
        },
        {
          active: true,
          filterTitle: null,
          type: 'freeShipping',
          items: ['']
        },
        {
          active: true,
          filterTitle: 'Ranking',
          type: 'ranking',
          items: ['']
        }
      ]
    }
  }
}
</script>
