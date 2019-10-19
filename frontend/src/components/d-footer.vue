<template>
  <v-footer
    class="d-footer"
    height="auto">
    <v-container
      px-5
      class="footer__container">
      <v-layout
        row
        wrap>
        <v-flex md12>
          <v-layout row wrap>
            <v-flex md2 xs12 mb-2>
              <span class="mr-2">¡SUSCRÍBETE A QUIMDER!</span>
            </v-flex>
            <v-flex md6 xs12>
              <v-form ref="form" v-model="valid" lazy-validation class="mr-2">
                <v-text-field
                  class="ma-0 border-radius"
                  v-model="email"
                  :rules="emailRules"
                  label="Correo Electrónico"
                  solo
                  required/>
                <v-layout row wrap align-center>
                  <v-flex shrink>
                    <v-checkbox
                      class="mt-2"
                      v-model="checkbox"
                      :rules="[v => !!v]"
                      required/>
                  </v-flex>
                  <v-flex>
                    Acepto
                    <router-link
                      v-if="pages && pages.legal"
                      class="text--no-recoration"
                      :to="{
                        name: links.pages,
                        params: {
                          slug: pages.legal
                        }
                      }">
                      términos y condiciones
                    </router-link>
                    <template v-else>
                      términos y condiciones
                    </template>
                  </v-flex>
                </v-layout>
              </v-form>
            </v-flex>
            <v-flex md4 xs12>
              <v-btn
                class="d-btn d-btn--rounded my-0"
                block
                dark
                depressed
                color="accent"
                @click="submit">
                RECIBE NUESTRAS OFERTAS
              </v-btn>
            </v-flex>
            <!--v-flex md5 xs12>
              <v-layout row justify-space-between>
                <v-flex md6 xs6 mr-2>
                  <v-btn
                    class="my-0"
                    color="grey darken-4"
                    block
                    dark
                    depressed
                    @click="submit"
                  >
                    OFERTA PARA HOMBRES
                  </v-btn>
                </v-flex>
                <v-spacer></v-spacer>
                <v-flex md6 xs6>
                  <v-btn
                    class="my-0"
                    color="grey darken-4"
                    block
                    dark
                    depressed
                    @click="submit"
                  >
                    OFERTA PARA MUJERES
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-flex-->
          </v-layout>
        </v-flex>
        <v-flex xs12 hidden-sm-and-down>
          <v-container fluid>
            <v-layout row wrap>
              <v-flex xs3 px-1 v-for="(infoItem, i) in footer.infoItem" :key="i">
                <h3 class="mb-3">{{ infoItem.title }}</h3>
                <v-flex mb-2 v-for="(item, i) in infoItem.list" :key="i">
                  <a href="" class="black--text" style="text-decoration:none;">{{ item.item }}</a>
                </v-flex>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<style lang="less">
.d-footer {
  .v-text-field {
    .v-input__control {
      min-height: 36px;
      .v-input__slot {
        margin: 0;
        box-shadow: none !important;
        height: 36px;
        input {
          font-size: 14px;
          line-height: 14px;
        }
      }
      .v-text-field__details {
        display: none;
      }
    }
  }
  .v-input--checkbox {
    .v-input__slot {
      margin: 0 !important;
    }
    .v-input--selection-controls__input {
      width: 18px;
      .v-icon.material-icons.theme--light {
        color: transparent;
        background-color: white;
        width: 16px;
        height: 16px;
        border-radius: 2px;
        margin-top: 4px;
      }
    }
  }
  .terms-label {
    text-decoration: none;
    color: inherit;
    &:hover {
      color: #f58220;
    }
  }
  @media only screen and (max-width: 960px) {
    .footer__container {
      padding-left: 24px !important;
      padding-right: 24px !important;
    }
  }

  @media only screen and (max-width: 600px) {
    .footer__container {
      padding-left: 16px !important;
      padding-right: 16px !important;
      label {
        font-size: 12px !important;
      }
      .v-btn {
        font-size: 12px !important;
      }
    }
  }
}
</style>

<script>
import { PAGE_DETAIL } from '@/router/pages'

export default {
  name: 'd-footer',
  data () {
    return {
      links: {
        pages: PAGE_DETAIL
      },
      pages: null,

      valid: null,
      email: null,
      emailRules: [],
      checkbox: false,
      footer: {
        infoItem: {
          1: {
            title: 'Conócenos',
            list: [
              { item: 'Productos' },
              { item: 'Blog' },
              { item: 'Acerca de' },
              { item: 'Relaciones con invercionistas' },
              { item: 'Dispositivos' }
            ]
          },
          2: {
            title: 'Gana dinero con nosotros',
            list: [
              { item: 'Vende con nosotros' },
              { item: 'Vende tus servicios' },
              { item: 'Vende tus aplicaciones' },
              { item: 'Conviértase en un afiliado' },
              { item: 'Anuncie sus productos' },
              { item: 'Autoedición con nosotros' },
              { item: 'Ver todo >>' }
            ]
          },
          3: {
            title: 'Productos de Pago',
            list: [
              { item: 'Pago con efectivo' },
              { item: 'Tarjetas de la tienda' },
              { item: 'Línea de crédito corporativo' },
              { item: 'Compre con puntos' },
              { item: 'Recarga tu saldo' },
              { item: 'Conversor de crédito' }
            ]
          },
          4: {
            title: 'Déjanos ayudarte',
            list: [
              { item: 'Tu cuenta' },
              { item: 'Tus órdenes' },
              { item: 'Tarifa y política de envío' },
              { item: 'Devolución y reembolso' },
              { item: 'Administre su contenido' },
              { item: 'Asistente de productos' },
              { item: 'Ayuda' }
            ]
          }
        }
      }
    }
  },
  methods: {
    submit () {}
  },
  created () {
    let pages = document.querySelector('[name="meta-pages"]')
    if (pages) {
      this.pages = JSON.parse(pages.content)
    }
  }
}
</script>
