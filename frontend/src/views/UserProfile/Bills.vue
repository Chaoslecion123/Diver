<template>
  <v-flex
    xs12 md10 pl-3
    style="font-size:14px;"
    class="remove-padding">
    <v-card
      class="py-2 px-3 mb-3"
      flat
      color="grey lighten-4">
      <v-layout row wrap align-center>
        <v-flex
          xs8
          style="font-size:1.25rem;"
          class="font-weight-600">
          Mis Facturas
        </v-flex>
      </v-layout>
    </v-card>

    <v-card flat>
      <v-container grid-list-md pa-0>
        <v-layout row wrap>
          <v-flex xs6 md3 class="settings-card" v-for="(item, i) in bills" :key="i">
            <v-card min-height="164px" class="pa-3 border-radius fill-height" flat color="grey lighten-4">
              <v-container fluid pa-0 grid-list-lg>
                <v-layout row wrap>
                  <v-flex xs10>
                    {{item.name}}
                  </v-flex>
                  <v-flex xs12>
                    {{item.ruc}}
                  </v-flex>
                  <v-flex xs12>
                    {{item.address}}
                  </v-flex>
                  <v-btn :ripple="false" icon absolute class="close-btn">
                    <d-icon class="q-red--text" scale="1.25" name="b-close"/>
                  </v-btn>
                  <v-btn @click="editBill=!editBill" :ripple="false" icon absolute class="edit-btn">
                    <d-icon
                      name="b-edit"/>
                  </v-btn>
                  <d-new-bill-popup v-model="editBill"/>
                </v-layout>
              </v-container>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>

    <v-card flat class="my-3">
        <v-layout row wrap align-center>
          <v-flex xs2 md2 style="font-size:1.5rem;">
            PDF
          </v-flex>
          <v-flex xs10>
            <v-divider style="border-color:#e0e0e0;"/>
          </v-flex>
        </v-layout>
        <v-container px-0 fluid grid-list-xl>
          <v-layout row wrap>
            <v-flex xs6 sm3 md2 v-for="(bill,i) in bills" :key="i">
              <v-card flat class="pa-2 bill-card border-radius">
                <v-card-title class="text-xs-center">
                  <d-icon scale="2.25" name="b-pdffile"/>
                </v-card-title>
                <v-divider style="border-color:#000"/>
                <v-card-actions class="py-0">
                  <v-flex pa-0>
                    {{bill.pdf}}
                  </v-flex>
                  <v-spacer/>
                  <v-flex pa-0 class="text-xs-right">
                    <v-btn
                      style="height:32px !important;"
                      class="ma-0"
                      flat
                      icon
                      :ripple="false">
                      <d-icon scale="0.85" name="b-download"/>
                    </v-btn>
                  </v-flex>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
      </v-container>
    </v-card>
  </v-flex>
</template>

<style lang="less">
.bill-card {
  border: 1px solid #000 !important;
  min-height: 108px;
  .fa-icon {
    margin: 0 auto;
  }
  .v-card__actions {
    font-size:0.85rem;
    .v-btn {
      &:hover {
        .fa-icon {
          color: #F58220
        }
      }
    }
  }
}
</style>

<script>
export default {
  name: 'UserBills',
  data () {
    return {
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        ruc: v => (v && v.length >= 11) || 'EL RUC debe tener al 11 caracteres'
      },
      editBill: false,
      bills: {
        1: {
          name: 'Softbutterfly',
          ruc: '20601826535',
          address: 'Av. Garcilazo de la Vega',
          pdf: 'bill_1.pdf'
        },
        2: {
          name: 'Softbutterfly 2',
          ruc: '20601826535',
          address: 'Av. Garcilazo de la Vega 2',
          pdf: 'bill_2.pdf'
        }
      }
    }
  }
}
</script>
