<template>
  <v-content class="terms-and-conditions">
    <v-container py-5 px-0 fluid>
      <v-layout row wrap class="section">
        <v-flex xs12 md2
          class="terms-column">
          <v-card
            flat
            pa-3
            v-for="(item,i) in policies" :key="i"
            color="grey lighten-3">
            <v-card-title class="pa-2 font-weight-600 text-uppercase">{{item.title}}</v-card-title>
            <v-card-text class="pa-0">
              <v-list>
                <v-list-tile v-for="(item,i) in item.subtitles" :key="i">
                  {{item}}
                </v-list-tile>
              </v-list>
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex xs12 md10 pl-5>
          <h2 class="text-uppercase">Términos &amp; condiciones</h2>
          <v-divider class="mb-3"></v-divider>
          <span class="terms-content">{{text}}</span>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<style lang="less">
.terms-and-conditions {
  .terms-column {
    .v-list {
      background-color: #eee!important;
      border-color: #eee!important;
      &__tile {
        height: 36px;
      }
    }
  }
  .terms-content {
    line-height: 1.75rem;
  }
}
</style>

<script>
export default {
  name: 'Policies',
  data () {
    return {
      policies: {
        1: {
          title: 'Test 1',
          subtitles: [
            'subtitle1', 'subtitle2', 'subtitle3', 'subtitle4'
          ]
        },
        2: {
          title: 'Test 2',
          subtitles: [
            'subtitle1', 'subtitle2', 'subtitle3', 'subtitle4'
          ]
        },
        3: {
          title: 'Test 3',
          subtitles: [
            'subtitle1', 'subtitle2', 'subtitle3', 'subtitle4'
          ]
        }
      },
      text: 'El acceso y uso de este sitio web se rige por los "Términos y Condiciones" descritos a continuación, así como por la legislación que se aplique en la República de Perú. En consecuencia, todas las visitas y todos los contratos y transacciones que se realicen en este sitio, como asimismo sus efectos jurídicos, quedarán regidos por estas reglas y sometidas a esta legislación. Los Términos y Condiciones contenidos en este instrumento se aplicarán y se entenderá que forman parte de todos los actos y contratos que se ejecuten o celebren mediante los sistemas de oferta y comercialización comprendidos en este sitio web entre los usuarios de este sitio y Quimder, la cual se denominará en adelante también en forma indistinta como "la empresa", o bien "la empresa oferente", "el proveedor" o "la empresa proveedora", según convenga al sentido del texto. Es requisito para comprar en la Tienda Virtual de Saga Falabella la aceptación de los Términos y Condiciones de ventas descritos a continuación. Cualquier persona que realice una transacción en la Tienda Virtual de Saga Falabella o a través del número telefónico que Quimder destine para tal efecto, declara y reconoce, por el hecho de efectuar la compra, que conoce y acepta todos y cada uno de los Términos y Condiciones descritos a continuación. Se entenderán conocidos y aceptados los Términos y Condiciones por el solo hecho del registro y/o la compra de productos a través de este sitio. Saga Falabella se reserva el derecho de actualizar y/o modificar los Términos y Condiciones que detallamos a continuación en cualquier momento, sin previo aviso. Por esta razón recomendamos revisar los Términos y Condiciones cada vez que utilice este Sitio. Los consumidores quedarán sujetos a los Términos y Condiciones del presente sitio, en el momento en el que envíen su solicitud de compra. Realizaremos nuestros mesjores esfuerzos para asegurar la disponibilidad, sin interrupciones, de los servicios de la presente página web, así como en la ausencia de errores en cualquier transmision deinformación que pudiera tener lugar. No obstante, y debido a la naturaleza misma de internet, no es posible garantizar tales extremos. Asimismo, el acceso a los servicios de la presente página web podría ocasionalmente verse suspendido o restringido a efectos de la realización de trabajos de reparación o mantenimiento, o la introducción de nuevos productos o servicios. Procuraremos limitar la frecuencia y duración de tales suspensiones o restricciones. A continuación detallamos los Términos y Condiciones:'
    }
  }
}
</script>
